
cantantes = ["kase o", "Morodo", "Rapsuskley", "haze"]
numeros = [1, 2, 32, 14, 8, 8, 8]

#Ordenar
print(numeros)
numeros.sort()
print(numeros)

#Añadir elementos
cantantes.append("Lirico")
cantantes.insert(1,"CPV")  #Posicion

print(cantantes) 

#Eliminar elementos
cantantes.pop(1) #eliminar por posicion
cantantes.remove("Lirico") #Eliminamos por nombre

print(cantantes)

#Dar la vuelta
numeros.reverse()
print(numeros)

#Buscar dentro de una lista
print("kase o" in cantantes)

#Contar elementos 
print(len(cantantes))

#Cuantas veces aparece un elemento en la lista
print(numeros.count(8))

#conseguir el indice
print(cantantes.index("haze"))

#unir dos listas
cantantes.extend(numeros)
print(cantantes)