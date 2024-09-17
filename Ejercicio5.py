#Crea un programa que pida por teclado introducir una contraseña. La contraseña no podrá tener menos 
# de 8 caracteres ni espacios en blanco. Si la contraseña es correcta, el programa imprime “Contraseña OK”. 
# En caso contrario imprime “Contraseña errónea”

print("Recomendaciones: La contraseña debe tener 8 o mas caracteres, no debe haber espacios en blanco")
micontraseña=input("Introduce tu nueva contraseña: ")
Contador=0

for i in range(len(micontraseña)):
    if micontraseña[i]==" ":
        Contador=Contador+1

if len(micontraseña)<8:
    Contador=Contador+1

if Contador==0:
    print("La contraseña es valida")
else:
    print("La contraseña no cumple con las caracteristicas correctas")