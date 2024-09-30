areaTriangulo=lambda base,altura: (base+altura)/2
triangulo1=areaTriangulo(7,6)
triangulo2=areaTriangulo(3,2)
print(triangulo1)
print(triangulo2)

al_cubo= lambda numero: numero**3

calculo1=al_cubo(4)
calculo2=al_cubo(8)

print(calculo1)
print(calculo2)


val_des=lambda comision:"¡{}! Pesos".format(comision)

comisionOto=65000

print(val_des(comisionOto))