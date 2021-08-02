#include "FILTRO.h"
#include <xc.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

char banderafir;
int aceleracion;

int N=9;
int b[9] = {0,    2,   22,   62,   84,   62,   22,    2,    0};
int x[9];


volatile int k=0;
long y = 0;
volatile int j=0;




long filtrarFIR(int aceleracion){
    int i=0;
    x[k]=aceleracion;
    int indx=k;
    int indx2 = (indx+1)%(N);
    int *apuntadorB  = &b[0];
    int *apuntadorX  = &x[indx];
    int *apuntadorX2 = &x[indx2];
    long y=0;
    
    j= ((N%2)==0) ? 0:1;
    //PORTD = 0;
    for (i=0; i<(N-j)/2; ++i){
        y +=((long)(*apuntadorX)+(long)(*apuntadorX2)) * (long)(*apuntadorB);
        apuntadorB++;
        
        if(indx2!=(N-1)){
            apuntadorX2++;
            indx2++;    
        }
        else{
            apuntadorX2=&x[0];
            indx2=0;
        }
        if(indx!=0){
            apuntadorX--;
            indx--;
        }
        else{
            apuntadorX=&x[N-1];
            indx=N-1;
        }
    }
    
    if(j==1){
        y+=((long)(*apuntadorX)) * (long)(*apuntadorB);
    }
    
    k = (k>=N-1) ? 0:(k+1);      
      
    banderafir = 1; 
    //PORTD = 1;  //TOGGLE PORTD
    return y>>8;
}

