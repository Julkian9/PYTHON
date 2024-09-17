edad=7
if 0<edad<100:
   print("Edad es correcta")
else:
    print("Edad incorrecta")

salario_presidente=int(input("Introduce Salario presidente: "))
print("salario presidente es " + str(salario_presidente))

salario_director=int(input("Introduce Salario de director: "))
print("salario de director es " + str(salario_director))

salario_jefe_area=int(input("Introduce Salario del jefe de area: "))
print("salario jefe de area es " + str(salario_jefe_area))

salario_administrativo=int(input("Introduce Salario administrativo: "))
print("salario administrativo es " + str(salario_administrativo))

if salario_administrativo<salario_jefe_area<salario_director<salario_presidente:
    print("Todo funciona correctamente")
else:
    print("Algo falla en la empresa")