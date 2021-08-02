/*
 * 1 CAMBIAR FRECUENCIA DE MUESTREO A 100HZ 
 * 2 CAMBIAR FRECUENCIA DE MUESTREO A 150HZ
 * 3 CAMBIAR FRECUENCIA DE MUESTREO A 200HZ
 * 
 * 4 CAMBIAR FRECUENCIA DE GUARDADO +1min
 * 5 CAMBIAR FRECUENCIA DE GUARDADO -1min
 * 6 CAMBIAR FRECUENCIA DE GUARDADO 15 seg
 * 7 CAMBIAR FRECUENCIA DE GUARDADO 1 min
 * 
 * 8 DETENER GUARDADO EN MEMORIA
 * 
 * 9 PEDIR DATO HISTORICO
 * 
 * A CAMBIAR HORA RTC 
 */



#include <stdio.h>
#include <stdlib.h>
#include "comandos_usuario.h"
#include "transmit_uart.h"
#include "i2c.h"

char uart_rx;
char hex;
char contador_datos;
char bandera_recibido;
char bandera_recibido1;
int comando_adc;
int frec_adc;
int frec_mem;
float comando_mem;
char detener_mem;

int ascii2hex_rtc(char fecha){
    switch(fecha){
        case 48:
            return 0x00;
        break;
        
        case 49:
            return 0x01;
        break;
        
        case 50:
            return 0x02;
        break;
        
        case 51:
            return 0x03;
        break;
        
        case 52:
            return 0x04;
        break;
        
        case 53:
            return 0x05;
        break;
        
        case 54:
            return 0x06;
        break;
        
        case 55:
            return 0x07;
        break;
        
        case 56:
            return 0x08;
        break;
        
        case 57:
            return 0x09;
        break;
        
        default:
            return 0xff;
        break;
    }
}

int ascii2hex(char uart_rx){
    switch(uart_rx){
        case 49:
            hex = 0x01;
        break;
        
        case 50:
            hex = 0x02;
        break;
        
        case 51:
            hex = 0x03;
        break;
        
        case 52:
            hex = 0x04;
        break;
        
        case 53:
            hex = 0x05;
        break;
        
        case 54:
            hex = 0x06;
        break;
        
        case 55:
            hex = 0x07;
        break;
        
        case 56:
            hex = 0x08;
        break;
        
        case 57:
            hex = 0x09;
        break;
        
        case 65:
            hex = 0x0A;
        break;
        
        default:
            hex = 0xff;
        break;
        
    }
}

void command(char hex){
    switch(hex){
        case 1:
            transmitir_comandos(2);
            comando_adc=1;
            frec_adc=0;
            contador_datos=0;
        break;
        
        case 2:
            transmitir_comandos(2);
            comando_adc=2;
            frec_adc=0;
            contador_datos=0;
        break;  
        
        case 3:
            transmitir_comandos(2);
            comando_adc=3;
            frec_adc=0;
            contador_datos=0;
        break;
        
        case 4:
            transmitir_comandos(2);
            frec_mem=0;
            detener_mem=0;
            contador_datos=0;
            if(comando_mem==10){
                transmitir_comandos(1);
                comando_mem = 1;
            }    
            else{
                comando_mem = comando_mem+1;
            }
        break;
        
        case 5:
            transmitir_comandos(2);
            frec_mem=0;
            detener_mem=0;
            contador_datos=0;
            if(comando_mem==1){
                transmitir_comandos(1);
                comando_mem = 10;
            }
            else{
                comando_mem = comando_mem-1;
            }
        break;
            
        case 6:
            transmitir_comandos(2);
            frec_mem=0;
            comando_mem = 0.25;
            detener_mem=0;
            contador_datos=0;
        break;
        
        case 7:
            transmitir_comandos(2);
            frec_mem=0;
            contador_datos=0;
            comando_mem = 1;
            detener_mem=0;
        break;
        
        case 8:
            transmitir_comandos(2);
            frec_mem=0;
            contador_datos=0;
            detener_mem=(detener_mem==0)?1:0;
        break;
        
        case 9:
            transmitir_comandos(2);
            if(bandera_recibido){
                escribir_rtc();
                bandera_recibido=0;
            }    
        break;
        
        case 10:
            if(bandera_recibido1){
                contador_datos=0;
                leer_mem();
                bandera_recibido1=0;
                transmitir_datos(1);
                transmitir_datos(2);
                transmitir_datos(3);
            }
        break;

        default:
            transmitir_comandos(1);
        break;
       
    }        
}
