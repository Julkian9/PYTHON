class persona():

    def __init__(self, nombre, edad, Lugar_residencia):
        self.nombre=nombre
        self.edad=edad
        self.Lugar_residencia=Lugar_residencia
    def descripcion(self):
        print("Nombre: ",self.nombre," Edad: ",self.edad," Residencia: ",self.Lugar_residencia)

class Empleado(persona):

    def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, residencia_empleado):
        super().__init__(nombre_empleado, edad_empleado, residencia_empleado)
        self.salario=salario
        self.antiguedad=antiguedad
#Se hereda la descripcion de la clase persona con sus datos nombre, edad y residencia
    def descripcion(self):
        super().descripcion()
        print("Salario: ",self.salario," Antiguedad: ",self.antiguedad)

#Alejandro=Empleado(4000000, 1, "Alejandro", 45, "Cali")
Alejandro=persona("Alejandro",45,"Cali")
Alejandro.descripcion()

print("Es un empleado: ",isinstance(Alejandro, Empleado))
print("Es un persona: ",isinstance(Alejandro, persona))