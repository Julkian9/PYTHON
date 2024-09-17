#print("Verificacion de acceso")
#edad_usuario=int(input("Introduce tu edad por favor: "))
#Valida si la edad del usuario es apta para entrar con 3 condiciones
#if  edad_usuario<18:
#    print("No puedes pasar")
#elif edad_usuario>100:
#    print("Edad incorrecta")
#else:
#    print("Puedes pasar")
#print("El programa ha finalizado")

nota_alumno=int(input("Introduce tu nota, por favor: "))
if nota_alumno<5:
    print("Deficiente")
elif nota_alumno<6:
    print("Insuficiente")
elif nota_alumno<7:
    print("Aceptable")
elif nota_alumno<10:
    print("Sobresaliente")
else:
    print("Excelente")