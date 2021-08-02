#include "transmit_uart.h"
#include <xc.h>
 
#define E 14;
#define R 27;

#define S 28;
#define U 30;
#define C 12;

#define coma 16;
#define salto 16;

//VARIABLES PARA DATOS
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
//COMANDOS
char uart_tx_comandos;
char control_uart_comandos;
char error1;
char error2;
char error3;
char success1;
char success2;
char success3;
//rtc
char mins;
char hour;
char day_number;
char month;
char year;
char prueba;
//DATOS
void transmitir_ascii_datos(char uart_tx_datos){
        int vect_transmision_datos[18] = {0x30,0x31,0x32,0x33,0x34,0x35,0x36,0x37,0x38,0x39,0x41,0x42,0x43,0x44,0x45,0x46,0x20,0x0A};     //HEXA TO ASCII
        if(PIR3bits.U1TXIF==1){                                                                                                     //CHECK BUFFER
            U1TXB=vect_transmision_datos[uart_tx_datos];                                                                                        //TRANSMIT DATA        
            prueba=vect_transmision_datos[uart_tx_datos];
        }    
   }
 
void transmitir_datos(char control_uart_datos){
                                                          
    aceleracion_3=aceleracion_1&0xF00;                                        
    aceleracion_3=aceleracion_3>>8;
    aceleracion_2=aceleracion_1&0x0F0;                                        
    aceleracion_2=aceleracion_2>>4;
    aceleracion_1=aceleracion_1&0x0F;
                                     
    deflexion_3=deflexion_1&0xF00;                                        
    deflexion_3=deflexion_3>>8;
    deflexion_2=deflexion_1&0xF0;                                        
    deflexion_2=deflexion_2>>4;
    deflexion_1=deflexion_1&0x0F;
                
    temperatura_3=temperatura_1&0xF00;                                        
    temperatura_3=temperatura_3>>8;
    temperatura_2=temperatura_1&0xF0;                                        
    temperatura_2 = temperatura_2>>4;
    temperatura_1=temperatura_1&0x0F;
    
 switch (control_uart_datos)
    {   
        case 1: 
            transmitir_ascii_datos(aceleracion_3);  
            transmitir_ascii_datos(aceleracion_2);  
            transmitir_ascii_datos(aceleracion_1);
            transmitir_ascii_datos(16);
        break;
        
        case 2: 
            transmitir_ascii_datos(deflexion_3);  
            transmitir_ascii_datos(deflexion_2);  
            transmitir_ascii_datos(deflexion_1);
            transmitir_ascii_datos(16);
        break;
        
        case 3: 
            transmitir_ascii_datos(temperatura_3);  
            transmitir_ascii_datos(temperatura_2);  
            transmitir_ascii_datos(temperatura_1);
            transmitir_ascii_datos(17);
            bandera_uart_datos=1;
        break;
        
        default:
             transmitir_ascii_datos(0xff);
        break;
    }
}

//COMANDOS
void transmitir_ascii_comandos(char uart_tx_comandos){
    int vect_transmision_comandos[43] ={0x30,0x31,0x32,0x33,0x34,0x35,0x36,0x37,0x38,0x39,0x41,0x42,0x43,0x44,0x45,0x46,0x47,0x48,0x49,0x4A,0x4B,0x4C,0x4D,0x4E,0x4F,0x50,0x51,0x52,0x53,0x54,0x55,0x56,0x57,0x58,0x59,0x5A,0x5B,0x5C,0x5D,0x5E,0x5F,0x2C,0x0A};     //HEXA TO ASCII     //HEXA TO ASCII
    if(PIR3bits.U1TXIF==1){                                                                                                     //CHECK BUFFER
        U1TXB=vect_transmision_comandos[uart_tx_comandos];                                                                                        //TRANSMIT DATA        
    }    
   }

void transmitir_comandos(char control_uart_comandos){
    error1 = E;
    error2 = R;
    error3 = R;
    
    success1= S;
    success2= U;
    success3= C;
    
 switch (control_uart_comandos)
    {   
        case 1: 
            transmitir_ascii_comandos(error1);  
            transmitir_ascii_comandos(error2);  
            transmitir_ascii_comandos(error3);  
            transmitir_ascii_comandos(42);  
        break;
        
        case 2: 
            transmitir_ascii_comandos(success1);
            transmitir_ascii_comandos(success2);
            transmitir_ascii_comandos(success3);
            transmitir_ascii_comandos(42);  
        break;
        
        default:
             transmitir_ascii_datos(0xff);
        break;
    }
}

