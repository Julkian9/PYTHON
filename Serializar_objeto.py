import pickle

class vehiculos():
    def __init__(self, marca, modelo):
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False
    
    def arrancar(self):
        self.enmarcha=True
    def acelerar(self):
        self.acelera=True
    def frenar(self):
        self.frena=True
    def estado(self):
        print ("Marcas: ",self.marca,"\nModelo: ",self.modelo,"\nEn marcha: ",self.enmarcha,"\nAcelerando: ",self.acelera,"\nFrenando: ",self.frena)

coche1=vehiculos("Mazda","MX5")

coche2=vehiculos("Seat","Leon")

coche3=vehiculos("Renault","Megane")

coches=[coche1,coche2,coche3]

fichero=open("LosCoches","wb")

pickle.dump(coches, fichero)

fichero.close()

del (fichero)

ficheroApertura=open("LosCoches","rb")

misCoches=pickle.load(ficheroApertura)

ficheroApertura.close()

for c in misCoches:
    print(c.estado())