"""
Ejercicio 6: Mostrar las tablas de multiplica del  1 al 10

"""

for numero in range(1,11):
    print(f"\nTabla del numero {numero}")
    
    for multi in range (0,11):
        print(f"{numero} X {multi} = {numero*multi}")
    