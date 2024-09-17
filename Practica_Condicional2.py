print("Asignatura Optativa Año 2017")
print("Asignaturas optativas: Informatica grafica - Pruebas de software - Usabilidad y accesibilidad")
asignatura=input("Escribe la asignatura escogida: ").lower()


if asignatura in ("informatica grafica","pruebas de software","usabilidad y accesibilidad"):
    print("Asignatura elegida " + asignatura)
else:
    print("La asignatura escogida no esta contemplada")



#print("Programa de becas año 2017")
#distancia_escuela=int(input("Introduce la distancia a la escuela en km: "))
#print(distancia_escuela)

#numero_hermanos=int(input("Introduce el # de hermanos en el centro: "))
#print(numero_hermanos)

#salario_familiar=int(input("Introduce tu salario anual bruto: "))
#print(salario_familiar)

#if distancia_escuela>40 and numero_hermanos>2 or salario_familiar<=200000:
#    print("Tienes derecho a beca")
#else:
#    print("No tienes derecho a beca")