#Crea un programa que pida introducir una dirección de email por teclado. El programa debe imprimir en consola 
# si la dirección de email es correcta o no en función de si esta tiene el símbolo ‘@’. Si tiene una ‘@’ la 
# dirección será correcta. Si tiene más de una o ninguna ‘@’ la dirección será errónea. Si la ‘@’ está al comienzo 
# de la dirección de email o al final, la dirección también será errónea

contador_arroba=0
contador_puntos=0
mi_email=str(input("Introduce tu direccion de email: "))

ValidarIF=mi_email.count("@")

for i in mi_email:
    if(i=="@"):
        contador_arroba=contador_arroba+1
        

for i in mi_email:
    if(i=="."):
        contador_puntos=contador_puntos+1

if contador_arroba>1:
    print("El correo solo puede tener un caracter de @")
elif contador_arroba==0:
    print("El correo debe tener al menos un caracter @")

if contador_puntos==0:
    print("El correo debe tener al menos un caracter de punto")

while mi_email[0]=="@" or mi_email[-1]=="@":
    print("El caracter arroba no puede estar al inicio o al final")
    mi_email=str(input("Introduce tu direccion de email: "))

if contador_arroba==1 and contador_puntos>0:
    print("El email es correcto")
else:
    print("El email es incorrecto")