class Coche():
#Contrustor de la clase
    def __init__(self):
        self.__largoChasis=250
        self.__anchoChasis=120
        self.__ruedas=4
        self.__enmarcha=False
#Metodo
    def arrancar(self,arrancamos):
        self.__enmarcha=arrancamos
        if(self.__enmarcha):
            chequeo=self.chequeo_interno()
        if(self.__enmarcha and chequeo):
            return "El coche esta en marcha"
        elif(self.__enmarcha and chequeo==False):
            return "Algo ha ido mal en el chequeo no podemos arrancar"
        else:
            return "El coche esta parado"
    def estado(self):
        print("El coche tiene ", self.__ruedas,"ruedas. Un ancho de",self.__anchoChasis,"y un largo de",self.__largoChasis)

    def __chequeo_interno(self):
        print("Realizando un chequeo interno...")
        self.gasolina="OK"
        self.aceite="OK"
        self.puertas="Cerradas"

        if(self.gasolina=="OK" and self.aceite=="OK" and self.puertas=="Cerradas"):
            return True
        else:
            return False

miCoche=Coche()
print(miCoche.arrancar(True))
miCoche.estado()

print("-------------------A continuacion creamos el segundo objeto-------------------------------")

miCoche2=Coche()
print(miCoche2.arrancar(False))
miCoche2.estado()

print("-------------------A continuacion creamos el tercer objeto-------------------------------")

miCoche3=Coche()
print(miCoche3.arrancar(False))
miCoche2.estado()