from io import open

#Crea un archivo editable
#archivo_texto=open("archivo.txt","w")
#frase="Estupendo dia para estudiar Python \n el jueves"
#Coloca la frase dentro del archivo
#archivo_texto.write(frase)
#Cierra el archivo en memoria
#archivo_texto.close()

#Abre el archivo en solo lectura y almacena el texto en una variable
#archivo_texto=open("archivo.txt","r")
#texto=archivo_texto.read()
#archivo_texto.close()
#print(texto)

#Crea un lista del texto en el documento
#archivo_texto=open("archivo.txt","r")
#lineas_texto=archivo_texto.readlines()
#archivo_texto.close()
#print(lineas_texto[1])

#archivo_texto=open("archivo.txt","a") #a de append agregar
#archivo_texto.write("\n Siempre es una buena ocasion para estudiar Python")
#archivo_texto.close()

#archivo_texto=open("archivo.txt","r")
#Se posiciona en el caracter indicado y empieza a leer
#archivo_texto.seek(11)
#el .read(n) con valor solo lee la cantidad de caracteres indicados
#print(archivo_texto.read(11))

#Lee el archivo desde la mitad
#archivo_texto.seek(len(archivo_texto.read())/2)

#Lee apartir del final de la primera linea
#archivo_texto.seek(len(archivo_texto.readline()))

#archivo_texto=open("archivo.txt","r+") #Lectura y escritura
#archivo_texto.write("Comienza el texto") Sobrescribe en la primera linea
#print(archivo_texto.read())

archivo_texto=open("archivo.txt","r+")
lista_texto=archivo_texto.readlines();
lista_texto[1]=" Esta lineaha sido incluida desde el exterior \n"
archivo_texto.seek(0)
archivo_texto.writelines(lista_texto)
archivo_texto.close()
