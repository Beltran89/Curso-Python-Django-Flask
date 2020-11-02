# Entrada

nombre = input ("¿Cual es tu nombre?: ")
edad = input("¿Cual es tu edad?: ")



# Salida

print ("Bienvenido {}!".format(nombre))

if (int(edad) >= 18):
    print("Eres mayor de edad ")
else:
    print("Eres menor")