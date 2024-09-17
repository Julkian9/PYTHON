print("Programa de evaluacoin de notas de alumnos")
#Con el Input solicitamos a la persona que debe ingresar un valor y hasta que no lo coloque no se ejecutara el siguiente bloque de codigo
nota_alumno=input("Introduce la nota del alumno: ")
#Funcion que permite determinar si un alumno Aprueba o Suspende segun el valor numerico asignado
def evaluacion(nota):
    valoracion="aprobado"
    if nota<5:
        valoracion="Suspendido"
    return valoracion
#Con la palabra de int volvemos el valor dentro de una variable a numero entero
print(evaluacion(int(nota_alumno)))