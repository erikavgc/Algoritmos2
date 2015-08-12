#Clase archivos contiene metodos para leer archivo y crear

class archivos:
    @staticmethod #metodo estatico crear
    def crear(texto):
        archi=open('nota.txt',"w") #abro el archivo y reemplazo si ya existe
        archi.write(texto)         #escribo el texto encriptado/desencriptado
        archi.close()              #cierro el archivo
    @staticmethod
    def leer():  #metodo estatico leer
        archi=open('nota.txt',"r")#abro el archivo para leer su contenido
        texto=archi.read()        #almaceno el texto del archivo
        archi.close()
        return texto              #retorno texto



        
        
