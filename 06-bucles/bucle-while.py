"""
# BUCLE WHILE
Estructura de control que itera o repite la ejecuacion de una 
serie de instrucciones tantas veces como sea necesario, 
hasta quqe deje de cumplirse la condiciones 

"""

contador = 1 

while contador <= 20:
    print("Estoy en el contador ", contador)
    contador += 1

print("### EJEMPLO TABLA DE MULTIPLICAR ###")

numero_usuario = int(input("Introduzca numero : "))

if numero_usuario <= 0:
        numero_usuario= 1

contador = 0

while contador <= 10:
    print(f"{numero_usuario}  X  {contador} = {numero_usuario*contador}")
    contador+=1
