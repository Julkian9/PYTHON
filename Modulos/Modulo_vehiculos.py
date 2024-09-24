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

class   Furgoneta(vehiculos):
    def carga(self, cargar):
        self.cargado=cargar
        if (self.cargado):
            return "La furgoneta esta cargada"
        else:
            return "La furgoneta no esta cargada"

#Se hereda los parametros de la clase vehiculos en la clase moto
class Moto(vehiculos):
    hcaballito=""
    def caballito(self):
        self.hcaballito="Estoy haciendo caballito"
    def estado(self):
        print ("Marcas: ",self.marca,"\nModelo: ",self.modelo,"\nEn marcha: ",self.enmarcha,"\nAcelerando: ",self.acelera,"\nFrenando: ",self.frena,"\n",self.hcaballito)

class VElectricos(vehiculos):
    def __init__(self,marca,modelo):
        super().__init__(marca,modelo)
        self.autonomia=100
    def cargarEnergia(self):
        self.cargando=True