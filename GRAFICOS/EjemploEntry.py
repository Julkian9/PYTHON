from tkinter import *

raiz=Tk()
raiz.title("Interface de usuario")
miFrame=Frame(raiz, width=1200,height=600)
miFrame.pack()
miFrame.config(bg="#abebc6")

minombre=StringVar()

cuadroNombre=Entry(miFrame,textvariable=minombre)
cuadroNombre.grid(row=0,column=1)
nombreLabel=Label(miFrame,text="Nombre:")
nombreLabel.grid(row=0,column=0, sticky="e",padx="10",pady="10")
cuadroNombre.config(fg="#000080",justify="left")

cuadroPass=Entry(miFrame)
cuadroPass.grid(row=1,column=1)
PassLabel=Label(miFrame,text="Password: ")
PassLabel.grid(row=1,column=0, sticky="e",padx=10,pady=10)
cuadroPass.config(show="*")

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=2,column=1)
apellidoLabel=Label(miFrame,text="Apellido: ")
apellidoLabel.grid(row=2,column=0, sticky="e",padx=10,pady=10)

cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=3,column=1)
direccionLabel=Label(miFrame,text="Direccion:")
direccionLabel.grid(row=3,column=0,padx=10,pady=10)


comentariosLabel=Label(miFrame,text="Comentarios: ")
comentariosLabel.grid(row=4,column=0,padx=10,pady=10)
textoComentario=Text(miFrame, width=16,height=6)
textoComentario.grid(row=4,column=1,padx=10,pady=10)
scrollVert=Scrollbar(miFrame,command=textoComentario.yview)
scrollVert.grid(row=4,column=2,sticky="nsew")
textoComentario.config(yscrollcommand=scrollVert.set)

def codigoBoton():
    minombre.set("Julian")
botonEnvio=Button(raiz,text="Enviar",command=codigoBoton)
botonEnvio.pack()

raiz.mainloop()