class Coche():
    def __init__(self):
        self.__largoChasis=250
        self.__anchoChasis=120
        self.__ruedas=4
        self.__enmarcha=False

    def arrancar(self,arrancamos):
        self.__enmarcha=arrancamos
        if(self.__enmarcha):
            return "El coche esta en marcha"
        else:
            return "El coche esta parado"
    def estado(self):
        print("El coche tiene ", self.__ruedas,"ruedas. Un ancho de",self.__anchoChasis,"y un largo de",self.__largoChasis)
        
miCoche=Coche()
print(miCoche.arrancar(True))
miCoche.estado()

print("-------------------A continuacion creamos el segundo objeto-------------------------------")

miCoche2=Coche()
print(miCoche.arrancar(False))
miCoche2.ruedas=2
miCoche2.estado()

print("-------------------A continuacion creamos el tercer objeto-------------------------------")

miCoche3=Coche()
print(miCoche.arrancar(False))
miCoche2.estado()