from tkinter import *


root=Tk()

miFrame=Frame(root, width=500, height=400)
miFrame.pack()
miImage=PhotoImage(file="kumoko.png")
Label(miFrame, image=miImage).place(x=120,y=100)
#Label(miFrame, text="Hola alumnos de python",fg="red",font=("Arial",18)).place(x=120,y=100)
#miLabel= Label(miFrame, text="Hola alumnos de python")
#miLabel.place(x=150,y=100)
root.mainloop()