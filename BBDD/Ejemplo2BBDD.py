import sqlite3
miConexion=sqlite3.connect("Gestion Productos")
miCursor=miConexion.cursor()

#miCursor.execute('''
#    CREATE TABLE PRODUCTOS (
#    ID INTEGER PRIMARY KEY AUTOINCREMENT,
#    NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
#    PRECIO INTEGER,
#    SECCION VARCHAR(20))
#''')

#productos=[

#    ("pelota", 20, "jugueteria"),
#    ("pantalon", 15, "confeccion"),
#    ("destornillador", 15, "ferreteria"),
#    ("jarron", 45, "ceramica"),
#    ("pantalones", 30, "confeccion")

#]

#miCursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)", productos)

#miCursor.execute("INSERT INTO PRODUCTOS VALUES (NULL,'tren', 15, 'jugueteria')")

#miCursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION='confeccion'")

#productos=miCursor.fetchall()

#print(productos)

#miCursor.execute("UPDATE PRODUCTOS SET PRECIO=35 WHERE NOMBRE_ARTICULO='pelota'")

#miCursor.execute("DELETE FROM PRODUCTOS WHERE ID=5")


miConexion.commit()
miConexion.close()