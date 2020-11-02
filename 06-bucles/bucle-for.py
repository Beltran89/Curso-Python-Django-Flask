"""
#FOR

for varible in elemento_iterable (listas,rango,etc)
    BLOQUE INSTRUCCIONES
    
"""

contador = 0 
resultado = 0

for contador in range(0,5):
    print(" Voy por el numero ", contador)
    
    resultado = resultado + contador


print(resultado)

#Ejemplo tabla de multiplicar
print("\n########   EJMEPLO TABLAS X #######")

numero_user =  int(input("¿Que numero deseas multiplicar ? "))
if numero_user > 0:
    print("TABLA DE MULTIPLICAR DEL NUMERO " f"{numero_user}")
    for numero in range(0,11):
        resultado = numero_user * numero
        print(f"{numero_user} X {numero} = ", resultado)
    print("Tabla finalizada {}".format(numero_user))
else:
    print("Numero no valido")
