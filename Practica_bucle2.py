#for letra in "python":
#    if letra=="h":
#        continue
#    print("Viendo la palabra " + letra)
#------------------------------------------------------------------------
#nombre="Pildoras Informaticas"
#contador=0
#for i in nombre:
#    if i==" ":
#        continue 
#    contador+=1 #Con el += autoincrementa el valor de la variable en 1
#print(contador)
#------------------------------------------------------------------------
email=input("Introduce tu email, por favor: ")
for i in email:
    if i=="@":
        arroba=True
        break;
else:
    arroba=False
print(arroba)