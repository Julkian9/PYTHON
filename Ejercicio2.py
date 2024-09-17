#Crea un programa que pida por teclado “Nombre”, “Dirección” y “Tfno”. Esos tres datos deberán ser almacenados 
# en una lista y mostrar en consola el mensaje: “Los datos personales son: nombre apellido teléfono” 
# (Se mostrarán los datos introducidos por teclado).

name=input("Introduzca su nombre: ")
adress=input("Introduzca su direccion: ")
phone=input("Introduzca su numero de telefono: ")

milista=[name,adress,phone]

print("Los datos personasles son: ")
print(milista)