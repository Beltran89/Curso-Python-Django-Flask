from tkinter import *

class Programa:
    def __init__(self):
        self.title = "Master de Python"
        self.icon = "./21-tkinter/imagenes/car.ico"
        self.size = "470x470"
        self.resizable = True
    
    def cargar(self):
        ventana = Tk()
        self.ventana = ventana
        
        ventana.geometry(self.size)
        ventana.title(self.title)
        
        if self.resizable:
            ventana.resizable(1,1)
        else:
            ventana.resizable(0,0)
        #ventana.mainloop()
    
    def addtexto(self, dato):
        texto = Label(self.ventana, text = dato)
        texto.pack()
    
    def mostrar(self):
        self.ventana.mainloop()

programa = Programa()
programa.cargar()
programa.addtexto("yeahhhhhh")
programa.addtexto("Esto funciona")
programa.addtexto("carallo")
programa.addtexto("yeahhhhhh")
programa.mostrar()