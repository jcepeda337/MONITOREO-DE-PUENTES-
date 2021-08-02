#include "BITSCONFIG.h"
#include "perifericos.h"

void tmr1_init(void){
    T1CONbits.CKPS = 0x3;   //PRESCALER 8
    T1CONbits.RD16 = 1;     //16 BITS MODE
    T1CONbits.ON   = 1;     //TURN ON TMR1
    T1CLKbits.CS   = 0x01;  //Fosc/4 AS CLK
    T1GCON         = 0x00;  //NOT GATE CONTROL
    TMR1L          = 0xE6;  //1m INTERRUPT
    TMR1H          = 0x38;  //1m INTERRUPT
}    

void clk_init(void){
    OSCCON1bits.NDIV = 0x0;   //CLK DIVIDED BY 1
    OSCCON2bits.CDIV = 0x0;   //CLK DIVIDED BY 1
    OSCCON1bits.NOSC = 0x6;   //CLK SOURCE HFINTOSC
    OSCCON2bits.COSC = 0x6;   //CLK SOURCE HFINTOSC
    OSCFRQbits.FRQ   = 0x8;   //CLK 64MHz
    OSCTUNEbits.TUN  = 0x1F;  //MAX FREQ HFINTOSC
    OSCEN            = 0x40;  //ENA HFINTOSC DIS OTHER CLK   
}

void interr(void){
    INTCON0bits.GIE  = 1;       //ENA INTERRUPTS
    INTCON0bits.GIEH = 1;       //ENA HIGH PRIORITY INTERRUPTS
    INTCON0bits.GIEL = 1;       //ENA LOW PRIORITY INTERRUPT
    INTCON0bits.IPEN = 1;       //ENA PRIORITIES 
    INTCON1bits.STAT = 0x11;    //
    //TIMER
    PIE4bits.TMR1IE  = 1;  //ENA TMR1 INTERRUPT
    PIR4bits.TMR1IF  = 0;  //CLEAR TMR1 FLAG
    //ADC
    PIE1bits.ADIE = 1;  //ENA ADC INTERRUPT
    PIR1bits.ADIF = 0;  //CLEAR ADC FLAG
    //UART
    PIE3bits.U1IE   = 0;
    PIE3bits.U1TXIE = 0;
    PIE3bits.U1RXIE = 1;
    PIE3bits.U1EIE  = 0;
    //SET ALL INTERRUPTS LOW PRIORITY 
    IPR0  = 0x00;
    IPR1  = 0x00;
    IPR2  = 0x00;
    IPR3  = 0x00;
    IPR4  = 0x00;
    IPR5  = 0x00;
    IPR6  = 0x00;
    IPR7  = 0x00;
    IPR8  = 0x00;
    IPR9  = 0x00;
    IPR10 = 0x00;
    //PRIORIDADES
    IPR4bits.TMR1IP   = 1;  //ONLY TMR1 HIGH PRIORITY INTERR
    IPR1bits.ADIP     = 0;  //LOW PRI FOR ADC
    IPR2bits.SPI1TXIP = 0;  //LOW PRI FOR ADC
    IPR3bits.U1TXIP   = 0;
    IPR3bits.U1RXIP   = 1;
}

void adc_init(void){
    //PORT A
    TRISAbits.TRISA0   = 1; //AN0 AS CHANEL 0 (INPUT)
    TRISAbits.TRISA1   = 1; //AN1 AS CHANEL 1 (INPUT)
    ANSELAbits.ANSELA0 = 1; //A0 ANALOG
    ANSELAbits.ANSELA1 = 1;  //A1 ANALOG
    //ADC
    ADCON0bits.ON  = 1;      //TURN ON ADC
    ADCON0bits.CS  = 0;      //Fosc as CLK
    ADCON0bits.FM  = 1;      //RIGHT JUSTIFIED 
    ADCLKbits.CS   = 0x20;   //FOSC/64 = 1u CONVERSION 
    ADREFbits.NREF = 0;      //NEGATIVE REFERENCE VSS
    ADREFbits.PREF = 0x00;   //POSITIVE REFECENRE VDD
    ADPCH          = 0x00;   //CHANEL 0 
}

void uart_init(void){
    //UART
    U1CON0bits.BRGS  = 1;       //HIGH SPEED BAUDRATE 
    U1CON0bits.TXEN  = 1;       //ENA TRANSMITER 
    U1CON0bits.RXEN  = 1;       //ENA RECEIVER 
    U1CON0bits.MODE  = 0x00;    //ASYNC MODE NO PARITY
    U1CON1bits.ON    = 1;       //TURN ON SERIAL PORT 
    U1BRG            = 0x0010;  //BAUDRATE = 921600 
    //GPIO
    TRISCbits.TRISC7 = 1; //RX IN
    TRISCbits.TRISC6 = 0; //TX OUT
    ANSELCbits.ANSELC7 =0;
    ANSELCbits.ANSELC6 =0;
    RC6PPS  = 0x13; 
    U1RXPPS = 0x17;
}

void i2c_init(void){
  //GPIO
    PORTB      = 0x00; //CLEAR PORTB 
    TRISB      = 0xF9; //ANB1>SCL OUT, ANB2>SDA OUT (pag 548)
    ANSELB     = 0xF9; //ANB1, ANB2  
    WPUB       = 0x06; //WEAK PULL UP
    ODCONB     = 0x06; //OPEN DRAIN ANB1 ANB2
    SLRCONB    = 0xFF;   //LIMITED SLWE RATE
    INLVLB     = 0xFF; //TRESHOLD TTL
  //RxyI2C
    RB1I2C            = 0x01; //SCL slew rate GPIO, standar pull up, i2c input treshold
    RB2I2C            = 0x01; //SDA slew rate GPIO, standar pull up, i2c input treshold
    SLRCONBbits.SLRB1 = 1;    //SLEW RATE LIMIT
    SLRCONBbits.SLRB2 = 1;    //SLEW RATE LIMIT 
  //PPS BI-DIRECTIONAL (pag 277)
    //UNLOCK PPS
    PPSLOCK = 0x55; //FIRST STEP TO UNLOCK PPS SEQUENCE  
    PPSLOCK = 0xAA; //SECOND STEP TO UNLOCK PPS SEQUENCE
    PPSLOCK = 0x00; //UNLOCK PPS
    //PPS OUT I2C
    RB1PPS     = 0x23; //SCL on RB1 I2C2
    RB2PPS     = 0x24; //SDA on RB2 I2C2
    //PPS IN I2C
    I2C2SCLPPS = 0x09; //SCL on RB1 I2C2
    I2C2SDAPPS = 0x0A; //SDA on RB2 I2C2
    //LOCK PPS
    PPSLOCK = 0x55;
    PPSLOCK = 0xAA;
    PPSLOCK = 0x01; //LOCK PPS
  //I2C 2
    I2C2CON0        = 0x04; //MASTERMODE 7BIT ADDRESS
    I2C2CON1        = 0x80; //CLEAN ACK 
    I2C2CON2        = 0x24; //AUTO CNT DISABLE, ADDRESS BUFFER DISABLESD, 100nS HOLD TIME, BUS FREE 8CLK PULSES 
    I2C2CLK         = 0x03; //FOSC/4
    I2C2CNT         = 0x00; //CLEAR COUNTER 
    I2C2PIR         = 0x00; //CLEAR INTERRUPT FLAG
    I2C2PIE         = 0x00; //DISABLE INTERRUPTS
}