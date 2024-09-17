#Crea un programa que pida tres números por teclado. El programa imprime en consola la media aritmética de los 
# números introducidos.

n1=int(input("Introduce el primer numero: "))
n2=int(input("Introduce el segundo numero: "))
n3=int(input("Introduce el tercer numero: "))


def media(n1,n2,n3):
    m1=(n1+n2+n3)/3
    print(m1)


print("La media arimetica es: ")

media(n1,n2,n3)
