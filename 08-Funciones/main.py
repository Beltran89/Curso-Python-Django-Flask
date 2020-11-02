"""

FUNCIONES: 
    Es un conjunto de intrucciones agrupadas bajo un nombre
    concreto que pueden reutilizarse invocando a la funcion
    tantas veces como sea necesario

"""

#def nombreDeMiFuncion(Argumentos)
    # Bloque / conjunto de Instruciones


#Ejemplo 1

def muestraNombre(nombre, edad):
    if edad >= 18:
        print(f"Su nombre es {nombre}, y eres mayor de edad")
    else:
        print(f"Su nombre es {nombre}, y eres menor de edad")

muestraNombre("ruben",31)
muestraNombre("Lorena",15)

# EJEMPLO 2

def tablaMultiplicar(numero):
    print(f"TABLA DE MULTIPLICAR DEL {numero}")
    
    for contador in range(11):
        print(f"{numero}  X {contador} = {numero*contador} ")
    print("\n")

tablaMultiplicar(5)
tablaMultiplicar(2)

# EJEMPLO 3 (parametro opcional)

def getEmpleado(nombre, dni = False):  # Tambien valido dni = None
    print(f"Nombre {nombre}")
    if dni != False:
        print(f"DNI {dni}")

getEmpleado("ruben","12155")
getEmpleado("malonin")

#EJEMPLO 4

def saludame(nombre):
    saludo = f"Hola {nombre}"
    
    return saludo

print(saludame("EL CHEPAS"))

#EEJMPLO 5 Funciones dentro de otras Funciones

def getNombre(nombre):
    texto = f"El nombre es : {nombre}"
    return texto

def getApellids(apellido):
    texto = f"El apellido es : {apellido}"
    return texto

def getTodo(nombre, apellido):
    texto = getNombre(nombre) + " " + getApellids(apellido)
    return texto

print(getTodo("Manolo", "El del Bombo"))

# Ejemplo 6 Funciones Lambda (funcion anonima)

dime_el_year = lambda year:f"El año es {year}"
print(dime_el_year(2024))