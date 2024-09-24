import pickle
#lista_nombres=["Juan","Diego","Karen","Diana","Paola","Isabel"]
#fichero_binario=open("lista_nombres","wb") abre el fichero binario [nombre] y con la opcion wb escritura en binario
#pickle.dump(lista_nombres,fichero_binario) volca la informacion de la lista al fichero binario
#fichero_binario.close() Cierra el fichero
#del (fichero_binario) Borra en memoria el fichero

fichero=open("lista_nombres","rb")  #lee el fichero binario
lista=pickle.load(fichero) #Carga la informacion en el fichero
print(lista)