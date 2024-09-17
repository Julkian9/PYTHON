#Crea un programa que pida dos números por teclado. El programa tendrá una función llamada “DevuelveMax” 
#encargada de devolver el número más alto de los dos introducidos.

n1=int(input("Introduzca el primer numero: "))
n2=int(input("Introduzca el segundo numero: "))

def DevuelveMax(n1,n2):
    if n1>n2:
        print(n1)
    elif n2>n1:
        print(n2)
    else:
        print("Los numeros son iguales")

print("El numero mas alto es: " + " ")

DevuelveMax(n1,n2)


