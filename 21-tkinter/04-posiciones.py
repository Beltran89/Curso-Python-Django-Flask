from tkinter import *

ventana = Tk()
#ventana.geometry("500x500")
#ventana.resizable(1,0)

texto = Label(ventana, text = "Bienvenido a mi programa")
texto.config(
    fg="white",
    bg="#000000",
    padx=20,         #Margen Horizontal
    pady=30,         #Margen Vertical
    font=("Consolas", 25)
)
texto.pack()
texto = Label(ventana, text = "Soy Ruben")
texto.config(
    height=10,
    bg="orange",
    font=("Arial",12)
)
texto.pack(side=TOP,expand=YES, fill=X) # Con TOP Elegimos las ubicacion, EXPAND que se expanda, FILL elejimos en que eje se expande


texto = Label(ventana, text = "basico 1")
texto.config(
    height=3,
    bg="green",
    font=("Arial",15)
)
texto.pack(side=LEFT,expand=YES, fill=X)# Con TOP Elegimos las ubicacion, EXPAND que se expanda, FILL elejimos en que eje se expande

texto = Label(ventana, text = "basico 2")
texto.config(
    height=3,
    bg="red",
    font=("Arial",15)
)
texto.pack(side=LEFT,expand=YES, fill=X)# Con TOP Elegimos las ubicacion, EXPAND que se expanda, FILL elejimos en que eje se expande

texto = Label(ventana, text = "basico 3")
texto.config(
    height=3,
    bg="blue",
    font=("Arial",15)
)
texto.pack(side=LEFT,expand=YES, fill=X)# Con TOP Elegimos las ubicacion, EXPAND que se expanda, FILL elejimos en que eje se expande
ventana.mainloop()