/*______________________________________________________________________________
 *          20/02/2021 BOGOTÁ, D.C. PONTIFICIA UNIVERSIDAD JAVERIANA           *
 *                  ING PABLO ANDRÉS RODRIGUEZ FERRO M.s.C.                    *
 *                         PROYECTO EN ELECTRÓNICA II                          *
 *                          MAIN CODE,INTERRUPT MODE                           *
 *                                 MADE BY:                                    *
 *                ANDRES ESQUIVEL andresesquivel@javeriana.edu.co              *
 *                 SEBASTIAN CEPEDA juan_cepeda@javeriana.edu.co               *
 *                   SUSANA GÓMEZ gomezsusanam@javeriana.edu.co                *
 * ____________________________________________________________________________*/

#include "BITSCONFIG.h"
#include "perifericos.h"
#include "transmit_uart.h"
#include "comandos_usuario.h"
#include "FILTRO.h"
#include "i2c.h"

char uart_rx;
char hex;
//UART DATOS
char uart_tx_datos;
int aceleracion_1;
int aceleracion_2;
int aceleracion_3;
int deflexion_1;
int deflexion_2;
int deflexion_3;
int temperatura_1;
int temperatura_2;
int temperatura_3;
char control_uart_datos;
char bandera_uart_datos;
char bandera_uart_comandos;
char contador_datos;
char bandera_recibido;
char bandera_recibido1;
//ADC
char canal;
int ADC;
int aceleracion;
int deflexion;
int temperatura; 
//TIMER
int frec_adc;
int frec_mem;
int comando_adc=1;
//FILTRO 
char banderafir;
//i2c
char secs=0x00;
char mins=0x18;
char hour=0x5C;
char day=0x02;
char day_number=0x07;
char month=0x06;
char year=0x21;
//rtc escribir
char mins_wr=0x18;
char hour_wr=0x5C;
char day_wr=0x02;
char day_number_wr=0x07;
char month_wr=0x06;
char year_wr=0x21;
char pos_memH;
char pos_memL;
//
float comando_mem = 1;
unsigned int aux=18181;
unsigned int aux1;
char detener_mem=0;

void main(){
    clk_init();
    interr();
    tmr1_init();
    adc_init();
    uart_init();
    i2c_init();
    escribir_rtc();
    //TRISBbits.TRISB5=0;  //PORTD PIN 0 SALIDA
    //ANSELBbits.ANSELB5=0;     //SALIDA DIGITAL
    while(1){
        //PORTBbits.RB5=1;
        if(!banderafir){
            aceleracion = filtrarFIR(aceleracion);
        }
        if(bandera_uart_comandos){
            ascii2hex(uart_rx); 
            command(hex);
            bandera_uart_comandos = 0;
            aux=18181*comando_mem;
        }
        if(bandera_uart_comandos==0){
            if(bandera_uart_datos==0){
                aceleracion_1 = aceleracion;
                deflexion_1 = deflexion;
                temperatura_1 = temperatura;
                control_uart_datos=(control_uart_datos>2)?1:control_uart_datos+1;
                transmitir_datos(control_uart_datos);
            }
        }
        if(!detener_mem){
            if(frec_mem==aux){
                leer_rtc();     
                frec_mem=0;
                escribir_mem();
            }
        }    
        if(frec_adc==comando_adc){
           frec_adc=0;                             //RESTART THE COUNT 
           ADCON0bits.GO_nDONE = 1;
        }
        //PORTBbits.RB5=0;
    }
}

void __interrupt (irq(IRQ_TMR1),base(0x0008)) TMR1_ISR (void){
    //PORTBbits.RB5=(PORTBbits.RB5==1)?0:1;
    frec_adc=frec_adc+1;
    frec_mem=frec_mem+1;
    TMR1L          = 0xB1;  //1m INTERRUPT
    TMR1H          = 0xE5;  //1m INTERRUPT
    PIR4bits.TMR1IF = 0; 
}

void __interrupt (irq(IRQ_U1RX),base(0x0008)) U1RX_ISR (void){
    bandera_uart_comandos = 1;
    if(contador_datos==0){
        uart_rx=U1RXB;        
    }
    else if(contador_datos==1){
        mins_wr=U1RXB;
        mins_wr=(ascii2hex_rtc(mins_wr)<<4);
    }
    else if(contador_datos==2){
        aux1=U1RXB;
        aux1=ascii2hex_rtc(aux1);
        mins_wr=mins_wr|aux1;
    }
    else if(contador_datos==3){
        hour_wr=U1RXB;
        hour_wr=(ascii2hex_rtc(hour_wr)<<4);
    }
    else if(contador_datos==4){
        aux1=U1RXB;
        aux1=ascii2hex_rtc(aux1);
        hour_wr=hour_wr|aux1;
        bandera_recibido1=1;
    }
    else if(contador_datos==5){
        day_number_wr=U1RXB;
        day_number_wr=(ascii2hex_rtc(day_number_wr)<<4);
    }
    else if(contador_datos==6){
        aux1=U1RXB;
        aux1=ascii2hex_rtc(aux1);
        day_number_wr=day_number_wr|aux1;
    }
    else if(contador_datos==7){
        month_wr=U1RXB;
        month_wr=(ascii2hex_rtc(month_wr)<<4);
    }
    else if(contador_datos==8){
        aux1=U1RXB;
        aux1=ascii2hex_rtc(aux1);
        month_wr=month_wr|aux1;
    }
    else if(contador_datos==9){
        year_wr=U1RXB;
        year_wr=(ascii2hex_rtc(year_wr)<<4);
    }
    else if(contador_datos==10){
        aux1=U1RXB;
        aux1=ascii2hex_rtc(aux1);
        year_wr=year_wr|aux1;
        bandera_recibido=1;
    }
    contador_datos=(contador_datos==10)?0:contador_datos+1;
}

void __interrupt (irq(IRQ_AD),base(0x0008)) AD_ISR (void){          //ISR ADC
        PIR1bits.ADIF = 0;                                          //CLEAN INTERRUPT FLAG
        if(canal==0){
            //PORTBbits.RB5=(PORTBbits.RB5==1)?0:1;
            ADC = ADRESH;
            ADC = ADC<<8;
            aceleracion = ADC + ADRESL;
            canal =1;
        }
        else if(canal==1){
            ADC = ADRESH;
            ADC = ADC<<8;
            deflexion = ADC + ADRESL;
            canal = 2;
        }
        else if(canal == 2){
            ADC = ADRESH;
            ADC = ADC<<8;
            temperatura = ADC + ADRESL;
            canal = 0;
        }
        ADPCH = canal;                                              //CHANGE ADC SOURCE 
        bandera_uart_datos=0;
        banderafir=0;
}        