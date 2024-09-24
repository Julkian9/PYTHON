import sqlite3

miConexion=sqlite3.connect("PrimeraBase")

miCursor=miConexion.cursor()

#miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")
#miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALON', 80000, 'DEPORTES')")
#miCursor.execute("INSERT INTO PRODUCTOS VALUES('CACEROLA', 35000,'COCINA')")

#variosProductos=[
    #('Camiseta', 45000, 'Deportes'),
    #('Jarron', 95000, 'Ceramica'),
    #('Camion', 20000, 'Jugueteria'),
    #('Cuchillo', 32000, 'Cocina')
#]
#miCursor.executemany("INSERT INTO PRODUCTOS VALUES(?,?,?)",variosProductos)

miCursor.execute("SELECT * FROM PRODUCTOS")
variosProductos=miCursor.fetchall()
#print(variosProductos)

for producto in variosProductos:
    print("Nombre Articulo: ",producto[0],"\tSeccion: ",producto[2],"\tPrecio: ",producto[1])

miConexion.commit()





miConexion.close()

