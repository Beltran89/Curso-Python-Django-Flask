"""
Ejercicio 2-1 HAcer un prgrama que tenga una lista
de 8 numeros enteros y haga lo siguiente:
- Recorrer la lista y mostrarla
- Hacer funcion que recorra la lista de numeros y devuelva un string
- Ordenarla y mostrarla
- Mostrar su longitud
- Buscar algun elemento (que pida el usuario)
"""

numeros = [2,8,78,88,23,15,1,46]

print("##########Punto 1 ##########")
for numero in numeros :
    print(numero)

print("\n##########Punto 2  ##########")
def numLista(lista):
    retorno = ""
    for numero in lista :
        retorno = retorno + str(numero) + " , "
    return retorno

print(numLista(numeros))

print("\n##########Punto 3  ##########")
numeros.sort
print(numeros)

print("\n##########Punto 4  ##########")
print(len(numeros))

print("\n##########Punto 5 ##########")
buscar = int(input("Que numero desea buscar ? "))
for numero in numeros :
    if numero is buscar:
        print(f"Se ha encontrado en la posicion {numeros.index(numero)}")

