from tkinter import *

raiz=Tk()

raiz.title("VENTANA DE PRUEBA :D")
#raiz.resizable(1,1) #(Width alto y Height ancho) 1=true 0=false es decir permite o no cambiar dimensiones
#raiz.iconbitmap("imagen")
#raiz.geometry("650x350") #Define el alto y el ancho

raiz.config(background="blue")

miFrame=Frame()
miFrame.pack()#side="bottom", anchor="e" fill="y", expand="true"
miFrame.config(background="yellow")
miFrame.config(width="650",height="350")
miFrame.config(bd="5")
miFrame.config(relief="sunken")
miFrame.config(cursor="pirate")
raiz.mainloop()