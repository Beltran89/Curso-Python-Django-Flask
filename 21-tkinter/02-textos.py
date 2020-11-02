from tkinter import *

ventana = Tk()
ventana.geometry("500x500")
ventana.resizable(1,0)

texto = Label(ventana, text = "Bienvenido a mi programa")
texto.config(
    fg="white",
    bg="#000000",
    padx=20,         #Margen Horizontal
    pady=30,         #Margen Vertical
    font=("Consolas", 30)
)
texto.pack()
texto = Label(ventana, text = "Soy Ruben")
texto.config(
    height=10,
    bg="orange",
    font=("Arial",7)
)
texto.pack(anchor=SE)


def pruebas(nombre, apellidos, pais):
    return f"Hola {nombre} {apellidos} veo que eres del pais {pais}"
texto = Label(ventana, text = pruebas("ruben", "Beltran", "España"))
texto.config(
    height=3,
    bg="green",
    font=("Arial",15)
)
texto.pack(anchor=W)
ventana.mainloop()