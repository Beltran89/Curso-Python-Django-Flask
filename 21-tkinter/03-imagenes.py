from tkinter import * 
from PIL import ImageTk, Image

ventana = Tk()
ventana.geometry("700x400")

Label(ventana, text="Hola Soy Ruben").pack(anchor=CENTER)

imagen = Image.open("./21-tkinter/imagenes/skate.jpg")
newImg = imagen.resize((256, 256))
render = ImageTk.PhotoImage(newImg)
Label(ventana, image=render).pack(anchor=CENTER)

ventana.mainloop()
