"""
    Ejercicio 4 : Pedir dos numero al usuario y hacer todas las operaciones de una calculadora
    
"""

num_1 = int(input("Introduce numero 1 : "))
num_2 = int(input("Introduce numero 2 : "))

print(f"{num_1} + {num_2} = {num_1+num_2}")
print(f"{num_1} - {num_2} = {num_1-num_2}")
print(f"{num_1} * {num_2} = {num_1*num_2}")

if num_1>num_2:
    print(f"{num_1} / {num_2} = {num_1/num_2}")
    print(f"El resto es = {num_1%num_2}")
else:
    print("No se puede realizar operacion de division")
