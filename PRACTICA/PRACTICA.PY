from tkinter import *
from tkinter import messagebox
import sqlite3

#---------------------FUNCIONES----------------------
def conexionBBDD():
    
    miConexion=sqlite3.connect("Usuarios")
    miCursor=miConexion.cursor()
    try:
        miCursor.execute('''
            CREATE TABLE DATOSUSUARIOS (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOMBRE_USUARIO VARCHAR(50),
            PASSWORD VARCHAR(50),
            APELLIDO VARCHAR(10),
            DIRECCION VARCHAR(50),
            COMENTARIOS VARCHAR(100))
            ''')
        messagebox.showinfo("BBDD", "BBDD creada con exito")
    except:
        messagebox.showwarning("¡Atencion!", "La BBDD ya existe")

def salirAplicacion():
    valor=messagebox.askquestion("Salir","¿Deseas salir de la aplicacion?")
    if valor=="yes":
        root.destroy()


def limpiarCampos():
    idBD.set("")
    nombre.set("")
    contrase.set("")
    apellido.set("")
    direccion.set("")
    cuadroComent.delete(1.0,END)

def crearCampos():
    miConexion=sqlite3.connect("Usuarios")
    miCursor=miConexion.cursor()
    """miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL, '" + nombre.get() + "','" + contrase.get() + "','" + apellido.get() + "','" + direccion.get() +"','" + cuadroComent.get("1.0",END) + "')")"""

    datos=nombre.get(),contrase.get(),apellido.get(),direccion.get(),cuadroComent.get("1.0",END)
    miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL,?,?,?,?,?)",(datos))
    miConexion.commit()
    messagebox.showinfo("BBDD","Registro insertado con exito")


def leerBDDD():
    miConexion=sqlite3.connect("Usuarios")
    miCursor=miConexion.cursor()

    miCursor.execute("SELECT * FROM DATOSUSUARIOS WHERE ID=" + idBD.get())
    elUsuario=miCursor.fetchall()
    for usuario in elUsuario:
        idBD.set(usuario[0])
        nombre.set(usuario[1])
        contrase.set(usuario[2])
        apellido.set(usuario[3])
        direccion.set(usuario[4])
        cuadroComent.insert(1.0,usuario[5])
    
    miConexion.commit()

def actualizar():
    miConexion=sqlite3.connect("Usuarios")
    miCursor=miConexion.cursor()
    """"miCursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO='" + nombre.get() + "', PASSWORD='" + contrase.get() + "', APELLIDO='" + apellido.get() + "', DIRECCION='" + direccion.get() + "', COMENTARIOS='" + cuadroComent.get("1.0", END) + "' WHERE ID=" + idBD.get())"""
    datos=nombre.get(),contrase.get(),apellido.get(),direccion.get(),cuadroComent.get("1.0",END)
    miCursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO=?,PASSWORD=?,APELLIDO=?,DIRECCION=?,COMENTARIOS=?" + "WHERE ID=" + idBD.get(),(datos))
    miConexion.commit()
    messagebox.showinfo("BBDD","Registro actualizado con exito")

def eliminar():
    miConexion=sqlite3.connect("Usuarios")
    miCursor=miConexion.cursor()
    miCursor.execute("DELETE FROM DATOSUSUARIOS WHERE ID=" + idBD.get())
    miConexion.commit()
    messagebox.showinfo("BBDD", "Registro borrado exitosamente")


#---------------------INTERFAZ GRAFICA----------------------
root=Tk()
root.title("ADM BASE DE DATOS")
miFrame=Frame(root)
miFrame.pack()
miFrameButtons=Frame(root)
miFrameButtons.pack()


#---------------------CAMPOS----------------------

#***********ID*************
idBD=StringVar()
cuadroId=Entry(miFrame,textvariable=idBD)
cuadroId.grid(column=1,row=0)
labelId=Label(miFrame,text="ID: ")
labelId.grid(column=0,row=0,padx=10,pady=10)
cuadroId.config(justify="left")

#***********NOMBRE*************
nombre=StringVar()
cuadroNombre=Entry(miFrame,textvariable=nombre)
cuadroNombre.grid(column=1,row=1)
labelNombre=Label(miFrame,text="NOMBRE: ")
labelNombre.grid(column=0,row=1,padx=10,pady=10)
cuadroNombre.config(justify="left")

#***********PASSWORD*************
contrase=StringVar()
cuadroContrase=Entry(miFrame,textvariable=contrase)
cuadroContrase.config(show="*")
cuadroContrase.grid(column=1,row=2)
labelContrase=Label(miFrame,text="PASSWORD:")
labelContrase.grid(column=0,row=2,padx=10,pady=10)
cuadroContrase.config(justify="left")

#***********APELLIDO*************
apellido=StringVar()
cuadroApellido=Entry(miFrame,textvariable=apellido)
cuadroApellido.grid(column=1,row=3)
labelApellido=Label(miFrame,text="APELLIDO: ")
labelApellido.grid(column=0,row=3,padx=10,pady=10)
cuadroApellido.config(justify="left")

#***********DIRECCION*************
direccion=StringVar()
cuadroDir=Entry(miFrame,textvariable=direccion)
cuadroDir.grid(column=1,row=4)
labelDir=Label(miFrame,text="DIRECCION: ")
labelDir.grid(column=0,row=4,padx=10,pady=10)
cuadroDir.config(justify="left")

#***********COMENTARIO*************
coment=StringVar()
cuadroComent=Text(miFrame,width=16,height=5)
cuadroComent.grid(column=1,row=5,padx=10,pady=10)
ScrollVert=Scrollbar(miFrame, command=cuadroComent.yview)
ScrollVert.grid(row=5,column=2,sticky="nsew")
labelComent=Label(miFrame,text="COMENTARIO: ")
labelComent.grid(column=0,row=5,padx=10,pady=10)
cuadroComent.config(yscrollcommand=ScrollVert.set)

#---------------------BOTONES----------------------

#***********CREATE*************
botonCreate=Button(miFrameButtons,text="CREATE",command=crearCampos)
botonCreate.grid(row=0,column=0,padx=6,pady=6)

#***********READ*************
botonRead=Button(miFrameButtons,text="READ", command=leerBDDD)
botonRead.grid(row=0,column=1,padx=6,pady=6)

#***********UPDATE*************
botonUpdate=Button(miFrameButtons,text="UPDATE", command=actualizar)
botonUpdate.grid(row=0,column=2,padx=6,pady=6)

#***********DELETE*************
botonDelete=Button(miFrameButtons,text="DELETE", command=eliminar)
botonDelete.grid(row=0,column=3,padx=6,pady=6)

#---------------------MENU----------------------
barraMenu=Menu(root)
root.config(menu=barraMenu,width=300,height=300)

#***********BBDD*************
bdMenu=Menu(barraMenu,tearoff=0)
barraMenu.add_cascade(label="BBDD",menu=bdMenu)
bdMenu.add_command(label="Conectar", command=conexionBBDD)
bdMenu.add_command(label="Salir", command=salirAplicacion)

#***********BORRAR*************
borrarMenu=Menu(barraMenu,tearoff=0)
barraMenu.add_cascade(label="Borrar",menu=borrarMenu)
borrarMenu.add_command(label="Borrar Campos", command=limpiarCampos)

#***********CRUD*************
crudMenu=Menu(barraMenu,tearoff=0)
barraMenu.add_cascade(label="CRUD",menu=crudMenu)
crudMenu.add_command(label="CREATE", command=crearCampos)
crudMenu.add_command(label="READ", command=leerBDDD)
crudMenu.add_command(label="UPDATE", command=actualizar)
crudMenu.add_command(label="DELETE", command=eliminar)
#***********CRUD*************
ayudaMenu=Menu(barraMenu,tearoff=0)
barraMenu.add_cascade(label="Ayuda",menu=ayudaMenu)
ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Acerca de...")


root.mainloop()