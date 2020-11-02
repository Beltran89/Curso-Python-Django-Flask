"""

Ejercicio 7: Mostrar numeros pares entre dos numeros que elija el usuario


"""

num_1= int(input("Primer numero : "))
num_2= int(input("Segundo numero : "))

if num_1 < num_2:
    for num in range(num_1, num_2 + 1):
        if num%2 == 0:
            print(num)
else:
    for num in range(num_2, num_1 + 1):
        if num%2 == 0:
            print(num)