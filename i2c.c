#include "i2c.h"
#include <xc.h>

char i2c_rx;
//RTC
char secs;
char mins;
char hour;
char day;
char day_number;
char month;
char year;
char count_rtc;
//rtc escribir
char mins_wr=0x18;
char hour_wr=0x5C;
char day_wr=0x02;
char day_number_wr=0x07;
char month_wr=0x06;
char year_wr=0x21;
char pos_memH;
char pos_memL;
//memoria
int aceleracion_1;
int aceleracion_2;
int aceleracion_3;
int deflexion_1;
int deflexion_2;
int deflexion_3;
int temperatura_1;
int temperatura_2;
int temperatura_3;
int pos_memoria; //int = 2 bytes 
char count_mem;
//
int aceleracionh_1;
int aceleracionh_2;
int aceleracionh_3;
int deflexionh_1;
int deflexionh_2;
int deflexionh_3;
int temperaturah_1;
int temperaturah_2;
int temperaturah_3;


short int escribir_rtc(){
    I2C2CON0bits.EN = 1;    //ena i2c
    I2C2CNT = 8;
    I2C2ADB1 = 0xD0;
    I2C2TXB = 0x00; //reg 0
    I2C2CON0bits.S = 1;
    while (I2C2STAT1bits.TXBE==0);
    I2C2TXB = secs; // secs 
    while (I2C2STAT1bits.TXBE==0);
    I2C2TXB = mins_wr; // mins 
    while (I2C2STAT1bits.TXBE==0);
    I2C2TXB = hour_wr; //hour
    while (I2C2STAT1bits.TXBE==0);
    I2C2TXB = day_wr; //day 
    while (I2C2STAT1bits.TXBE==0);
    I2C2TXB = day_number_wr; //day 
    while (I2C2STAT1bits.TXBE==0);
    I2C2TXB = month_wr; //month 
    while (I2C2STAT1bits.TXBE==0);
    I2C2TXB = year_wr; //year
    
}

short int leer_rtc(){
    I2C2CON0bits.EN = 1;
    I2C2CNT = 1;
    I2C2ADB1 = 0xD0;
    I2C2TXB = 0x00;
    I2C2CON0bits.RSEN = 1;
    I2C2CON0bits.S = 1;
    while (I2C2STAT1bits.TXBE==0);
    while(!I2C2CON0bits.MDR);
    I2C2CNT=7;
    I2C2ADB1 = 0xD1;
    I2C2CON0bits.S = 1;
    while(I2C2CNT>0){
        while(!I2C2STAT1bits.RXBF);
        i2c_rx= I2C2RXB;
        if(count_rtc==0){
            secs=i2c_rx;
        }
        else if(count_rtc==1){
            mins=i2c_rx;
        }
        else if(count_rtc==2){
            hour=i2c_rx;
        }
        else if(count_rtc==3){
            day=i2c_rx;
        }
        else if(count_rtc==4){
            day_number=i2c_rx;
        }
        else if(count_rtc==5){
            month=i2c_rx;
        }
        else if(count_rtc==6){
            year=i2c_rx;
        }
        count_rtc=(count_rtc==6)?0:count_rtc+1;    
    }   
    I2C2CON0bits.RSEN = 0;
    while(I2C2PIRbits.PCIF==0);
    I2C2CON0bits.EN = 0;    //ena i2c
}

short int escribir_mem(){
    I2C2CON0bits.EN = 1;    //ena i2c
    I2C2CNT = 13;
    I2C2ADB1 = 0xA2;
    I2C2TXB = (pos_memoria&0xff00)>>8;
    I2C2CON0bits.S = 1;
    while (I2C2STAT1bits.TXBE==0);
    I2C2TXB = pos_memoria&0x00ff;
    while (I2C2STAT1bits.TXBE==0);
    I2C2TXB = year;
    while (I2C2STAT1bits.TXBE==0);
    I2C2TXB = month;
    while (I2C2STAT1bits.TXBE==0);
    I2C2TXB = day_number;
    while (I2C2STAT1bits.TXBE==0);
    I2C2TXB = hour;
    while (I2C2STAT1bits.TXBE==0);
    I2C2TXB = mins;
    while (I2C2STAT1bits.TXBE==0);
    I2C2TXB = aceleracion_3;
    while (I2C2STAT1bits.TXBE==0);
    I2C2TXB = (aceleracion_2<<4)|aceleracion_1;
    while (I2C2STAT1bits.TXBE==0);
    I2C2TXB = deflexion_3;
    while (I2C2STAT1bits.TXBE==0);
    I2C2TXB = (deflexion_2<<4)|deflexion_1;
    while (I2C2STAT1bits.TXBE==0);
    I2C2TXB = temperatura_3;
    while (I2C2STAT1bits.TXBE==0);
    I2C2TXB = (temperatura_2<<4)|temperatura_1;
    pos_memoria=pos_memoria+13;
    //I2C2CON0bits.EN = 0;    //ena i2c
    
 }

short int leer_mem(){
    I2C2CON0bits.EN = 1;
    I2C2CNT = 2;
    I2C2ADB1 = 0xA2;
    I2C2TXB = mins_wr;
    I2C2CON0bits.S = 1;
    while (I2C2STAT1bits.TXBE==0);
    I2C2TXB = hour_wr;
    I2C2CON0bits.RSEN = 1;
    I2C2CON0bits.S = 1;
    while (I2C2STAT1bits.TXBE==0);
    while(!I2C2CON0bits.MDR);
    I2C2CNT=11;
    I2C2ADB1 = 0xA3;
    I2C2CON0bits.S = 1;
    //
    while(I2C2CNT>0){
        while(!I2C2STAT1bits.RXBF);
        I2C2CON1bits.ACKDT=0;
        i2c_rx= I2C2RXB;
        
        if(!count_mem){
            year=i2c_rx;
        }
        else if(count_mem==1){
            month=i2c_rx;
        }
        else if(count_mem==2){
            day_number=i2c_rx;
        }
        else if(count_mem==3){
            hour=i2c_rx;
        }
        else if(count_mem==4){
            mins=i2c_rx;
        }
        else if(count_mem==5){
            aceleracionh_1=i2c_rx;
        }
        else if(count_mem==6){
            aceleracionh_2=i2c_rx;
        }
        else if(count_mem==7){
            deflexionh_1=i2c_rx;
        }
        else if(count_mem==8){
            deflexionh_2=i2c_rx;
        }
        else if(count_mem==9){
            temperaturah_1=i2c_rx;
        }
        else if(count_mem==10){
            temperaturah_2=i2c_rx;
        }
        count_mem=(count_mem==10)?0:count_mem+1;
    }
    I2C2CON0bits.S = 0;
    I2C2CON0bits.EN = 0;    //ena i2c
    while(I2C2PIRbits.PCIF==0);
 }