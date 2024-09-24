from tkinter import *

root=Tk()

root.title("Ejemplo")

foto=PhotoImage(file="avion.png")
Label(root, image=foto).pack()

frame=Frame(root)
frame.pack()

Label(frame, text="Elige destinos",width=50).pack()

playa=IntVar()
montanya=IntVar()
turismoRural=IntVar()

def opcionesViaje():
    opcionEscogido=""

    if(playa.get()==1):
        opcionEscogido+="Playa,"
    if(montanya.get()==1):
        opcionEscogido+=" Montaña,"
    if(turismoRural.get()==1):
        opcionEscogido+=" Turismo Rural."

    textoFinal.config(text=opcionEscogido)

Checkbutton(root,text="Playa",variable=playa, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(root,text="Montaña",variable=montanya, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(root,text="Turismo rural",variable=turismoRural, onvalue=1, offvalue=0, command=opcionesViaje).pack()

textoFinal=Label(frame)
textoFinal.pack()

root.mainloop()