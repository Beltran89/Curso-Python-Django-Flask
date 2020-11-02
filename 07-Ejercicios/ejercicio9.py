"""
Ejercicio 9 : hacer un programa que pida numeros indefinidamente hasta introducir el numero 111

"""
num = 0 

while num != 111:
    num = int(input("Introduzca numero "))
    if num != 111:
        print(num)