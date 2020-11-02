from tkinter import *

class Programa:
    def __init__(self):
        self.title = "MAStes de Python"
        self.icon = "./21-tkinter/imagenes/car.ico"
        self.size = "470x470"
        self.resizable = True
    
    def cargar(self):
        ventana = Tk()
        ventana.geometry(self.size)
        ventana.title(self.title)
        saludo = " Hola mundo desde interface grafica"
        texto = Label(ventana, text = saludo)
        texto.pack()
        if self.resizable:
            ventana.resizable(1,1)
        else:
            ventana.resizable(0,0)
        ventana.mainloop()

programa = Programa()
programa.cargar()