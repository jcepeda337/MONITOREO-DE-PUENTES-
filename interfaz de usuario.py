from tkinter import *
import serial
import sys
import time
import collections
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.lines import Line2D
import numpy as np

#CREAR PUERTO SERIAL PARA LA COMUNICACION  USANDO PYTHON
puerto= serial.Serial()
#DEFINIR VELOCIDAD EN BAUDIOS
puerto.baudrate=921600
puerto.timeout=3#tiempo hasta recibir un caracterer de fin de linea
#DEFINIR PUERTO COM DEL FTDI232
puerto.port='COM5'
#ABRIR UNA CONEXION SERIAL
puerto.open()

#CREAR PUERTO SERIAL PARA LA COMUNICACION  USANDO PYTHON
puerto= serial.Serial()
#DEFINIR VELOCIDAD EN BAUDIOS
puerto.baudrate=921600
puerto.timeout=3#tiempo hasta recibir un caracterer de fin de linea
#DEFINIR PUERTO COM DEL FTDI232
puerto.port='COM5'
#ABRIR UNA CONEXION SERIAL
puerto.open()
#Crear un objeto Tk() 
vent=Tk()
#TITULO DE LA INTERFAZ
vent.title("Interfaz Proyecto 2")
#DIMENSIONES DE LA INTERFAZ
vent.geometry('580x410')

gData=[]

contador=0
contador1=0

#DATOS CONVERSION
def HexTodec(dato):
    datodecimal=20
    if (dato=='0'):
       datodecimal=0
    if (dato=='1'):
       datodecimal=1
    if (dato=='2'):
       datodecimal=2
    if (dato=='3'):
       datodecimal=3
    if (dato=='4'):
       datodecimal=4   
    if (dato=='5'):
       datodecimal=5      
    if (dato=='6'):
       datodecimal=6     
    if (dato=='7'):
       datodecimal=7
    if (dato=='8'):
       datodecimal=8
    if (dato=='9'):
       datodecimal=9   
    if (dato=='A'):
       datodecimal=10   
    if (dato=='B'):
       datodecimal=11  
    if (dato=='C'):
       datodecimal=12  
    if (dato=='D'):
       datodecimal=13 
    if (dato=='E'):
       datodecimal=14
    if (dato=='F'):
       datodecimal=15
    return datodecimal
pass

#DATOS ENVIO DATO HISTORICO
def HexTodec2(dato):
    var1=10
    if (dato=='0'):
       var1=str('0').encode()
       puerto.write(var1)
    if (dato=='1'):
       var1=str('1').encode()
       puerto.write(var1)
    if (dato=='2'):
       var1=str('2').encode()
       puerto.write(var1)
    if (dato=='3'):
       var1=str('3').encode()
       puerto.write(var1)
    if (dato=='4'):
       var1=str('4').encode()
       puerto.write(var1)   
    if (dato=='5'):
       var1=str('5').encode()
       puerto.write(var1)      
    if (dato=='6'):
       var1=str('6').encode()
       puerto.write(var1)     
    if (dato=='7'):
       var1=str('7').encode()
       puerto.write(var1)
    if (dato=='8'):
       var1=str('8').encode()
       puerto.write(var1)
    if (dato=='9'):
       var1=str('9').encode()
       puerto.write(var1)   
    if (dato=='A'):
       var1=str('A').encode()
       puerto.write(var1)   
    if (dato=='B'):
       var1=str('B').encode()
       puerto.write(var1)  
    if (dato=='C'):
       var1=str('C').encode()
       puerto.write(var1)  
    if (dato=='D'):
       var1=str('D').encode()
       puerto.write(var1) 
    if (dato=='E'):
       var1=str('E').encode()
       puerto.write(var1)
    if (dato=='F'):
       var1=str('F').encode()
       puerto.write(var1)
    return var1
pass

#Conversión de texto interfaz
def variable(entrada):
    if (entrada=='01'):
        var1=str('0').encode()
        puerto.write(var1)
        contador=0
        while contador<10 :
            contador=contador+1
        var2=str('1').encode()
        puerto.write(var2)
        
    if (entrada=='02'):
        var1=str('0').encode()
        puerto.write(var1)
        contador=0
        while contador<10 :
            contador=contador+1
        var2=str('2').encode()
        puerto.write(var2)
        
    if (entrada=='03'):
        var1=str('0').encode()
        puerto.write(var1)
        contador=0
        while contador<10 :
            contador=contador+1
        var2=str('3').encode()
        puerto.write(var2)
        
    if (entrada=='04'):
        var1=str('0').encode()
        puerto.write(var1)
        contador=0
        while contador<10 :
            contador=contador+1
        var2=str('4').encode()
        puerto.write(var2)
        
    if (entrada=='05'):
        var1=str('0').encode()
        puerto.write(var1)
        contador=0
        while contador<10 :
            contador=contador+1
        var2=str('5').encode()
        puerto.write(var2)
        
    if (entrada=='06'):
        var1=str('0').encode()
        puerto.write(var1)
        contador=0
        while contador<10 :
            contador=contador+1
        var2=str('6').encode()
        puerto.write(var2)
        
    if (entrada=='07'):
        var1=str('0').encode()
        puerto.write(var1)
        contador=0
        while contador<10 :
            contador=contador+1
        var2=str('7').encode()
        puerto.write(var2)
        
    if (entrada=='08'):
        var1=str('0').encode()
        puerto.write(var1)
        contador=0
        while contador<10 :
            contador=contador+1
        var2=str('8').encode()
        puerto.write(var2)
        
    if (entrada=='09'):
        var1=str('0').encode()
        puerto.write(var1)
        contador=0
        while contador<10 :
            contador=contador+1
        var2=str('9').encode()
        puerto.write(var2)
        
    if (entrada=='10'):
        var1=str('1').encode()
        puerto.write(var1)
        contador=0
        while contador<10 :
            contador=contador+1
        var2=str('0').encode()
        puerto.write(var2)
        
    if (entrada=='11'):
        var1=str('1').encode()
        puerto.write(var1)
        contador=0
        while contador<10 :
            contador=contador+1
        var2=str('1').encode()
        puerto.write(var2)
        
    if (entrada=='12'):
        var1=str('1').encode()
        puerto.write(var1)
        contador=0
        while contador<10 :
            contador=contador+1
        var2=str('2').encode()
        puerto.write(var2)
        
    if (entrada=='13'):
        var1=str('1').encode()
        puerto.write(var1)
        contador=0
        while contador<10 :
            contador=contador+1
        var2=str('3').encode()
        puerto.write(var2)
        
    if (entrada=='14'):
        var1=str('1').encode()
        puerto.write(var1)
        contador=0
        while contador<10 :
            contador=contador+1
        var2=str('4').encode()
        puerto.write(var2)
        
    if (entrada=='15'):
        var1=str('1').encode()
        puerto.write(var1)
        contador=0
        while contador<10 :
            contador=contador+1
        var2=str('5').encode()
        puerto.write(var2)
        
    if (entrada=='16'):
        var1=str('1').encode()
        puerto.write(var1)
        contador=0
        while contador<10 :
            contador=contador+1
        var2=str('6').encode()
        puerto.write(var2)
        
    if (entrada=='17'):
        var1=str('1').encode()
        puerto.write(var1)
        contador=0
        while contador<10 :
            contador=contador+1
        var2=str('7').encode()
        puerto.write(var2)
        
    if (entrada=='18'):
        var1=str('1').encode()
        puerto.write(var1)
        contador=0
        while contador<10 :
            contador=contador+1
        var2=str('8').encode()
        puerto.write(var2)
        
    if (entrada=='19'):
        var1=str('1').encode()
        puerto.write(var1)
        contador=0
        while contador<10 :
            contador=contador+1
        var2=str('9').encode()
        puerto.write(var2)
        
    if (entrada=='20'):
        var1=str('2').encode()
        puerto.write(var1)
        contador=0
        while contador<10 :
            contador=contador+1
        var2=str('0').encode()
        puerto.write(var2)
        
    if (entrada=='21'):
        var1=str('2').encode()
        puerto.write(var1)
        contador=0
        while contador<10 :
            contador=contador+1
        var2=str('1').encode()
        puerto.write(var2)
        
    if (entrada=='22'):
        var1=str('2').encode()
        puerto.write(var1)
        contador=0
        while contador<10 :
            contador=contador+1
        var2=str('2').encode()
        puerto.write(var2)
        
    if (entrada=='23'):
        var1=str('2').encode()
        puerto.write(var1)
        contador=0
        while contador<10 :
            contador=contador+1
        var2=str('3').encode()
        puerto.write(var2)
        
    if (entrada=='24'):
        var1=str('2').encode()
        puerto.write(var1)
        contador=0
        while contador<10 :
            contador=contador+1
        var2=str('4').encode()
        puerto.write(var2)
        
    if (entrada=='25'):
        var1=str('2').encode()
        puerto.write(var1)
        contador=0
        while contador<10 :
            contador=contador+1
        var2=str('5').encode()
        puerto.write(var2)
        
    if (entrada=='26'):
        var1=str('2').encode()
        puerto.write(var1)
        contador=0
        while contador<10 :
            contador=contador+1
        var2=str('6').encode()
        puerto.write(var2)
        
    if (entrada=='27'):
        var1=str('2').encode()
        puerto.write(var1)
        contador=0
        while contador<10 :
            contador=contador+1
        var2=str('7').encode()
        puerto.write(var2)
        
    if (entrada=='28'):
        var1=str('2').encode()
        puerto.write(var1)
        contador=0
        while contador<10 :
            contador=contador+1
        var2=str('8').encode()
        puerto.write(var2)
        
    if (entrada=='29'):
        var1=str('2').encode()
        puerto.write(var1)
        contador=0
        while contador<10 :
            contador=contador+1
        var2=str('9').encode()
        puerto.write(var2)
        
    if (entrada=='30'):
        var1=str('3').encode()
        puerto.write(var1)
        contador=0
        while contador<10 :
            contador=contador+1
        var2=str('0').encode()
        puerto.write(var2)
        
    if (entrada=='31'):
        var1=str('3').encode()
        puerto.write(var1)
        contador=0
        while contador<10 :
            contador=contador+1
        var2=str('1').encode()
        puerto.write(var2)
        
    if (entrada=='32'):
        var1=str('3').encode()
        puerto.write(var1)
        contador=0
        while contador<10 :
            contador=contador+1
        var2=str('2').encode()
        puerto.write(var2)
        
    if (entrada=='33'):
        var1=str('3').encode()
        puerto.write(var1)
        contador=0
        while contador<10 :
            contador=contador+1
        var2=str('3').encode()
        puerto.write(var2)
        
    if (entrada=='34'):
        var1=str('3').encode()
        puerto.write(var1)
        contador=0
        while contador<10 :
            contador=contador+1
        var2=str('4').encode()
        puerto.write(var2)
        
    if (entrada=='35'):
        var1=str('3').encode()
        puerto.write(var1)
        contador=0
        while contador<10 :
            contador=contador+1
        var2=str('5').encode()
        puerto.write(var2)
        
    if (entrada=='36'):
        var1=str('3').encode()
        puerto.write(var1)
        contador=0
        while contador<10 :
            contador=contador+1
        puerto.write(var2)
        
    if (entrada=='37'):
        var1=str('3').encode()
        puerto.write(var1)
        contador=0
        while contador<10 :
            contador=contador+1
        var2=str('7').encode()
        puerto.write(var2)
        
    if (entrada=='38'):
        var1=str('3').encode()
        puerto.write(var1)
        contador=0
        while contador<10 :
            contador=contador+1
        var2=str('8').encode()
        puerto.write(var2)
        
    if (entrada=='39'):
        var1=str('3').encode()
        puerto.write(var1)
        contador=0
        while contador<10 :
            contador=contador+1
        var2=str('9').encode()
        puerto.write(var2)
        
    if (entrada=='40'):
        var1=str('4').encode()
        puerto.write(var1)
        contador=0
        while contador<10 :
            contador=contador+1
        var2=str('0').encode()
        puerto.write(var2)
        
    if (entrada=='41'):
        var1=str('4').encode()
        puerto.write(var1)
        contador=0
        while contador<10 :
            contador=contador+1
        var2=str('1').encode()
        puerto.write(var2)
        
    if (entrada=='42'):
        var1=str('4').encode()
        puerto.write(var1)
        contador=0
        while contador<10 :
            contador=contador+1
        var2=str('2').encode()
        puerto.write(var2)
        
    if (entrada=='43'):
        var1=str('4').encode()
        puerto.write(var1)
        contador=0
        while contador<10 :
            contador=contador+1
        var2=str('3').encode()
        puerto.write(var2)
        
    if (entrada=='44'):
        var1=str('4').encode()
        puerto.write(var1)
        contador=0
        while contador<10 :
            contador=contador+1
        var2=str('4').encode()
        puerto.write(var2)
        
    if (entrada=='45'):
        var1=str('4').encode()
        puerto.write(var1)
        contador=0
        while contador<10 :
            contador=contador+1
        var2=str('5').encode()
        puerto.write(var2)
        
    if (entrada=='46'):
        var1=str('4').encode()
        puerto.write(var1)
        contador=0
        while contador<10 :
            contador=contador+1
        var2=str('6').encode()
        puerto.write(var2)  
        
    if (entrada=='47'):
        var1=str('4').encode()
        puerto.write(var1)
        contador=0
        while contador<10 :
            contador=contador+1
        var2=str('7').encode()
        puerto.write(var2)
        
    if (entrada=='48'):
        var1=str('4').encode()
        puerto.write(var1)
        contador=0
        while contador<10 :
            contador=contador+1
        var2=str('8').encode()
        puerto.write(var2)
        
    if (entrada=='49'):
        var1=str('4').encode()
        puerto.write(var1)
        contador=0
        while contador<10 :
            contador=contador+1
        var2=str('9').encode()
        puerto.write(var2)
        
    if (entrada=='50'):
        var1=str('5').encode()
        puerto.write(var1)
        contador=0
        while contador<10 :
            contador=contador+1
        var2=str('0').encode()
        puerto.write(var2)
        
    if (entrada=='51'):
        var1=str('5').encode()
        puerto.write(var1)
        contador=0
        while contador<10 :
            contador=contador+1
        var2=str('1').encode()
        puerto.write(var2)
        
    if (entrada=='52'):
        var1=str('5').encode()
        puerto.write(var1)
        contador=0
        while contador<10 :
            contador=contador+1
        var2=str('2').encode()
        puerto.write(var2)
        
    if (entrada=='53'):
        var1=str('5').encode()
        puerto.write(var1)
        contador=0
        while contador<10 :
            contador=contador+1
        var2=str('3').encode()
        puerto.write(var2)
        
    if (entrada=='54'):
        var1=str('5').encode()
        puerto.write(var1)
        contador=0
        while contador<10 :
            contador=contador+1
        var2=str('4').encode()
        puerto.write(var2)
        
    if (entrada=='55'):
        var1=str('5').encode()
        puerto.write(var1)
        contador=0
        while contador<10 :
            contador=contador+1
        var2=str('5').encode()
        puerto.write(2)
        
    if (entrada=='56'):
        var1=str('5').encode()
        puerto.write(var1)
        contador=0
        while contador<10 :
            contador=contador+1
        var2=str('6').encode()
        puerto.write(var2)
        
    if (entrada=='57'):
        var1=str('5').encode()
        puerto.write(var1)
        contador=0
        while contador<10 :
            contador=contador+1
        var2=str('7').encode()
        puerto.write(var2)
        
    if (entrada=='58'):
        var1=str('5').encode()
        puerto.write(var1)
        contador=0
        while contador<10 :
            contador=contador+1
        var2=str('8').encode()
        puerto.write(var2)
        
    if (entrada=='59'):
        var1=str('5').encode()
        puerto.write(var1)
        contador=0
        while contador<10 :
            contador=contador+1
        var2=str('9').encode()
        puerto.write(var2)
        
    pass
    
##SERIAL GRAFICA
def getSerialData(self, Samples, numData, serialConnection, lines):
    contador1=0
    while True :
        contador1=contador1+1
        line=puerto.readline().decode('utf-8')
        separado= line.split(' ') 
        print(line)            
        "aceleracion"
        aceleracion = separado[0]
        aceleracion1= aceleracion[0: 1]
        aceleracion2= aceleracion[1: 2]
        aceleracion3= aceleracion[2: 3]
               
        "deflexion"
        deflexion = separado[1]
        deflexion1= deflexion[0: 1]
        deflexion2= deflexion[1: 2]
        deflexion3= deflexion[2: 3]
                
        "temperatura"
        temperatura = separado[2]
        temperatura1= temperatura[0: 1]
        temperatura2= temperatura[1: 2]
        temperatura3= temperatura[2: 3]
             
        "conversion a voltaje-aceleracion"
        aceleracion4=HexTodec(aceleracion1) * 16 * 16
        aceleracion5=HexTodec(aceleracion2) * 16
        aceleracion6=HexTodec(aceleracion3)
        voltacele=(aceleracion4 + aceleracion5 + aceleracion6) * 5 / 4096
              
        "conversion a voltaje-deflexion"
        deflexion4=HexTodec(deflexion1) * 16 * 16
        deflexion5=HexTodec(deflexion2) * 16
        deflexion6=HexTodec(deflexion3)
        voltdef=(deflexion4 + deflexion5 + deflexion6) * 5 / 4096
            
        "conversion a voltaje-temperatura"
        temperatura4=HexTodec(temperatura1) * 16 * 16
        temperatura5=HexTodec(temperatura2) * 16
        temperatura6=HexTodec(temperatura3)
        volttemp=(temperatura4 + temperatura5 + temperatura6) * 5 / 4096
       
        medicionacele=((voltacele*0.5963)-1.5398)
        mediciondef=((voltdef+2.4313)/0.039)
        mediciontemp=((volttemp*18.756)-15.415)
        
        print(voltacele,medicionacele)
        print(voltdef,mediciondef)
        
        datos=[medicionacele,mediciondef,mediciontemp]
        print(datos)
        
        for i in range(numData):
            datos[i]=float(datos[i])
            lines[i].set_data(range(Samples),datos[i]) # Dibujar nueva linea / Drawn new line
        print(datos[0])
        tex.delete(1.0,END)
        
        if(medicionacele>0.11 or medicionacele<0.56):
            tex.insert(1.0,"  ALERTA: medición del acelerómetro no es normal")
            var1=str('6').encode()
            puerto.write(var1)
            print(var1)
            contador=0
            while contador<30 :
                contador=contador+1
            var2=str('7').encode()
            puerto.write(var2)

            if(mediciondef>300 or mediciondef<7347):
                tex.insert(1.0,"ALERTA: medición de la galga no es normal")
                var1=str('6').encode()
                puerto.write(var1)
                print(var1)
                contador=0
                while contador<30 :
                    contador=contador+1
                var2=str('7').encode()
                puerto.write(var2)
                    
                if(mediciontemp>100 or mediciontemp<-10):
                    tex.insert(1.0,"ALERTA: medición del temperatura no es normal")
                    var1=str('6').encode()
                    puerto.write(var1)
                    print(var1)
                    contador=0
                    while contador<30 :
                        contador=contador+1
                    var2=str('7').encode()
                    puerto.write(var2)
       
#----------------------------------------
#CREACION DE FUNCIONES PARA CADA BOTON DE LA INTERFAZ GRAFICA

def boton1(): #CUANDO SE PRESIONA EL BOTON DE "LED ON"
    global vent
    numero=str('4')
    b = numero.encode()
    print(b)
    puerto.write(b)
    tex.delete(1.0,END)
    
    #INSERTAR UN MENSJAE EN LA INTERFAZ GRAFICA
    tex.insert(1.0,"Frecuencia de guardado en memoria +1")
   
def boton2():#CUANDO SE PRESIONA EL BOTON DE "LED OFF"
    global vent
    numero=str('5')
    b = numero.encode()
    print(b)
    puerto.write(b)
    tex.delete(1.0,END)
    
    #INSERTAR UN MENSJAE EN LA INTERFAZ GRAFICA
    tex.insert(1.0,"Frecuencia de guardado en memoria -1")

def boton3():#CUANDO SE PRESIONA EL BOTON DE "LED BLINK"
    global vent
    numero=str('1')
    b = numero.encode()
    print(b)
    puerto.write(b)
    tex.delete(1.0,END)
    
    #INSERTAR UN MENSJAE EN LA INTERFAZ GRAFICA
    tex.insert(1.0,"Frecuencia de muestreo x1")

def boton4():
    global vent
    numero=str('2')
    b = numero.encode()
    print(b)
    puerto.write(b)
    tex.delete(1.0,END)
    
    #INSERTAR UN MENSJAE EN LA INTERFAZ GRAFICA
    tex.insert(1.0,"Frecuencia de muestreo x2")
    
def boton5():
    numero=str('3')
    b = numero.encode()
    print(b)
    puerto.write(b)
    tex.delete(1.0,END)
    
    #INSERTAR UN MENSJAE EN LA INTERFAZ GRAFICA
    tex.insert(1.0,"Frecuencia de muestreo x3")
    
def boton6():
    global vent
    numero=str('9')
    b = numero.encode()
    print(b)
    puerto.write(b)
    
    tex.delete(1.0,END)
    #INSERTAR UN MENSJAE EN LA INTERFAZ GRAFICA
    tex.insert(1.0,"Cambio fecha/hora RTC")
    
def boton7():
    global vent
    numero=str('A')
    b = numero.encode()
    print(b)
    puerto.write(b)
    tex.delete(1.0,END)
    
    tex.insert(1.0,"Pedir dato histórico")
    
def boton8():
    global vent, contador
    numero=str('8')
    b = numero.encode()
    print(b)
    puerto.write(b)
    tex.delete(1.0,END)
    contador=contador+1
    print(contador)
    if(contador==1):
        tex.insert(1.0,"Detener guardado en memoria")
    if (contador==2):
        tex.insert(1.0, "Activar guardado en memoria")
        contador=0
    
def boton9():
    Vminuto2=Vminuto.get()
    print(Vminuto2)
    Vminuto3=variable(Vminuto2)

def boton10():
    Vhora2=Vhora.get()
    print(Vhora2)
    Vhora3=variable(Vhora2)
    
def boton11():
    Vdia2=Vdia.get()
    print(Vdia2)
    Vdia3=variable(Vdia2)

def boton12():
    Vmes2=Vmes.get()
    print(Vmes2)
    Vmes3=variable(Vmes2)
    
def boton13():
    Vaño2=Vaño.get()
    print(Vaño2)
    Vaño3=variable(Vaño2)
    
def boton14():
    Vregisalto2=Vregisalto.get()
    print(Vregisalto2)
    
    Vregisalto3=Vregisalto2[0: 1]
    Vregisalto4=Vregisalto2[1: 2]
    
    print(Vregisalto3,Vregisalto4)
    
    Vregisalto5=HexTodec2(Vregisalto3)
    Vregisalto6=HexTodec2(Vregisalto4)
    
    print(Vregisalto5,Vregisalto6)
    
def boton15():
    Vregisbajo2=Vregisbajo.get()
    print(Vregisbajo2)
    Vregisbajo3=Vregisbajo2[0: 1]
    Vregisbajo4=Vregisbajo2[1: 2]
    
    print(Vregisbajo3,Vregisbajo4)
    
    Vregisbajo5=HexTodec2(Vregisbajo3)
    Vregisbajo6=HexTodec2(Vregisbajo4)
    
    print(Vregisbajo5,Vregisbajo6)
    
    ##Leer puerto
    dato1=puerto.read()
    dato2=puerto.read()
    dato3=puerto.read()
    dato4=puerto.read() ##espacio
    dato5=puerto.read()
    dato6=puerto.read()
    dato7=puerto.read()
    dato8=puerto.read() ##Espacio
    dato9=puerto.read()
    dato10=puerto.read()
    dato11=puerto.read()
    dato12=puerto.read() ##Salto de linea
    
    ##Convertir a decimal
    datohisto1=HexTodec(dato1.decode('utf-8')) * 16 * 16
    datohisto2=HexTodec(dato2.decode('utf-8')) * 16
    datohisto3=HexTodec(dato3.decode('utf-8'))
    datohisto5=HexTodec(dato5.decode('utf-8')) * 16 * 16
    datohisto6=HexTodec(dato6.decode('utf-8')) * 16
    datohisto7=HexTodec(dato7.decode('utf-8'))
    datohisto9=HexTodec(dato9.decode('utf-8')) * 16 * 16
    datohisto10=HexTodec(dato10.decode('utf-8')) * 16
    datohisto11=HexTodec(dato11.decode('utf-8'))
    
    #Convertir a dato
    datoacele=(datohisto1 + datohisto2 + datohisto3) * 5 / 4096
    datodef=(datohisto5 + datohisto6 + datohisto7) * 5 / 4096
    datotemp=(datohisto9 + datohisto10 + datohisto11) * 5 / 4096
    
    #print(dato1,dato2,dato3,dato4,dato5,dato6,dato7,dato8,dato9,dato10,dato11,dato12)
   
    #print(datoacele, datodef, datotemp)
    
    tex.delete(1.0,END)
    #INSERTAR UN MENSJAE EN LA INTERFAZ GRAFICA
    tex.insert(1.0,"Dato histórico acelerómetro: ")
    tex.insert(2.0, datoacele)
    tex.insert(3.1,"  Dato histórico deflexión:  ")
    tex.insert(4.1, datodef)
    tex.insert(5.2,"Dato histórico temperatura: ")
    tex.insert(6.2, datotemp)
    
def boton16():
    Samples = 5000  #Muestras / Samples
    sampleTime = 200  #Tiempo de muestreo / Sample Time
    numData = 3
    
    # Limites de los ejes / Axis limit
    xmin = 0
    xmax = Samples
    ymin = [0, 0 , -20]
    ymax = [1, 1 , 110]
    lines = []
    data = []
    
    for i in range(numData):
        data.append(collections.deque([0] * Samples, maxlen=Samples))
        lines.append(Line2D([], [], color='blue'))
      
    fig = plt.figure()# Crea una nueva figura #Create a new figure.
    
    ax1 = fig.add_subplot(3, 1, 1,xlim=(xmin, xmax), ylim=(ymin[0] , ymax[0]))
    ax1.title.set_text('Aceleración')
    ax1.set_xlabel("Muestras")
    ax1.set_ylabel("G")
    ax1.add_line(lines[0])
    
    ax2 = fig.add_subplot(3, 1, 2, xlim=(xmin, xmax), ylim=(ymin[1] , ymax[1]))
    ax2.title.set_text('Deflexión')
    ax2.set_xlabel("Muestras")
    ax2.set_ylabel("Esfuerzo unitario")
    ax2.add_line(lines[1])
    
    ax3 = fig.add_subplot(3, 1, 3, xlim=(xmin, xmax), ylim=(ymin[2] , ymax[2]))
    ax3.title.set_text('Temperatura')
    ax3.set_xlabel("Muestras")
    ax3.set_ylabel("°C")
    ax3.add_line(lines[2])
    
    plt.tight_layout()
        
    anim = animation.FuncAnimation(fig,getSerialData, fargs=(Samples,numData,puerto,lines), interval=sampleTime)
    
    plt.show()
    
    tex.delete(1.0,END)
    tex.insert(1.0,"Gráficar datos")
       
#-------------------------------------------------------------------------------------
#CREACION DE BOTONES
b1=Button(vent,text='+1',command=boton1,cursor='arrow')
b2=Button(vent,text='-1',command=boton2,cursor='arrow')
b3=Button(vent,text='x1',command=boton3,cursor='arrow')
b4=Button(vent,text='x2',command=boton4,cursor='arrow') 
b5=Button(vent,text='x3',command=boton5,cursor='arrow') 
b6=Button(vent,text='Cambiar fecha/hora del RTC',command=boton6,cursor='arrow') 
b7=Button(vent,text='Pedir dato histórico',command=boton7,cursor='arrow') 
b8=Button(vent,text='Detener guardado en memoria',command=boton8,cursor='arrow')
b9=Button(vent,text='Enviar minuto',command=boton9,cursor='arrow')
b10=Button(vent,text='Enviar hora',command=boton10,cursor='arrow')
b11=Button(vent,text='Enviar dia',command=boton11,cursor='arrow')
b12=Button(vent,text='Enviar mes',command=boton12,cursor='arrow')
b13=Button(vent,text='Enviar año',command=boton13,cursor='arrow')
b14=Button(vent,text='Enviar',command=boton14,cursor='arrow')
b15=Button(vent,text='Enviar',command=boton15,cursor='arrow')
b16=Button(vent,text='Gráficar',command=boton16,cursor='arrow')

#CREACION DE ETIQUETAS 
nota=Label(vent, text='ADVERTENCIA: LEER EL MANUAL DE USUARIO COMPLETO ANTES DE UTILIZAR')
titulo=Label(vent,text='Interfaz Proyecto 2')
titulob1=Label(vent,text='Tiempo de guardado en memoria')
titulob3=Label(vent,text='Frecuencia de muestreo')
minuto=Label(vent,text='minuto:')
hora=Label(vent,text='hora:')
dia=Label(vent,text='dia:')
mes=Label(vent,text='mes:')
año=Label(vent,text='año:')
regisalto=Label(vent,text='Registro alto:')
regisbajo=Label(vent,text='Registro bajo:')

#CREACION DE TEXTO
tex= Text(vent,width=43,height=3)

#CREACION VARIABLES
Vminuto=StringVar()
Vhora=StringVar()
Vdia=StringVar()
Vmes=StringVar()
Vaño=StringVar()
Vregisalto=StringVar()
Vregisbajo=StringVar()

#CREACION DE ENTRADAS
entrada1=Entry(vent,textvariable=Vminuto)
entrada2=Entry(vent,textvariable=Vhora)
entrada3=Entry(vent,textvariable=Vdia)
entrada4=Entry(vent,textvariable=Vmes)
entrada5=Entry(vent,textvariable=Vaño)
entrada6=Entry(vent,textvariable=Vregisalto)
entrada7=Entry(vent,textvariable=Vregisbajo)

#ESTABLECER POSICIONES DE LOS BOTONES EN LA INTERFAZ GRAFICA
b1.place(x=80,y=93)
b2.place(x=145,y=93)
b3.place(x=400,y=93)
b4.place(x=435,y=93)
b5.place(x=470,y=93)
b6.place(x=40,y=150)
b7.place(x=390,y=150)
b8.place(x=365,y=270)
b9.place(x=180,y=183)
b10.place(x=185,y=213)
b11.place(x=188,y=243)
b12.place(x=184,y=273)
b13.place(x=185,y=303)
b14.place(x=530,y=180)
b15.place(x=530,y=213)
b16.place(x=430,y=310)

#POSICION DE LAS ENTRADAS
entrada1.place(x=50,y=185)
entrada2.place(x=50,y=217)
entrada3.place(x=50,y=247)
entrada4.place(x=50,y=277)
entrada5.place(x=50,y=307)
entrada6.place(x=400,y=185)
entrada7.place(x=400,y=217)

#ESTABLECER POSICIONES DE LAS ETQIUETAS Y TEXTOS EN LA INTERFAZ GRAFICA
nota.place(x=80,y=0)
titulo.place(x=250,y=30)
titulob1.place(x=40,y=70)
titulob3.place(x=380,y=70)
minuto.place(x=0,y=183)
hora.place(x=10,y=213)
dia.place(x=13,y=244)
mes.place(x=11,y=274)
año.place(x=11,y=304)
regisalto.place(x=324,y=183)
regisbajo.place(x=322,y=213)

#ESTABLECER POSICIÓN DEL TEXTO
tex.place(x=110,y=345)

#MOSTRAR LA INTERFAZ
vent.mainloop()

#CERRAR EL PUERTO SERIAL
puerto.close()
sys.exit(0)