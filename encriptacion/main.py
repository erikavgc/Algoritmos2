from archivos import * #importo clase archivos
from crypto import *   #importo clase de encriptacion

def menu():  
    texto=[] #Texto sera la lista que va a almacenar el texto a encriptar
    key="" #Auxiliar para llevar el texto en el momento de encriptacion
    print "\n1.- Encriptar. \n2.-Desencriptar\n3.-Salir"
    opcion=raw_input("Inserte Opcion: ")
    if opcion=="1":
        texto=archivos.leer()  #leo el texto y almaceno en variable
        x=crypto(texto)     #creo un objeto de tipo texto
        aux=x.encriptar(0,key)#Se llama a la funcion encriptar con el objeto creado
        archivos.crear(aux) #Se crea el archivo encriptado
        print "Listo"
        menu()
    elif opcion=="2":     
        texto=archivos.leer()   
        y=crypto(texto)
        aux=y.desencriptar(0,key)
        archivos.crear(aux)
        print "Listo"
        menu()
    else:
        print "Inserte una opcion valida"
        menu()


menu()


    
    
    
