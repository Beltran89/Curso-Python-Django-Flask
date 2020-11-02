"""
Ejercicio 3 
    -Escribir un programa que muestre los cuadrados de los 60 primero numeros
"""

for numero in range(1,61):
    print(f"{numero} al cuadrado en for = {numero*numero}")
    
numero_while=1

while numero_while <= 60: 
    print(f"{numero_while} al cuadrado en While = {numero_while*numero_while}")
    numero_while += 1