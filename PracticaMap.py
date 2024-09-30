class Empleado:

    def __init__(self,nombre,cargo,salario):
        self.nombre=nombre
        self.cargo=cargo
        self.salario=salario

    def __str__(self):
        return "{} que trabaja como {} tiene un salario de {} $".format(self.nombre,self.cargo,self.salario)
    
listaEmpleados=[
    Empleado("Julian","Director",75000),
    Empleado("Ana","Presidente",90000),
    Empleado("Martha","Gerente",80000),
    Empleado("Lucas","Administrativo",40000),
    Empleado("Falcao","Soporte",40000)
]

def calculoComision(empleado):
    if(empleado.salario<=3000):
        empleado.salario=empleado.salario*1.03
    return empleado

listaEmpleadosComision=map(calculoComision,listaEmpleados)

for empleado in listaEmpleadosComision:
    print(empleado)