#Clase Encriptacion
class crypto:
    texto=""
    def __init__(self,texto):   #constructor
        crypto.texto = texto
    
    
    #Funcion recursiva desencriptar, recibe el texto, la posicion que se usa para ir evaluando la lista y el auxiliar key
    def encriptar(self,pos,key):
        texto=crypto.texto
        if(pos==(len(texto))-1):                 #Caso base: Llegar al final de la lista
            preTexto=unichr(ord(texto[pos])-3) #Se altera su codigo unicode
            key=key+preTexto                   #Almacena en el auxiliar
            return key                         #se retorna el texto encriptado
        if (pos<(len(texto))-1):                 #Recorro la lista
            preTexto=unichr(ord(texto[pos])-3)
            key=key+preTexto
            return crypto.encriptar(self,pos+1,key)  #se llama a la funcion

    #Funcion desencriptar, recibe el texto, la posicion que se usa para ir evaluando la lista y el auxiliar key
    def desencriptar(self,pos,key):
        texto=crypto.texto
        if(pos==(len(texto))-1):
            preTexto=unichr(ord(texto[pos])+3) #Se altera el codigo de manera inversa a la funcion encriptar
            key=key+preTexto
            return key
        if (pos<(len(texto))-1):
            preTexto=unichr(ord(texto[pos])+3)
            key=key+preTexto
            return crypto.desencriptar(self,pos+1,key)#se llama a la funcion
