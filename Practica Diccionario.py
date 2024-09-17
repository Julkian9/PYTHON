#Se crea el diccionario con clave:valor
midiccionario={"Alemania":"Berlin","Francia":"Paris","Reino Unido":"Londres","España":"Madrid"}
#Imprime en consola el valor de una clave en este caso de reino unido trea el valor de londres
print(midiccionario["Reino Unido"])
#Imprime en consola todo el diccionario
print(midiccionario)
#Añadir al diccionario mas claves elementos
midiccionario["Italia"]="Lisboa"
print(midiccionario)
#Corregir una clave valor del diccionario
midiccionario["Italia"]="Roma"
print(midiccionario)
#Borrar del diccionario una clave y valor
del midiccionario["España"]
print(midiccionario)
#Muestra de clave valor con diferentes formatos de datos
midiccionario2={"Alemania":"Berlin",23:"Michael Jordan","Mosqueteros":3}
print(midiccionario2)
#Asociar una tupla a un diccionario en donde se usa el indice para asociar como valor:clave 
mitupla=["Colombia","Venezuela","Ecuador","Peru"]
midiccionario3={mitupla[0]:"Bogota",mitupla[1]:"Caracas",mitupla[2]:"Quito",mitupla[3]:"Lima"}
print(midiccionario3)
print(midiccionario3["Colombia"])
#Se puede asignar sobre un diccionario una tupla con varios valores
midiccionario4={23:"Jordan", "Nombre":"Michael","Equipo":"Chicago","Anillos":[1991,1992,1993,1996,1997,1998]}
print(midiccionario4["Equipo"])
print(midiccionario4["Anillos"])
#Imprimir las claves
print(midiccionario4.keys())
#Imprimir valores
print(midiccionario4.values())
#Imprimir la cantidad de llaves valores
print(len(midiccionario4))