"""
Instituto TecnolÃ³gico de Costa Rica
Computer Engineering
Taller de ProgramaciÃ³n

Ejemplo Consola Cliente
Implementación del módulo NodeMCU
Proyecto 2, semestre 1
2019

Profesor: Milton Villegas Lemus
Autor: Santiago Gamboa RamÃ­rez

Restricciónes: Python3.7 
Ejemplo de como usar el módudo NodeMCU de wifiConnection

"""
#           _____________________________
#__________/BIBLIOTECAS
from tkinter import *               # Tk(), Label, Canvas, Photo
from threading import Thread        # p.start()
import threading                    # 
import os                           # ruta = os.path.join('')
import time                         # time.sleep(x)
from tkinter import messagebox      # AskYesNo ()
import tkinter.scrolledtext as tkscrolled
import winsound
from copy import *
from random import randrange as azar
##### Biblioteca para el Carro
from WiFiClient import NodeMCU #LLAMA AL PROGRAMA
#_________________________________Funciones para el trabajo con archivos______________________________________#
try:#Intenta abrir los archivos
    File1=open("Nombres.txt","r")#Se abre archivo con los nombres registrados
    File2=open("Estado.txt","r")#Se abre archivo con los estados
    File3=open("Temperaturas.txt","r")#Se abre archivos con las temperaturas registradas
    File4=open("Tiempo de Giro.txt","r")#Se abre archivo con los tiempos de giros registrados
    File5=open("Aceleraciones.txt","r")#Se abre archivo con las aceleraciones registradas
except:#En caso de que se presente un error durante el proceso, crea unos nuevos archivos
    File1=open("Nombres.txt","w")#Se abre un nuevo archivo en blanco para los nombres
    File2=open("Estado.txt","w")#Se abre un nuevo archivo en blanco para los estados
    File3=open("Temperaturas.txt","w")#Se abre un nuevo archivo en blanco para las temperaturas
    File4=open("Tiempo de Giro.txt","w")#Se abre un nuevo archivo en blanco para los tiempos de giro
    File5=open("Aceleraciones.txt","w")#Se abre un nuevo archivo en blanco para las aceleraciones
    #_____________________Se escriben contenidos genericos en los archivos_________________________#
    File1.writelines(["Maria\n","Pedro\n","Arnoldo\n","Randall\n","Esteban\n","Carlos\n","Ignacio\n","Eduardo\n","Daniel\n","Isaac\n","Erick\n","Pablo\n","Michelle\n","Mario\n"])
    File2.writelines(["OK\n","OK\n","OK\n","OK\n","OK\n","OK\n","OK\n","OK\n","OK\n","OK\n","OK\n","OK\n","OK\n","OK\n"])
    File3.writelines(["230\n","30\n","90\n","75\n","65\n","23\n","43\n","77\n","12\n","94\n","54\n","88\n","63\n","19\n"])
    File4.writelines(["11\n","12\n","13\n","14\n","15\n","16\n","17\n","18\n","19\n","20\n","21\n","22\n","23\n","24\n"])
    File5.writelines(["10\n","120\n","33\n","95\n","12\n","13\n","126\n","312\n","99\n","133\n","16\n","122\n","38\n","101\n"])
    File1.close()#Se cierra el archivo
    File2.close()#Se cierra el archivo
    File3.close()#Se cierra el archivo
    File4.close()#Se cierra el archivo
    File5.close()#Se cierra el archivo
    File1=open("Nombres.txt","r")#Se abre archivo con los nombres registrados en modo lectura
    File2=open("Estado.txt","r")#Se abre archivo con los estados en modo lectura
    File3=open("Temperaturas.txt","r")#Se abre archivos con las temperaturas registradas
    File4=open("Tiempo de Giro.txt","r")#Se abre archivo con los tiempos de giros registrados
    File5=open("Aceleraciones.txt","r")#Se abre un nuevo archivo en blanco para las aceleraciones en modo lectura
#--------------------Funcion eliminar el fin de linea ----------------------#
def eliminar(Lista):
    if len(Lista)==1:#Condicion de finalizacion
        return [Lista[0][:-1]]
    else:
        return [Lista[0][:-1]]+eliminar(Lista[1:])
#--------------------Funcion generalizar todos los numeros como float ----------------------#
def homogenizar(Lista):#Funcion para volver todos los datos numericos, datos con punto flotante
    Resultado=[]#Variable a devolver
    while(Lista)!=[]:#Condicional del bulce
        Resultado+=[float(Lista[0])]#Convierte el dato en un float
        Lista=Lista[1:]
    return Resultado#Retorna Resultado
        
#-----------------Funcion para ordenar los puntajes respecto a las aceleraciones-------------#
def ordenar_por_aceleracion():#Funcion para ordenar varias listas con respecto al valor en una lista especifica
    global Nombres,Estado_Coche,Registro_Temperatura,Registro_Giros,Registro_Aceleraciones#Se importan las variables globales
    Mayor=float(Registro_Aceleraciones[0])#Se asume como mayor el primer elemento de la lista
    Respaldo_Nombres=[]#Datos que remplazaran a la lista de nombres.Mismo contenido, con orden diferente
    Respaldo_Estado_Coche=[]#Datos que remplazaran a la lista de Estados.Mismo contenido, con orden diferente
    Respaldo_Registro_Temperatura=[]#Datos que remplazaran a la lista de Temperaturas.Mismo contenido, con orden diferente
    Respaldo_Registro_Giros=[]#Datos que remplazaran a la lista de giros.Mismo contenido, con orden diferente
    Respaldo_Registro_Aceleraciones=[]#Datos que remplazaran a la lista de aceleraciones.Mismo contenido, con orden diferente
    Cuenta=len(Registro_Aceleraciones)#Determina la cardinalidad de la lista de aceleraciones
    while len(Respaldo_Registro_Aceleraciones)!=Cuenta:#Mientras la nueva lista no tenga la misma cantidad de elementos que tenia la primera lista
        for i in Registro_Aceleraciones:#i toma el valor de cada uno de los elementos de una lista
            i=float(i)#Lo convierte en un float
            if i>Mayor:#Se el dato a evaluar es mayor al dato anterior, este lo remplaza
                Mayor=i#Una vez se haya obtenido el mayor en ese momento de la lista, se determina la posicion del mismo
        Indice=Registro_Aceleraciones.index(Mayor)#Se determina el indice de la posicion para el mismo
        Respaldo_Nombres+=[Nombres[Indice]]#Agrega el elemento correspondiente a esa posicion en la nueva lista
        Nombres.pop(Indice)#Elimina el dato en dicha posicion de la lista original
        Respaldo_Estado_Coche+=[Estado_Coche[Indice]]#Agrega el elemento correspondiente a esa posicion en la nueva lista
        Estado_Coche.pop(Indice)#Elimina el dato en dicha posicion de la lista original
        Respaldo_Registro_Temperatura+=[Registro_Temperatura[Indice]]#Agrega el elemento correspondiente a esa posicion en la nueva lista
        Registro_Temperatura.pop(Indice)#Elimina el dato en dicha posicion de la lista original
        Respaldo_Registro_Giros+=[Registro_Giros[Indice]]#Agrega el elemento correspondiente a esa posicion en la nueva lista
        Registro_Giros.pop(Indice)#Elimina el dato en dicha posicion de la lista original
        Respaldo_Registro_Aceleraciones+=[Registro_Aceleraciones[Indice]]#Agrega el elemento correspondiente a esa posicion en la nueva lista
        Registro_Aceleraciones.pop(Indice)#Elimina el dato en dicha posicion de la lista original
        try:#Trata de obtener el nuevo dato inicial de comparacion para repetir el proceso
            Mayor=float(Registro_Aceleraciones[0])
        except:#En caso de que se presente un error, probablemente debido a que la lista original ya esta vacia
            break #Se termina la funcion
    Nombres=Respaldo_Nombres#La lista original adquiere el valor de la nueva
    Estado_Coche=Respaldo_Estado_Coche#La lista original adquiere el valor de la nueva
    Registro_Temperatura=Respaldo_Registro_Temperatura
    Registro_Giros=Respaldo_Registro_Giros#La lista original adquiere el valor de la nueva
    Registro_Aceleraciones=Respaldo_Registro_Aceleraciones#La lista original adquiere el valor de la nueva
#-----------------Funcion para ordenar los puntajes respecto a las temperaturas-------------#
def ordenar_por_temperatura():
    global Nombres,Estado_Coche,Registro_Temperatura,Registro_Giros,Registro_Aceleraciones#Se importan las variables globales
    Mayor=float(Registro_Temperatura[0])#Variable parametro de comparacion inicial
    Respaldo_Nombres=[]#Se crea nueva lista para almacenar los datos extraidos de la original
    Respaldo_Estado_Coche=[]#Se crea nueva lista para almacenar los datos extraidos de la original
    Respaldo_Registro_Temperatura=[]#Se crea nueva lista para almacenar los datos extraidos de la original
    Respaldo_Registro_Giros=[]#Se crea nueva lista para almacenar los datos extraidos de la original
    Respaldo_Registro_Aceleraciones=[]#Se crea nueva lista para almacenar los datos extraidos de la original
    Cuenta=len(Registro_Temperatura)#Se establece la cardinalidad de una de las listas iniciales(Deben coincidir)
    while len(Respaldo_Registro_Temperatura)!=Cuenta:#Mientras la nueva lista no alcance la cardinalidad inicial de la lista original
        for i in Registro_Temperatura:#La variable i toma cada uno de los valores de una lista
            i=float(i)#Se asegura que todos los datos a comparar sean del mismo tipo
            if i>Mayor:#Si el dato Actual es mayor al preupuesto,este pasa a ser el mayor
                Mayor=i
        Indice=Registro_Temperatura.index(Mayor)#Se busca el indice del dato que se determino como mayor
        Respaldo_Nombres+=[Nombres[Indice]]#Se agrega dicho elemento a la lista nueva
        Nombres.pop(Indice)#Se elimina el elemento de la lista anterior
        Respaldo_Estado_Coche+=[Estado_Coche[Indice]]#Se agrega dicho elemento a la lista nueva
        Estado_Coche.pop(Indice)#Se elimina el elemento de la lista anterior
        Respaldo_Registro_Temperatura+=[Registro_Temperatura[Indice]]
        Registro_Temperatura.pop(Indice)#Se elimina el elemento de la lista anterior
        Respaldo_Registro_Giros+=[Registro_Giros[Indice]]#Se agrega dicho elemento a la lista nueva
        Registro_Giros.pop(Indice)#Se elimina el elemento de la lista anterior
        Respaldo_Registro_Aceleraciones+=[Registro_Aceleraciones[Indice]]
        Registro_Aceleraciones.pop(Indice)#Se elimina el elemento de la lista anterior
        try:#Intenta obtener un nuevo punto de inicio
            Mayor=float(Registro_Temperatura[0])
        except:#En casode que no lo logre,se termina la ejecucion 
            break 
    Nombres=Respaldo_Nombres#La variable original se le asigna el valor de la antigua
    Estado_Coche=Respaldo_Estado_Coche#La variable original se le asigna el valor de la antigua
    Registro_Temperatura=Respaldo_Registro_Temperatura#La variable original se le asigna el valor de la antigua
    Registro_Giros=Respaldo_Registro_Giros#La variable original se le asigna el valor de la antigua
    Registro_Aceleraciones=Respaldo_Registro_Aceleraciones#La variable original se le asigna el valor de la antigua
#-----------------Funcion para ordenar los puntajes respecto a los tiempo de giro-------------#
def ordenar_por_giro():
    global Nombres,Estado_Coche,Registro_Temperatura,Registro_Giros,Registro_Aceleraciones#Se imporan las variables globales correspondientes 
    Mayor=float(Registro_Giros[0])#Se asume el primer elemento como el mayor
    Respaldo_Nombres=[]#Se crea nueva lista para almacenar los datos de la original
    Respaldo_Estado_Coche=[]#Se crea nueva lista para almacenar los datos de la original
    Respaldo_Registro_Temperatura=[]#Se crea nueva lista para almacenar los datos de la original
    Respaldo_Registro_Giros=[]#Se crea nueva lista para almacenar los datos de la original
    Respaldo_Registro_Aceleraciones=[]#Se crea nueva lista para almacenar los datos de la original
    Cuenta=len(Registro_Temperatura)#Se determina la cardianidad de alguna de las listas
    while len(Respaldo_Registro_Giros)!=Cuenta:#Mientas las listas no tengan la misma cardinalidad de la lista original antes de ser modificada
        for i in Registro_Giros:#La variable toma progresivamente los valores de los diferentes elementos de la lista
            i=float(i)#Se asegura de que el elemento sea un float
            if i>Mayor:#Si es mayor al mayor anterior,este lo sustituye
                Mayor=i
        Indice=Registro_Giros.index(Mayor)#Se obtiene la posicion del dato determinado como mayor en ese momento
        Respaldo_Nombres+=[Nombres[Indice]]#Se agrega el elemento a la nueva lista
        Nombres.pop(Indice)#Se elimina el elemento de la lista original
        Respaldo_Estado_Coche+=[Estado_Coche[Indice]]
        Estado_Coche.pop(Indice)#Se elimina el elemento de la lista original
        Respaldo_Registro_Temperatura+=[Registro_Temperatura[Indice]]#Se agrega el elemento a la nueva lista
        Registro_Temperatura.pop(Indice)#Se elimina el elemento de la lista original
        Respaldo_Registro_Giros+=[Registro_Giros[Indice]]#Se agrega el elemento a la nueva lista
        Registro_Giros.pop(Indice)#Se elimina el elemento de la lista original
        Respaldo_Registro_Aceleraciones+=[Registro_Aceleraciones[Indice]]#Se agrega el elemento a la nueva lista
        Registro_Aceleraciones.pop(Indice)#Se elimina el elemento de la lista original
        try:#Intenta adquirir un nuevo valor inicial
            Mayor=float(Registro_Giros[0])
        except:#Si no se cumple se termina la funcion
            break 
    Nombres=Respaldo_Nombres#LA variable original adquiere el valor de la nueva
    Estado_Coche=Respaldo_Estado_Coche#LA variable original adquiere el valor de la nueva
    Registro_Temperatura=Respaldo_Registro_Temperatura#LA variable original adquiere el valor de la nueva
    Registro_Giros=Respaldo_Registro_Giros#LA variable original adquiere el valor de la nueva
    Registro_Aceleraciones=Respaldo_Registro_Aceleraciones#LA variable original adquiere el valor de la nueva
#__________________Funcion para actualizar los archivos en al salir________________#
def actualizar_archivos():
    global Nombres,Estado_Coche,Registro_Temperatura,Registro_Giros,Registro_Aceleraciones#Se importan las variables globales necesarias durante la ejecucion
    os.remove("Nombres.txt")#Se eliminan los archivos anteriores
    os.remove("Estado.txt")#Se eliminan los archivos anteriores
    os.remove("Temperaturas.txt")#Se eliminan los archivos anteriores
    os.remove("Tiempo de Giro.txt")#Se eliminan los archivos anteriores
    os.remove("Aceleraciones.txt")#Se eliminan los archivos anteriores
    File1=open("Nombres.txt","w")#Se abre un nuevo archivo en forma de lectura
    Grabar=fin_linea(Nombres)#Se agrega el finde linea al final de cada dato en la lista
    File1.writelines(Grabar)#Se escibe dichainformacion en el archivo
    File1.close()#Se cierra el archivo
    File2=open("Estado.txt","w")#Se abre un nuevo archivo en forma de lectura
    Grabar=fin_linea(Estado_Coche)#Se agrega el finde linea al final de cada dato en la lista
    File2.writelines(Grabar)#Se escibe dichainformacion en el archivo
    File2.close()#Se cierra el archivo
    File3=open("Temperaturas.txt","w")#Se abre un nuevo archivo en forma de lectura
    Grabar=fin_linea(Registro_Temperatura)#Se agrega el finde linea al final de cada dato en la lista
    File3.writelines(Grabar)#Se escibe dichainformacion en el archivo
    File3.close()#Se cierra el archivo
    File4=open("Tiempo de Giro.txt","w")#Se abre un nuevo archivo en forma de lectura
    Grabar=fin_linea(Registro_Giros)#Se escibe dichainformacion en el archivo
    File4.writelines(Grabar)#Se escibe dichainformacion en el archivo
    File4.close()#Se cierra el archivo
    File5=open("Aceleraciones.txt","w")#Se abre un nuevo archivo en forma de lectura
    Grabar=fin_linea(Registro_Aceleraciones)
    File5.writelines(Grabar)#Se escibe dichainformacion en el archivo
    File5.close()#Se cierra el archivo

#____________Funcion para agregar el fin de linea al final de cada linea___________#
def fin_linea(Lista):
    Resultado=[]
    while(Lista!=[]):
        Resultado+=[str(Lista[0])+"\n"]
        Lista=Lista[1:]
    return Resultado    
#_________Variables a utilizar______________#
global N_piloto,Nombres,Estado_Coche,Registro_Temperatura,Registro_Giros,Registro_Aceleraciones,Pagina,PI,PF,Mensaje,ListaR,WifiState,Pitch,Roll#DE declaran las distintas variables globales
N_piloto=1#Variable para conocer el numero de piloto en pantalla en ese momento
Nombres=eliminar(File1.readlines())#Se crea una variable correspodiente a la lectura del archivo, pero eliminando los fines de linea
Estado_Coche=eliminar(File2.readlines())#Se crea una variable correspodiente a la lectura del archivo, pero eliminando los fines de linea
Registro_Temperatura=homogenizar(eliminar(File3.readlines()))#Se crea una variable correspodiente a la lectura del archivo, pero eliminando los fines de lineay todo pueda ser interpretado como un float
Registro_Giros=homogenizar(eliminar(File4.readlines()))#Se crea una variable correspodiente a la lectura del archivo, pero eliminando los fines de lineay todo pueda ser interpretado como un float
Registro_Aceleraciones=homogenizar(eliminar(File5.readlines()))#Se crea una variable correspodiente a la lectura del archivo, pero eliminando los fines de lineay todo pueda ser interpretado como un float
Pagina=1#Pagina en la que nos encontramos
PI=0#Posicion del dato inicial a desplegar
PF=9#Posicin final de los datos a desplegar
Mensaje=""#Mensaje de info
#Se procede a cerrar los archivos para evitar errores
File1.close()
File2.close()
File3.close()
File4.close()
File5.close()

#_________Funcion para importar imagenes______________#
def imagenes(archivo):
    ruta=os.path.join("imagenes",archivo)#Asigna la ruta donde esta el archivo
    imagen=PhotoImage(file=ruta)#Establece como un objeto de clase PhotoImage al archivo ubicado en la ruta establecida
    return imagen#Retorna el objeto PhotoImage
#_____________Funciones para Audio_________________#
def off():#Funcion para apagar las demas pistas
    winsound.PlaySound(None,winsound.SND_ASYNC)#Se cierra el sonifo


#           ____________________________
#__________/Ventana Principal
root=Tk()#Ventana principla
root.title('Proyecto 1')#titulo de la ventana
root.minsize(1100,600)#Dimension
root.resizable(width=NO,height=NO)# se establecen dimensiones fijas para la ventana

#           ______________________________
#__________/Se crea un lienzo para objetos
C_root=Canvas(root, width=1100,height=700, bg='white')#Se crea el canvas correspondiente a la ventana principal
C_root.place(x=0,y=0)#Se ubuca el canvas
img_portada=imagenes("portada.png")#Se crea el objeto photoimage correspondiente 
C_root.create_image(0,0,image=img_portada,anchor=NW)#Se ubica la imagen del fondo 
img_piloto=imagenes("piloto1.png")#Se importa la imagen del piloto 

L_encabezado= Label(C_root,width=15,height=1,text="Seleccion de piloto",font=('Times New Roman',15),justify=CENTER)#Se crea label para el encabezado
L_encabezado.place(x=435,y=305)#Se ubica el label

L_conductor=Label(C_root,width=130,height=117,image=img_piloto,anchor=CENTER)#Se crea el label con la imagen correspondiente
L_conductor.place(x=450,y=340)#Se ubica el label





#                    _____________________________________
#__________/Creando el cliente para NodeMCU
myCar = NodeMCU()#Se crea una objeto de la clase NodeMCU
myCar.start()#Se llama al metodo start del objeto

E_Nombre = Entry(C_root,width=18,font=('Times New Roman',19),justify=CENTER)#Entry para obtener el nombre del piloto
E_Nombre.place(x=410,y=205)#Se ubica el label


def send (mns):#Funcion que envia los mensajes del NOdemCu
    global Mensaje#Global del mensaje

    if(len(mns)>0 and mns[-1] == ";"):#"Verifica que el mensaje no sea nulo y revisa el caracter de finalizacion"
        myCar.send(mns)#Se envia el mensaje
    return Mensaje#Se retorna el mesaje 


def switch(Posicion):#Funcion para atras de la seleccionde imagenes de pilotos
    ruta="piloto"+str(Posicion)+".png"#Se obtiene la ruta del archivo
    imagen=imagenes(ruta)#Se importa la nueva imagen
    L_conductor["image"]=imagen#Se cambia el artibuto de imagen correspondiente
    L_conductor.image=imagen#Se actualiza la informacion en la ventana
    root.update()#Se actualiza la info
def SD():#Avance hacia delante
    global N_piloto#vaiable globales necesarias
    N_piloto+=1#Aumenta en una el numero de piloto
    if N_piloto>=9:#Si el pilot es mayor o igual a nueve
        N_piloto=1#El numero de pilotos vuelve a ser cero
    switch(N_piloto)
def SI():#Avance hacia atras de la seleccionde imagenes de pilotos
    global N_piloto#variable globales necesarias
    N_piloto-=1#Disminuye en uno el numero de piloto 
    if N_piloto<=0:#Si fuese menor que cero
        N_piloto=8#Numero de piloto final corresponde al numero
    switch(N_piloto)#Se llama a la funcion switch



    
def ventana_about():#funcion para la info
    ventanainfo=Toplevel()#Se crea una ventana secundaria
    ventanainfo.title("Acerca de")#Se asigna un titulo
    ventanainfo.minsize(1000,600)#Se le establecen dimensiones minimas a la vantana
    ventanainfo.resizable(height=NO,width=NO)#Se establece que el usuario no puede cambiar el tamano de la ventana
    CA=Canvas(ventanainfo,width=1000,height=600)#Se crea el canvas
    CA.pack()#Se ubica el canvas

    #Canvas_ventanaabout.create_image(0,0,image=foto,anchor=NW)#Se crea la foto del creador
    root.withdraw()#Se minimiza la ventana principal


    """
    /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    Animación
    /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    """
    f1=imagenes("1.png")# Se importan las imagenes correspondientes
    f2=imagenes("2.png")# Se importan las imagenes correspondientes
    f3=imagenes("3.png")# Se importan las imagenes correspondientes
    imagecar=imagenes("Car.png")# Se importan las imagenes correspondientes
    FondoB=CA.create_image(12000,300,image=f2)#Se crea la imagen de fondo
    FondoA=CA.create_image(4000,300,image=f1)#Se crea la imagen de fondo
    FondoC=CA.create_image(20000,300,image=f3)#Se crea la imagen de fondo
    car=CA.create_image(100,550,image=imagecar)#Se crea la imagen de fondo
    def moverFondo():#Funcion para correr el fondo
        def Nocturno():#Cancion del fondo
            winsound.PlaySound("Nocturne.wav", winsound.SND_ASYNC)
        Nocturno()#Se llama a la cancion
        flag=True#Variable de espera y repeticion
        contador=0#Reloj para eventos
        while flag==True:#Ciclo de movimiento
            CA.move(FondoA,-4,0)#se mmueve el fondo a
            CA.move(FondoB,-4,0)#Se mueve el fondo b
            CA.move(FondoC,-4,0)#Se mueve el fondo c
            contador+=1#Se aumenta el contador de eventos
            if contador>=730 and contador <850:#Condiciones del contador
                CA.move(car,0,-1)#Mover el auto
            if contador >=1200 and contador < 1330:#Condiciones del contador
                CA.move(car,0,1)#Mover el auto
            if contador >=1600 and contador <1720:#Condiciones del contador
                CA.move(car,0,-1)#Mover el auto
            if contador >=4000 and contador <4120:#Condiciones del contador
                CA.move(car,0,1)#Mover el auto
            if contador >=4120:#Condiciones del contador
                CA.move(car,3,0)#Mover el auto
            if contador >= 5200:#Condiciones del contador
                winsound.PlaySound(None, winsound.SND_ASYNC)#Condiciones del contador
                return salir()
                
                                
            else:#Si no es, continue moviendose si alterar la ruta
                continue
        

            
    
    B=Thread(target=moverFondo ,args=()) ## CREO HILO QUE EJECUTA EL MOVIMIENTO DEL ESCENARIO
    B.start()  


    textoE="""
        Instituto Tecnologico de Costa Rica
        Area Academica de ingenieria en computadores
        Tercer Proyecto taller de programacion
        Version de python:3.7.2
        Nombre del programa: Telemetria
        Version del programa: 1.0.1
        Autores del programa:Luis Andrey Zuniga Hernandez
                             Adrian Gonzalez Jimenez
        Descripcion del programa:El programa se trata de una interfaz para el control de un auto a control remoto desarrollado en Arduino
        Entradas:El programa recibe entradas desde el teclado para realizar diferentes acciones. W para avanzar ,
        S para retroceder, a para direccionales izquierda, d para direccionales derechas,
        i para infinito,N para orientarse hacia el norte 
        Salidas:Presenta salidas de imagen
        Restricciones: Requiere la posibilidad de leer y escribir archivos con nombres especificos


        """


    """
    /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    Animación
    /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    """
        
    def salir():#Funcion para volver al menu principal
        CA.create_text(0,0,text=textoE,font=("Arial",20),fill="white", anchor=NW)
        time.sleep(10)
        ventanainfo.destroy()#Se elimina la ventana secundaria
        off()#Se apaga la tonada
        #ventana_about()
        root.deiconify()#Se maximiza la ventana pricipal
    def ventana_about():
        ventanainfo=Toplevel()#Se crea una ventana secundaria
        ventanainfo.title("About")#Se asigna un titulo
        ventanainfo.minsize(1300,622)#Se le establecen dimensiones minimas a la vantana
        ventanainfo.resizable(height=NO,width=NO)#Se establece que el usuario no puede cambiar el tamano de la ventana
        Canvas_ventanaabout=Canvas(ventanainfo,width=1300,height=622,bg="Blue")#Se crea el canvas
        Canvas_ventanaabout.place(x=0,y=0)#Se ubica el canvas
        Canvas_ventanaabout.create_text(20,30,text=textoE,font=("Arial",20),fill="white", anchor=NW)#Se crea el texto del about en espanol

    ventanainfo.mainloop()


    
def fase_juegos():#Funcion para la fase de pruebas
    """
        Instituto Tecnologico de Costa Rica
        Area Academica de ingenieria en computadores
        Tercer Proyecto taller de programacion
        Version de python:3.7.2
        Nombre del programa: Telemetria
        Version del programa: 1.0.1
        Autores del programa:Luis Andrey Zuniga Hernandez
                             Adrian Gonzalez Jimenez
        Descripcion del programa:El programa se trata de una interfaz para el control de un auto a control remoto desarrollado en Arduino
        Entradas:El programa recibe entradas desde el teclado para realizar diferentes acciones. W para avanzar , S para retroceder, a para direccionales izquierda, d para direccionales derechas,i para infinito,N para orientarse hacia el norte 
        Salidas:Presenta salidas de imagen
        Restricciones: Requiere la posibilidad de leer y escribir archivos con nombres especificos


        """
    global y,N_piloto,ListaR,EnPrueba,Nombres,Estado_Coche,Registro_Temperatura,Registro_Giros,Registro_Aceleraciones#Variables globales requeiridas en el proceso
    T1=time.time()
    y=0#Variable para indicar la posicion vertical del mouse
    EnPrueba=True#Si se esta realizando las prubas
    Nuevo_Nombre=E_Nombre.get()# se obtiene el nombre ingresado en el
    if Nuevo_Nombre=="":#Si el nombre es vacio se escoge un nombre generico
        Nombres+=["Mate"]
    else:
        Nombres+=[Nuevo_Nombre]
    Registro_Temperatura+=[0]#Se agregan datos iniciales a las listas
    Estado_Coche+=["OK"]#Se agregan datos iniciales a las listas
    Registro_Giros+=[0]#Se agregan datos iniciales a las listas
    Registro_Aceleraciones+=[0]#Se agregan datos iniciales a las listas
    velocidad="0"#Se agregan datos iniciales a las listas
    Ventana_Juego=Toplevel()#Se crea una ventana secundaria para el juego
    Ventana_Juego.title("Telemetry")#Se crea el titulo de la ventana
    Ventana_Juego.minsize(1200,650)#Se le asigna dimensiones minimas a la ventana
    Ventana_Juego.resizable(width=NO,height=NO)#Se restringen las dimensiones

    root.withdraw()#Se minimiza la ventana principal
    
    C_ventanaJuego=Canvas(Ventana_Juego,width=1300,height=650,bg="Blue")#Se crea el Canvas cubriendo la ventana
    C_ventanaJuego.create_image(0,0,anchor=NW,image=img_faseP)#Se crea una imagen correspondiente al fondo
    C_ventanaJuego.place(x=0,y=0)#Se ubica el canvas
    
    imagen_piloto=imagenes("piloto"+str(N_piloto+8)+".png")#Se ubica la imagen del piloto
    C_ventanaJuego.create_image(450,490,image=imagen_piloto,anchor=NW)#Se crea la imagen del piloto
    nombre_Text=C_ventanaJuego.create_text(480,470,text=Nombres[-1],font=("Times New Roman",22),fill="Green",anchor=NW)
    
    #______________________________________________Se crean los textos para los ubicar en pantalla__________________________________________________#
    
    Conexion_Text=C_ventanaJuego.create_text(470,20,text="m1",font=("Times New Roman",22),fill="Green",anchor=NW)
    
    Temp_Text=C_ventanaJuego.create_text(905,142,text="100",font=("Times New Roman",22),fill="Green",anchor=CENTER)
    
    Giro_Text=C_ventanaJuego.create_text(1070,127,text="",font=("Times New Roman",22),fill="Green",anchor=NW)
    
    Estado_Text=C_ventanaJuego.create_text(1090,580,text="",font=("Times New Roman",22),fill="Green",anchor=NW)
    
    Accel_Text=C_ventanaJuego.create_text(1090,335,text="",font=("Times New Roman",22),fill="Green",anchor=NW)
    
    Wifi_Text=C_ventanaJuego.create_text(900,580,text="",font=("Times New Roman",22),fill="Green",anchor=NW)
    
    Pitch_Text=C_ventanaJuego.create_text(730,20,text="",font=("Times New Roman",22),fill="Green",anchor=NW)
    
    Roll_Text=C_ventanaJuego.create_text(880,20,text="",font=("Times New Roman",22),fill="Green",anchor=NW)

    Actual_Text=C_ventanaJuego.create_text(245,360,text="100",font=("Times New Roman",22),fill="Green",anchor=CENTER)

    Inclinacion_Text=C_ventanaJuego.create_text(730,127,text="100",font=("Times New Roman",22),fill="Green",anchor=NW)


    Orientacion_Text=C_ventanaJuego.create_text(345,127,text="100",font=("Times New Roman",22),fill="Green",anchor=NW)

    Luz_Text=C_ventanaJuego.create_text(575,142,text="100",font=("Times New Roman",22),fill="Green",anchor=CENTER)

    
    ListaR=[Accel_Text,Temp_Text,Giro_Text,Estado_Text,Wifi_Text,Pitch_Text,Roll_Text,Actual_Text,Luz_Text,Inclinacion_Text,Orientacion_Text,Luz_Text]#Variable global para el contro de las diferentes etiqutas
    
    LuzAm=imagenes("b.png")#Imagen luz amarilla
    LuzRo=imagenes("c.png")#Imagen luz roja
    LuzAz=imagenes("a.png")#Imagen luz azul
    
    Power1=imagenes("P1.png")
    Power2=imagenes("P2.png")
    Power3=imagenes("P3.png")
    WarningSeñal= imagenes("warning.png")
    
    global luz#Variable global para el control de las diferentes luces de auto virtual
    luz=[ C_ventanaJuego.create_image(40,450,image=LuzAz)
               , C_ventanaJuego.create_image(165,450,image=LuzAz)
               , C_ventanaJuego.create_image(40,640,image=LuzAz)
               , C_ventanaJuego.create_image(165,640,image=LuzAz)
               ,C_ventanaJuego.create_image(1115,450,image=Power3)]

    """
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    
    """
    def warning():#Funcion para determinar si ha habido un error de time out
        global ListaR
        C_ventanaJuego.delete(ListaR[4])#Se borra el la etiqueta preexistente
        señal= C_ventanaJuego.create_image(920,600,image=WarningSeñal)#Se crea una nueva etiqueta
        ListaR[4]=señal#Se agrega a la lista de control
    def get_log():#Funcion que solicita continuamente los mensajes
        global Mensaje,EnPrueba#Variables globales necesarias
        while(myCar.loop)and EnPrueba:#Si esta ejecutandose la etapa y es posible la comunicacion
            if myCar.log!=[]:
                #print(myCar.log[-1][-1])
                Mensaje = myCar.log[-1][-1]#Guarda el mensaje obtenido en una variable global
                if myCar.log[-1][-1]=="timed out":

                    warning()
                myCar.log=[]


                
    p= Thread(target=get_log)
    p.start()        
    def luces(evento):#Funcion para cambiar las imagenes de las luces del auto
        global luz,ListaR
        if evento =="dirIzquierda":#Si es direccional izquierda
            C_ventanaJuego.delete(luz[2])
            luz[2]=C_ventanaJuego.create_image(40,640,image=LuzRo)
            C_ventanaJuego.delete(ListaR[7])#Cambia la imagen por la direccional
            Actual_Text=C_ventanaJuego.create_text(245,360,text="DI",font=("Times New Roman",22),fill="Green",anchor=CENTER)#Actualiza el texto de ejecucion actual
            ListaR[7]=Actual_Text
            C_ventanaJuego.update()
            time.sleep(0.9)#Espera un tiempo
            C_ventanaJuego.delete(ListaR[7])#Borra el texto anterior
            Actual_Text=C_ventanaJuego.create_text(245,360,text="",font=("Times New Roman",22),fill="Green",anchor=CENTER)#Crae un texto vacio
            ListaR[7]=Actual_Text#Guarda el valor en la lista de referencia
            C_ventanaJuego.delete(luz[2])#Elimina la imagen de ese momento(Encendida)
            luz[2]=C_ventanaJuego.create_image(40,640,image=LuzAz)#Cambia la imagen por la apagada
            C_ventanaJuego.update()
        if evento =="dirDerecha":#En caso de ser derecha
            C_ventanaJuego.delete(luz[3])
            luz[3]=C_ventanaJuego.create_image(165,640,image=LuzRo)
            C_ventanaJuego.delete(ListaR[7])#Cambia la imagen direccional
            Actual_Text=C_ventanaJuego.create_text(245,360,text="DR",font=("Times New Roman",22),fill="Green",anchor=CENTER)#Actualiza el texto
            ListaR[7]=Actual_Text#Guarda la info en la lista de referencia
            C_ventanaJuego.update()#Actualiza el contenido del canvas
            time.sleep(0.9)#Espera un tiempo
            C_ventanaJuego.delete(ListaR[7])#Elimina el texto
            Actual_Text=C_ventanaJuego.create_text(245,360,text="",font=("Times New Roman",22),fill="Green",anchor=CENTER)#Actualiza el texto a uno vacio
            ListaR[7]=Actual_Text#Se guarda el objeto en la lista de referencia
            C_ventanaJuego.delete(luz[3])
            luz[3]=C_ventanaJuego.create_image(165,640,image=LuzAz)#Se crea la imagen de luz apagada
            C_ventanaJuego.update()
        if evento =="delanterasOn":#En el caso de que sean luces delanteras
            C_ventanaJuego.delete(luz[0])#Elimina las luces delateras del momento
            C_ventanaJuego.delete(luz[1])#Elimina las luces delateras del momento
            C_ventanaJuego.delete(ListaR[7])#Elimina el texto del momento
            Actual_Text=C_ventanaJuego.create_text(245,360,text="LD",font=("Times New Roman",22),fill="Green",anchor=CENTER)#Crea un nuevo texto
            ListaR[7]=Actual_Text#Agrega el texto  la lista de referencia
            C_ventanaJuego.update()#Actualiza el contenido del canvas
            luz[0]=C_ventanaJuego.create_image(40,450,image=LuzAm)#Crea la imagen de luz encendida
            luz[1]=C_ventanaJuego.create_image(165,450,image=LuzAm)#Crea la imagen de luz encendida        
            C_ventanaJuego.update()
        if evento =="delanterasOff":#En caso de tener que apagar 
            C_ventanaJuego.delete(luz[0])#Elimina las luces delateras del momento
            C_ventanaJuego.delete(luz[1])#Elimina las luces delateras del momento
            C_ventanaJuego.delete(ListaR[7])#Elimina el texto del momento
            Actual_Text=C_ventanaJuego.create_text(245,360,text="",font=("Times New Roman",22),fill="Green",anchor=CENTER)#Crea un nuevo texto
            ListaR[7]=Actual_Text#Agrega el texto  la lista de referencia
            C_ventanaJuego.update() #Actualiza el contenido del canvas        
            luz[0]=C_ventanaJuego.create_image(40,450,image=LuzAz)#Crea la imagen de luz apagada
            luz[1]=C_ventanaJuego.create_image(165,450,image=LuzAz)#Crea la imagen de luz apagada
            C_ventanaJuego.update()
        if evento=="traserasOn":
            C_ventanaJuego.delete(luz[2])
            C_ventanaJuego.delete(luz[3])
            C_ventanaJuego.delete(ListaR[7])
            Actual_Text=C_ventanaJuego.create_text(245,360,text="LT",font=("Times New Roman",22),fill="Green",anchor=CENTER)
            ListaR[7]=Actual_Text
            C_ventanaJuego.update()            
            luz[3]=C_ventanaJuego.create_image(165,640,image=LuzRo)            
            luz[2]=C_ventanaJuego.create_image(40,640,image=LuzRo)
            C_ventanaJuego.update()
        if evento=="traserasOff":
            C_ventanaJuego.delete(luz[2])
            C_ventanaJuego.delete(luz[3])
            C_ventanaJuego.delete(ListaR[7])
            Actual_Text=C_ventanaJuego.create_text(245,360,text="",font=("Times New Roman",22),fill="Green",anchor=CENTER)
            ListaR[7]=Actual_Text
            C_ventanaJuego.update()            
            luz[3]=C_ventanaJuego.create_image(165,640,image=LuzAz)            
            luz[2]=C_ventanaJuego.create_image(40,640,image=LuzAz)
            C_ventanaJuego.update()

    def giro_derecha(event):  
        print("derecha")
        send("dir:1;")
        #send("lr:1;")
        return luces("dirDerecha")  
    def giro_izquierda(event):
        print("izquierda")
        send("dir:-1;")
        #send("ll:1;")
        return luces("dirIzquierda")        
    def avanzar(event):
        global ListaR
        if y < 200:
            velocidad= "pwm:1000;"
            send(velocidad)
        if y < 400 and y>200:
            velocidad = "pwm:800;"
            send(velocidad)
        if y < 600 and y >400:
            velocidad =  "pwm:300;"
            send(velocidad)
        print("avanzar a: " +velocidad[4:])
        luces("traserasOff")
        C_ventanaJuego.delete(ListaR[7])
        Actual_Text=C_ventanaJuego.create_text(245,360,text="Avanzar",font=("Times New Roman",22),fill="Green",anchor=CENTER)
        ListaR[7]=Actual_Text
        C_ventanaJuego.update()


    def retroceder(event):

        if y < 200:
            velocidad= "pwm:-1000;"
        if y < 400 and y>200:
            velocidad = "pwm:-800;"
        if y < 600 and y >200:
            velocidad =  "pwm:-500;"
        print("retroceder a :" +velocidad[4:])
        send(velocidad)
        luces("traserasOn")
        C_ventanaJuego.delete(ListaR[7])
        Actual_Text=C_ventanaJuego.create_text(245,360,text="Retroceder",font=("Times New Roman",22),fill="Green",anchor=CENTER)
        ListaR[7]=Actual_Text
        C_ventanaJuego.update()
    
    def EncenderLuces(evento):
        send("lf:1;")
        return luces("delanterasOn")
    
    def ApagarLuces(evento):
        send("lf:0;")
        return luces("delanterasOff")
    def EncenderLucesA(evento):
        send("lb:1;")
        return luces("traserasOn")
    def CircDerecha(evento):
        send("TurnTime:1;")

    def CircIzquierda(evento):
        send("TurnTime:-1;")


    
    def ApagarLuces(evento):
        send("lf:0;")
        return luces("delanterasOff")
    def EncenderLucesA(evento):
        send("lb:1;")
        return luces("traserasOn")
    
    def ApagarLucesA(evento):
        send("lb:0;")
        return luces("traserasOff")
    def infinite(event):
        send("Infinite;")
        print("Movimiento Especial: Infinito")
    def Especial(event):
        send("Especial;")
        print("Movimiento Especial: Sen")
    def pitar(event):
        print("pitar")
        send("pitar;")
    
    def musica(event):
        print("musica")
        send("song;")
        
    def motion(event):
        global y
        y = event.y
        if y < 200:
            C_ventanaJuego.delete(luz[4])
            luz[4]=C_ventanaJuego.create_image(1115,450,image=Power3)
            C_ventanaJuego.update()
            time.sleep(0.1)
        if y < 400 and y>200:
            C_ventanaJuego.delete(luz[4])
            luz[4]=C_ventanaJuego.create_image(1115,450,image=Power2)
            C_ventanaJuego.update()
            time.sleep(0.1)
        if y < 650 and y >400:
            C_ventanaJuego.delete(luz[4])
            luz[4]=C_ventanaJuego.create_image(1115,450,image=Power1)
            C_ventanaJuego.update()
            time.sleep(0.1)
            
    def space(Evento):
        print("Detener avance")
        return send("pwm:0;")
    
    def norte(evento):
        print("Orientando hacia el norte")
        return send("North;")
    def reporte_aceleracion():
        global ListaR,Registro_Aceleraciones
        Entrada=send("saved;")
        try:
            Aceleracion=Entrada[:Entrada.index("$")]
        except:
            Aceleracion="E"
        if len(Aceleracion)>5:
            Aceleracion="E"
        Estado="OK"
        if  Aceleracion!= "E" :
            if float(Aceleracion)>float(Registro_Aceleraciones[-1]) :
                Registro_Aceleraciones[-1]=float(Aceleracion)
        Estado_Coche[-1]=Estado
        C_ventanaJuego.delete(ListaR[3])
        Estado_Text=C_ventanaJuego.create_text(1090,580,text=Estado,font=("Times New Roman",22),fill="Green",anchor=NW)
        ListaR[3]=Estado_Text
        C_ventanaJuego.delete(ListaR[0])
        Accel_Text=C_ventanaJuego.create_text(1090,335,text=Aceleracion,font=("Times New Roman",22),fill="Green",anchor=NW)
        ListaR[0]=Accel_Text
        C_ventanaJuego.update()
    def reporte_estado():
        global ListaR,Estado_Coche
        Estado=send("saved;")
        if "$" not in Estado:
            Estado="X"
        Estado_Coche[-1]=Estado
        C_ventanaJuego.delete(ListaR[3])
        Estado_Text=C_ventanaJuego.create_text(1090,580,text=Estado,font=("Times New Roman",22),fill="Green",anchor=NW)
        ListaR[3]=Estado_Text
        C_ventanaJuego.update()
    def reporte_temperatura():
        global ListaR,Registro_Temperatura
        Entrada=send("saved;")
        if "$" in Entrada:
            Temperatura=Entrada[:Entrada.index("$")]
            Luz=Entrada[Entrada.index("$")+1:]
        else:
            Temperatura="E"
            Luz="E"
        
        if Temperatura!="E":
            if float(Temperatura)>float(Registro_Temperatura[-1]):
                Registro_Temperatura[-1]=float(Temperatura)
        C_ventanaJuego.delete(ListaR[1])
        Temp_Text=C_ventanaJuego.create_text(905,142,text=Temperatura,font=("Times New Roman",22),fill="Green",anchor=CENTER)
        ListaR[1]=Temp_Text
        C_ventanaJuego.delete(ListaR[11])
        Luz_Text=C_ventanaJuego.create_text(575,142,text=Luz,font=("Times New Roman",22),fill="Green",anchor=CENTER)
        ListaR[11]=Luz_Text
        C_ventanaJuego.update()
    def reporte_giro():
        global ListaR,Registro_Giros
        TiempoGiro=send("saved;")
        if float(TiempoGiro)>float(Registro_Giros[-1]):
            Registro_Giros[-1]=float(TiempoGiro)
        C_ventanaJuego.delete(ListaR[2])
        Giro_Text=C_ventanaJuego.create_text(1070,127,text=TiempoGiro,font=("Times New Roman",22),fill="Green",anchor=NW)
        ListaR[2]=Giro_Text
        C_ventanaJuego.update()
    def reporte_yaw():
        global ListaR
        YAW=send("yaw;")
        if len(YAW)>5:
            YAW="E"
        C_ventanaJuego.delete(ListaR[9])
        Inclinacion_Text=C_ventanaJuego.create_text(730,127,text=YAW,font=("Times New Roman",22),fill="Green",anchor=NW)
        ListaR[9]=Inclinacion_Text
        C_ventanaJuego.update()
    def reporte_pitch():
        global ListaR
        Pitch=send("pitch")
        if len(Pitch)>5:
            Pitch="E"
        C_ventanaJuego.delete(ListaR[5])
        Pitch_Text=C_ventanaJuego.create_text(730,20,text=Pitch,font=("Times New Roman",22),fill="Green",anchor=NW)
        ListaR[5]=Pitch_Text
        C_ventanaJuego.update()
    def reporte_roll():
        global ListaR
        Roll=send("roll;")
        if len(Roll)>5:
            Roll="E"
        C_ventanaJuego.delete(ListaR[6])
        Roll_Text=C_ventanaJuego.create_text(880,20,text=Roll,font=("Times New Roman",22),fill="Green",anchor=NW)
        ListaR[6]=Roll_Text
        C_ventanaJuego.update()

    def reporte_luz():
        global ListaR
        Luz=send("sense;")
        Luz="Mil"
        C_ventanaJuego.delete(ListaR[8])
        Luz_Text=C_ventanaJuego.create_text(555,127,text=Luz,font=("Times New Roman",22),fill="Green",anchor=NW)
        ListaR[8]=Luz_Text
        C_ventanaJuego.update()

    #def reporte_luz():
       # global ListaR
        #Inclinacion=send("sense;")
        #Luz="Mil"
        #C_ventanaJuego.delete(ListaR[8])
        #Luz_Text=C_ventanaJuego.create_text(555,127,text=Luz,font=("Times New Roman",22),fill="Green",anchor=NW)
        #ListaR[8]=Luz_Text
        #C_ventanaJuego.update()
        #Inclinacion_Text,Orientacion_Text
    def salir(Evento):
        global N_piloto,EnPrueba,Nombres,Estado_Coche,Registro_Temperatura,Registro_Giros,Registro_Aceleraciones
        EnPrueba=False
        time.sleep(0.4)
        off()
        Ventana_Juego.destroy()
        actualizar_archivos()
        #Nombres=eliminar(Nombres)
        #Estado_Coche=eliminar(Estado_Coche)
        #Registro_Temperatura=eliminar(Registro_Temperatura)
        #Registro_Giros=eliminar(Registro_Giros)
        #Registro_Aceleraciones=eliminar(Registro_Aceleraciones)
        root.deiconify()
        Aceleracion="0"
        Temperatura="0"
        TiempoGiro="0"
        Estado=""
        ListaR=[]
        WifiState=""
        Pitch=""
        Roll=""
    def ciclo_actualizado():
        global EnPrueba
        reporte_aceleracion()
        reporte_pitch()
        reporte_yaw()
        #reporte_estado()
        reporte_temperatura()
        #reporte_giro()
        reporte_roll()
    
    def reloj():
        while True:
            ciclo_actualizado()
            time.sleep(5)
            
    hilo_parametros=Thread(target=reloj)
    hilo_parametros.start()
        

    C_ventanaJuego.bind_all("<w>",avanzar)
    C_ventanaJuego.bind_all("<s>",retroceder)
    
    C_ventanaJuego.bind_all("<l>",EncenderLuces)
    C_ventanaJuego.bind_all("<j>",ApagarLuces)
    
    C_ventanaJuego.bind_all("<d>",giro_derecha)
    C_ventanaJuego.bind_all("<a>",giro_izquierda)

    C_ventanaJuego.bind_all("<n>",norte)
    C_ventanaJuego.bind_all("<i>",Especial)
    C_ventanaJuego.bind_all("<b>",infinite)
    C_ventanaJuego.bind_all("<o>",CircIzquierda)
    C_ventanaJuego.bind_all("<O>",CircDerecha)
     
    C_ventanaJuego.bind_all("<k>",pitar)
    C_ventanaJuego.bind_all("<m>",musica)
    
    C_ventanaJuego.bind_all("<h>",reporte_pitch)
    C_ventanaJuego.bind_all("<Escape>",salir)
    C_ventanaJuego.bind_all("<z>",reporte_aceleracion)
    C_ventanaJuego.bind_all("<x>",reporte_temperatura)

    
    C_ventanaJuego.bind_all("<space>",space)
    Ventana_Juego.bind('<Motion>', motion) 
    


    Ventana_Juego.mainloop()


root.bind('<Return>', send) #Vinculando tecla Enter a la función send
img_flechaD=imagenes("flechaD.png")
img_flechaI=imagenes("flechaI.png")
img_info=imagenes("boton info.png")
img_fondoabout=imagenes("pilotos.png")
img_pagS=imagenes("SiguientePagina.png")
img_pagA=imagenes("AnteriorPagina.png")
img_faseP=imagenes("PortadaPruebas.png")
img_buto=imagenes("CarB.png")
img_tabla=imagenes("Fondo Tabla Autos.png")
img_pantallaazul=imagenes("pantalla.png")
img_botonazul=imagenes("botones.png")
img_botonPuntajes=imagenes("PuntajeIcon.png")



def ventana_puntaje():
    global Nombre1,Nombre2,Nombre2,Nombre3,Nombre4,Nombre5,Nombre6,Nombre7,Nombre8,Nombre9,Nombre10,Temperatura1,Temperatura2,Temperatura3,Temperatura4,Temperatura5,Temperatura6,Temperatura7,Temperatura8,Temperatura9,Temperatura10,Aceleracion1,Aceleracion2,Aceleracion3,Aceleracion4,Aceleracion5,Aceleracion6,Aceleracion7,Aceleracion8,Aceleracion9,Aceleracion10,Giro1,Giro2,Giro3,Giro4,Giro5,Giro6,Giro7,Giro8,Giro9,Giro10,Estado1,Estado2,Estado3,Estado4,Estado5,Estado6,Estado7,Estado8,Estado9,Estado10
    
    Ventana_score=Toplevel()
    Ventana_score.title("Scores")
    Ventana_score.minsize(795,640)
    Ventana_score.resizable(height=NO, width=NO)
    root.withdraw()
    C_score=Canvas(Ventana_score,height=650,width=795,bg="black")
    C_score.place(x=0,y=0)
    #C_score.create_image(0,0,image=img_pantallaazul,anchor=NW)
    C_score.create_image(0,60,image=img_tabla,anchor=NW)
    C_score.create_text(255,50,text="Temperatura",fill="white",font=("Rockwell Extra Bold",10),anchor=NW)
    C_score.create_text(380,50,text="Aceleracion",fill="white",font=("Rockwell Extra Bold",10),anchor=NW)
    C_score.create_text(500,50,text="T Giro",fill="white",font=("Rockwell Extra Bold",10),anchor=NW)
    C_score.create_text(600,50,text="Estado",fill="white",font=("Rockwell Extra Bold",10),anchor=NW)
    Nombre1=C_score.create_text(60,70,text="Pedro",font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
    Nombre2=C_score.create_text(60,120,text="Carlos",font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
    Nombre3=C_score.create_text(60,175,text="Judith",font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
    Nombre4=C_score.create_text(60,230,text="Adrian",font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
    Nombre5=C_score.create_text(60,280,text="Ignacio",font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
    Nombre6=C_score.create_text(60,335,text="Randall",font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
    Nombre7=C_score.create_text(60,385,text="Francisco",font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
    Nombre8=C_score.create_text(60,435,text="Laura",font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
    Nombre9=C_score.create_text(60,490,text="Sofia",font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
    Nombre10=C_score.create_text(60,545,text="Rose",font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
    Temperatura1=C_score.create_text(270,70,text="200",font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
    Temperatura2=C_score.create_text(270,120,text="30",font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
    Temperatura3=C_score.create_text(270,175,text="55",font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
    Temperatura4=C_score.create_text(270,230,text="33",font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
    Temperatura5=C_score.create_text(270,280,text="47",font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
    Temperatura6=C_score.create_text(270,335,text="27",font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
    Temperatura7=C_score.create_text(270,385,text="25",font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
    Temperatura8=C_score.create_text(270,435,text="40",font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
    Temperatura9=C_score.create_text(270,490,text="55",font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
    Temperatura10=C_score.create_text(270,545,text="32",font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
    Aceleracion1=C_score.create_text(380,70,text="200",font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
    Aceleracion2=C_score.create_text(380,120,text="30",font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
    Aceleracion3=C_score.create_text(380,175,text="55",font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
    Aceleracion4=C_score.create_text(380,230,text="33",font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
    Aceleracion5=C_score.create_text(380,280,text="47",font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
    Aceleracion6=C_score.create_text(380,335,text="27",font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
    Aceleracion7=C_score.create_text(380,385,text="25",font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
    Aceleracion8=C_score.create_text(380,435,text="40",font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
    Aceleracion9=C_score.create_text(380,490,text="55",font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
    Aceleracion10=C_score.create_text(380,545,text="32",font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
    Giro1=C_score.create_text(490,70,text="200",font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
    Giro2=C_score.create_text(490,120,text="30",font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
    Giro3=C_score.create_text(490,175,text="55",font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
    Giro4=C_score.create_text(490,230,text="33",font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
    Giro5=C_score.create_text(490,280,text="47",font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
    Giro6=C_score.create_text(490,335,text="27",font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
    Giro7=C_score.create_text(490,385,text="25",font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
    Giro8=C_score.create_text(490,435,text="40",font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
    Giro9=C_score.create_text(490,490,text="55",font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
    Giro10=C_score.create_text(490,545,text="32",font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
    Estado1=C_score.create_text(600,70,text="OK",font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
    Estado2=C_score.create_text(600,120,text="OK",font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
    Estado3=C_score.create_text(600,175,text="OK",font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
    Estado4=C_score.create_text(600,230,text="OK",font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
    Estado5=C_score.create_text(600,280,text="OK",font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
    Estado6=C_score.create_text(600,335,text="OK",font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
    Estado7=C_score.create_text(600,385,text="OK",font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
    Estado8=C_score.create_text(600,435,text="OK",font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
    Estado9=C_score.create_text(600,490,text="OK",font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
    Estado10=C_score.create_text(600,545,text="OK",font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
    def actualizar_texto(A,B,C,D,E):
        global Nombre1,Nombre2,Nombre2,Nombre3,Nombre4,Nombre5,Nombre6,Nombre7,Nombre8,Nombre9,Nombre10,Temperatura1,Temperatura2,Temperatura3,Temperatura4,Temperatura5,Temperatura6,Temperatura7,Temperatura8,Temperatura9,Temperatura10,Aceleracion1,Aceleracion2,Aceleracion3,Aceleracion4,Aceleracion5,Aceleracion6,Aceleracion7,Aceleracion8,Aceleracion9,Aceleracion10,Giro1,Giro2,Giro3,Giro4,Giro5,Giro6,Giro7,Giro8,Giro9,Giro10,Estado1,Estado2,Estado3,Estado4,Estado5,Estado6,Estado7,Estado8,Estado9,Estado10
        C_score.delete(Nombre1)
        C_score.delete(Nombre2)
        C_score.delete(Nombre3)
        C_score.delete(Nombre4)
        C_score.delete(Nombre5)
        C_score.delete(Nombre6)
        C_score.delete(Nombre7)
        C_score.delete(Nombre8)
        C_score.delete(Nombre9)
        C_score.delete(Nombre10)
        C_score.delete(Temperatura1)
        C_score.delete(Temperatura2)
        C_score.delete(Temperatura3)
        C_score.delete(Temperatura4)
        C_score.delete(Temperatura5)
        C_score.delete(Temperatura6)
        C_score.delete(Temperatura7)
        C_score.delete(Temperatura8)
        C_score.delete(Temperatura9)
        C_score.delete(Temperatura10)
        C_score.delete(Aceleracion1)
        C_score.delete(Aceleracion2)
        C_score.delete(Aceleracion3)
        C_score.delete(Aceleracion4)
        C_score.delete(Aceleracion5)
        C_score.delete(Aceleracion6)
        C_score.delete(Aceleracion7)
        C_score.delete(Aceleracion8)
        C_score.delete(Aceleracion9)
        C_score.delete(Aceleracion10)
        C_score.delete(Giro1)
        C_score.delete(Giro2)
        C_score.delete(Giro3)
        C_score.delete(Giro4)
        C_score.delete(Giro5)
        C_score.delete(Giro6)
        C_score.delete(Giro7)
        C_score.delete(Giro8)
        C_score.delete(Giro9)
        C_score.delete(Giro10)
        C_score.delete(Estado1)
        C_score.delete(Estado2)
        C_score.delete(Estado3)
        C_score.delete(Estado4)
        C_score.delete(Estado5)
        C_score.delete(Estado6)
        C_score.delete(Estado7)
        C_score.delete(Estado8)
        C_score.delete(Estado9)
        C_score.delete(Estado10)
        #________________________________________________________________________________________________#
        Nombre1=C_score.create_text(60,70,text=A[0],font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
        Nombre2=C_score.create_text(60,120,text=A[1],font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
        Nombre3=C_score.create_text(60,175,text=A[2],font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
        Nombre4=C_score.create_text(60,230,text=A[3],font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
        Nombre5=C_score.create_text(60,280,text=A[4],font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
        Nombre6=C_score.create_text(60,335,text=A[5],font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
        Nombre7=C_score.create_text(60,385,text=A[6],font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
        Nombre8=C_score.create_text(60,435,text=A[7],font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
        Nombre9=C_score.create_text(60,490,text=A[8],font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
        Nombre10=C_score.create_text(60,545,text=A[9],font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
        Temperatura1=C_score.create_text(270,70,text=B[0],font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
        Temperatura2=C_score.create_text(270,120,text=B[1],font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
        Temperatura3=C_score.create_text(270,175,text=B[2],font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
        Temperatura4=C_score.create_text(270,230,text=B[3],font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
        Temperatura5=C_score.create_text(270,280,text=B[4],font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
        Temperatura6=C_score.create_text(270,335,text=B[5],font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
        Temperatura7=C_score.create_text(270,385,text=B[6],font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
        Temperatura8=C_score.create_text(270,435,text=B[7],font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
        Temperatura9=C_score.create_text(270,490,text=B[8],font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
        Temperatura10=C_score.create_text(270,545,text=B[9],font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
        Aceleracion1=C_score.create_text(380,70,text=C[0],font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
        Aceleracion2=C_score.create_text(380,120,text=C[1],font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
        Aceleracion3=C_score.create_text(380,175,text=C[2],font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
        Aceleracion4=C_score.create_text(380,230,text=C[3],font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
        Aceleracion5=C_score.create_text(380,280,text=C[4],font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
        Aceleracion6=C_score.create_text(380,335,text=C[5],font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
        Aceleracion7=C_score.create_text(380,385,text=C[6],font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
        Aceleracion8=C_score.create_text(380,435,text=C[7],font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
        Aceleracion9=C_score.create_text(380,490,text=C[8],font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
        Aceleracion10=C_score.create_text(380,545,text=C[9],font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
        Giro1=C_score.create_text(490,70,text=D[0],font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
        Giro2=C_score.create_text(490,120,text=D[1],font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
        Giro3=C_score.create_text(490,175,text=D[2],font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
        Giro4=C_score.create_text(490,230,text=D[3],font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
        Giro5=C_score.create_text(490,280,text=D[4],font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
        Giro6=C_score.create_text(490,335,text=D[5],font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
        Giro7=C_score.create_text(490,385,text=D[6],font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
        Giro8=C_score.create_text(490,435,text=D[7],font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
        Giro9=C_score.create_text(490,490,text=D[8],font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
        Giro10=C_score.create_text(490,545,text=D[9],font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
        Estado1=C_score.create_text(600,70,text=E[0],font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
        Estado2=C_score.create_text(600,120,text=E[1],font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
        Estado3=C_score.create_text(600,175,text=E[2],font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
        Estado4=C_score.create_text(600,230,text=E[3],font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
        Estado5=C_score.create_text(600,280,text=E[4],font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
        Estado6=C_score.create_text(600,335,text=E[5],font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
        Estado7=C_score.create_text(600,385,text=E[6],font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
        Estado8=C_score.create_text(600,435,text=E[7],font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
        Estado9=C_score.create_text(600,490,text=E[8],font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
        Estado10=C_score.create_text(600,545,text=E[9],font=("Rockwell Extra Bold",24),fill="white",anchor=NW)
    def completar(Lista):
        Resultado=copy(Lista)
        while len(Resultado)%10!=0:
            Resultado+=[""]
        return Resultado
    def accel_sort():
        global Nombres,Estado_Coche,Registro_Temperatura,Registro_Giros,Registro_Aceleraciones,PI,PF,Pagina
        PI=0
        PF=10
        Pagina=1
        ordenar_por_aceleracion()
        Respaldo_Nombres=completar(Nombres)[PI:PF]
        Respaldo_Estado_Coche=completar(Estado_Coche)[PI:PF]
        Respaldo_Registro_Temperatura=completar(Registro_Temperatura)[PI:PF]
        Respaldo_Registro_Giros=completar(Registro_Giros)[PI:PF]
        Respaldo_Registro_Aceleraciones=completar(Registro_Aceleraciones)[PI:PF]
        actualizar_texto(Respaldo_Nombres,Respaldo_Registro_Temperatura,Respaldo_Registro_Aceleraciones,Respaldo_Registro_Giros,Respaldo_Estado_Coche)
        #L_titulo_tabla["text"]="Historial de Resultados Pagina ("+str(Pagina)+")"
        
    def temp_sort():
        global Nombres,Estado_Coche,Registro_Temperatura,Registro_Giros,Registro_Aceleraciones,PI,PF,Pagina
        PI=0
        PF=10
        Pagina=1
        ordenar_por_temperatura()
        Respaldo_Nombres=completar(Nombres)[PI:PF]
        Respaldo_Estado_Coche=completar(Estado_Coche)[PI:PF]
        Respaldo_Registro_Temperatura=completar(Registro_Temperatura)[PI:PF]
        Respaldo_Registro_Giros=completar(Registro_Giros)[PI:PF]
        Respaldo_Registro_Aceleraciones=completar(Registro_Aceleraciones)[PI:PF]
        actualizar_texto(Respaldo_Nombres,Respaldo_Registro_Temperatura,Respaldo_Registro_Aceleraciones,Respaldo_Registro_Giros,Respaldo_Estado_Coche)
        #L_titulo_tabla["text"]="Historial de Resultados Pagina ("+str(Pagina)+")"
    def giro_sort():
        global Nombres,Estado_Coche,Registro_Temperatura,Registro_Giros,Registro_Aceleraciones,PI,PF,Pagina
        PI=0
        PF=10
        Pagina=1
        ordenar_por_giro()
        Respaldo_Nombres=completar(Nombres)[PI:PF]
        Respaldo_Estado_Coche=completar(Estado_Coche)[PI:PF]
        Respaldo_Registro_Temperatura=completar(Registro_Temperatura)[PI:PF]
        Respaldo_Registro_Giros=completar(Registro_Giros)[PI:PF]
        Respaldo_Registro_Aceleraciones=completar(Registro_Aceleraciones)[PI:PF]
        actualizar_texto(Respaldo_Nombres,Respaldo_Registro_Temperatura,Respaldo_Registro_Aceleraciones,Respaldo_Registro_Giros,Respaldo_Estado_Coche)
        #L_titulo_tabla["text"]="Historial de Resultados Pagina ("+str(Pagina)+")"
    def Tabladelante():
        global Nombres,Estado_Coche,Registro_Temperatura,Registro_Giros,Registro_Aceleraciones,PI,PF,Pagina
        if PF ==len(completar(Nombres)):
            PI=0
            PF=10
            Pagina=1
        else:
            PI+=10
            PF+=10
            Pagina+=1
        Respaldo_Nombres=completar(Nombres)[PI:PF]
        Respaldo_Estado_Coche=completar(Estado_Coche)[PI:PF]
        Respaldo_Registro_Temperatura=completar(Registro_Temperatura)[PI:PF]
        Respaldo_Registro_Giros=completar(Registro_Giros)[PI:PF]
        Respaldo_Registro_Aceleraciones=completar(Registro_Aceleraciones)[PI:PF]
        #L_titulo_tabla["text"]="Historial de Resultados Pagina ("+str(Pagina)+")"
        actualizar_texto(Respaldo_Nombres,Respaldo_Registro_Temperatura,Respaldo_Registro_Aceleraciones,Respaldo_Registro_Giros,Respaldo_Estado_Coche)
    def Tablatras():
        global Nombres,Estado_Coche,Registro_Temperatura,Registro_Giros,Registro_Aceleraciones,PI,PF,Pagina
        if PI ==0:
            PF=len(completar(Nombres))
            PI=len(completar(Nombres))-10
            Pagina=int(len(completar(Nombres))//10)
        else:
            PI-=10
            PF-=10
            Pagina-=1
                       
        Respaldo_Nombres=completar(Nombres)[PI:PF]
        Respaldo_Estado_Coche=completar(Estado_Coche)[PI:PF]
        Respaldo_Registro_Temperatura=completar(Registro_Temperatura)[PI:PF]
        Respaldo_Registro_Giros=completar(Registro_Giros)[PI:PF]
        Respaldo_Registro_Aceleraciones=completar(Registro_Aceleraciones)[PI:PF]
        actualizar_texto(Respaldo_Nombres,Respaldo_Registro_Temperatura,Respaldo_Registro_Aceleraciones,Respaldo_Registro_Giros,Respaldo_Estado_Coche)
    def salir(Evento):
        Ventana_score.destroy()
        off()
        root.deiconify()
        #L_titulo_tabla["text"]="Historial de Resultados Pagina ("+str(Pagina)+")"
    accel_sort()
    

    
    Btn_delante=Button(C_score,text="Adelante",command=Tabladelante,bg="blue",bd=10)
    Btn_delante.place(x=600,y=600)
    
    Btn_atras=Button(C_score,text="Atras",command=Tablatras,bg="blue",bd=10)
    Btn_atras.place(x=100,y=600)
    
    Btn_Accelsort=Button(C_score,text="Aceleración",command=accel_sort ,bg="blue",bd=10)
    Btn_Accelsort.place(x=200,y=600)
    
    Btn_Tempsort=Button(C_score,text="Temperatura",command=temp_sort,bg="blue",bd=10)
    Btn_Tempsort.place(x=310,y=600)
    
    Btn_Girosort=Button(C_score,text="Tiempo de giro",command=giro_sort,bg="blue" ,bd=10)
    Btn_Girosort.place(x=420,y=600)

    C_score.bind_all("<Escape>",salir)


#                    ____________________________
#__________/Botones de ventana principal
Btn_switchD=Button(C_root,image=img_flechaD,command=SD)
Btn_switchD.place(x=570,y=340)

Btn_switchI=Button(C_root,image=img_flechaI,command=SI)
Btn_switchI.place(x=397,y=340)

Btn_about=Button(C_root,image=img_info,command=ventana_about,bg="light cyan")
Btn_about.place(x=1015,y=525)

Btn_play=Button(C_root,command=fase_juegos, image= img_buto)
Btn_play.place(x=100,y=300)

Btn_ventanaJuego=Button(C_root,command=ventana_puntaje,image=img_botonPuntajes)
Btn_ventanaJuego.place(x=880,y=300)

ordenar_por_aceleracion()

#ordenar_por_temperatura()
#ordenar_por_giro()
#actualizar_archivos()

#Btn_ConnectControl = Button(C_root,text='Send',command=lambda:send(None),fg='white',bg='blue', font=('Agency FB',12))
#Btn_ConnectControl.place(x=450,y=250)

#Btn_Controls = Button(C_root,text='Send & Show ID',command=sendShowID,fg='white',bg='blue', font=('Agency FB',12))
#Btn_Controls.place(x=500,y=250)

#Btn_ConnectControl = Button(C_root,text='Leer Mensaje',command=read,fg='white',bg='blue', font=('Agency FB',12))
#Btn_ConnectControl.place(x=450,y=300)
root.mainloop()
