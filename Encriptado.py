#Funcion menu
def menu():
    texto=[] #Texto sera la lista que va a almacenar el texto a encriptar
    key="" #Auxiliar para llevar el texto en el momento de encriptacion
    print "\n1.- Encriptar. \n2.-Desencriptar\n3.-Salir"
    opcion=input("Inserte Opcion: ")
    while (opcion<1 or opcion>3): #Se valida que se inserte una opcion valida
        print "Inserte una opcion valida"
        opcion=input("\nInserte Opcion: ")
    if opcion==1:
        texto=raw_input("\nInsertar texto: ")
        print(encriptar(texto,0,key))#Se llama a la funcion encriptar, se le pasa el texto, 0 y el auxiliar
        menu()
    elif opcion==2:
        texto=raw_input("\nInsertar texto: ")
        print desencriptar(texto,0,key)#Se llama a la funcion desencriptar, se le pasa el texto, 0 y el auxiliar
        menu()

#Funcion recursiva desencriptar, recibe el texto, la posicion que se usa para ir evaluando la lista y el auxiliar key
def encriptar(texto,pos,key):
    if(pos==len(texto)-1):#Caso base: Llegar al final de la lista
        preTexto=unichr(ord(texto[pos])-3) #Se altera su codigo unicode
        key=key+preTexto
        return key
    if (pos<len(texto)-1): #Mientras recorro la lista
        preTexto=unichr(ord(texto[pos])-3)
        key=key+preTexto
        return encriptar(texto,pos+1,key)
        
def desencriptar(texto,pos,key=""):
    if(pos==len(texto)-1):
        preTexto=unichr(ord(texto[pos])+3)
        key=key+preTexto
        return key
    if (pos<len(texto)-1):
        preTexto=unichr(ord(texto[pos])+3)
        key=key+preTexto
        return desencriptar(texto,pos+1,key)



menu()



