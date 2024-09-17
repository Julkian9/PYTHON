#for i in ["Primavera","Verano","Otoño","Invierno"]:
#    print(i)


#contador=0
#mi_email=input("Introduce tu direccion de email: ")
#for i in mi_email:
#    if(i=="@" or i=="."):
#        contador=contador+1
#if contador==2:
#    print("El email es correcto")
#else:
#    print("El email es incorrecto")

#for i in range(5):
#    print("Hola")

valido=False

email=input("Introduzca un email: ")

for i in range(len(email)):
    if email[i]=="@":
        valido=True

if valido:
    print("Email correcto")
else:
    print("Email incorrecto")