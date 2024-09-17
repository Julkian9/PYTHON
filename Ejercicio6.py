#Crea un programa que evalúe si una dirección de correo electrónico es válida o no en función 
# de si tiene “@” o “.” Hay que tener en cuenta que la dirección se considera correcta si solo 
# tiene una “@” y si tiene uno o más “.”

contador_arroba=0
contador_puntos=0
mi_email=input("Introduce tu direccion de email: ")
for i in mi_email:
    if(i=="@"):
        contador_arroba=contador_arroba+1
        

for i in mi_email:
    if(i=="."):
        contador_puntos=contador_puntos+1
        
if contador_arroba==1 and contador_puntos>0:
    print("El email es correcto")
else:
    print("El email es incorrecto")