from tkinter import *

#Crear la ventana raiz

ventana = Tk()

#Cambiar tamañao de la ventana
ventana.geometry("750x450") #Tamaño

#Bloquear tamaño de la venta
ventana.resizable(0,0)
'''
ventana.resizable(1,0) SOLO DEJA A NIVEL HORIZONTAL
ventana.resizable(0,1) SOLO DEJA A NIVEL VERTICAL
'''

#Icono de la ventana
ventana.iconbitmap("./21-tkinter/imagenes/car.ico")

#Titulo
ventana.title("Mi ventana tkinter")
#Mostar Texto
saludo = " Hola mundo desde interface grafica"
texto = Label(ventana, text = saludo)
texto.pack()

#Arrancar y mostrar la ventana hasta que se cierre

ventana.mainloop()