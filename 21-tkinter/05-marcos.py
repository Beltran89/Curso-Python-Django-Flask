from tkinter import *

ventana = Tk()
ventana.title("Marcos | Maste Python")
ventana.geometry("700x700")

marco_padre = Frame(ventana, width = 125 , height = 125)
marco_padre.config(
    bg="orange",
    bd=5,
    relief="groove"
)
marco_padre.pack(side=BOTTOM, fill=X, expand=YES, anchor=S)

marco = Frame(marco_padre, width = 250 , height = 250)
marco.config(
    bg="red",
    bd=5,
    relief="solid"
)
marco.pack(side=RIGHT, anchor=SE)

marco = Frame(marco_padre, width = 250, height = 250)
marco.config(
    bg="blue",
    bd=5,
    relief="groove"
)
marco.pack(side=LEFT, anchor=SW)

Label(marco, text="Primer Marco").pack(side=BOTTOM, anchor=CENTER)
marco.pack_propagate(False) 



marco_padre = Frame(ventana, width = 250 , height = 250)
marco_padre.pack(side=TOP, fill=X, expand=YES, anchor=N)

marco = Frame(marco_padre, width = 250, height = 250)
marco.config(
    bg="pink",
    bd=5,
    relief="solid"
)
marco.pack(side=LEFT, anchor=SW)


marco = Frame(marco_padre, width = 250, height = 250)
marco.config(
    bg="green",
    bd=5,
    relief="groove"
)
marco.pack(side=RIGHT, anchor=SE)
ventana.mainloop()