"""

#Operadores de comparacion
== igual
!= diferente
< menor que
> mayor que
<= menor o igual que
>=mayor o igual quew

#Operadores Logicos:
and y
or O
! Negacion
not no

"""

print("######   EJEMPLO 1  ########")
color = "rojo"

if color is "rojo":
    print("Es rojo")
else:
    print("No es rojo") 

print("\n######   EJEMPLO 2  ########")


#year = 2020

year = int(input("Introduce un año : "))
if year <= 2021:
    print("En menor o igual a 2021")
else:
    print("es mayor de 2021")

#If anidados
print("\n######   EJEMPLO 3 ########")

nombre = "Rubén Beltrán"
ciudad = "Madrid"
continente = "Europa"
edad = 31 
mayoria_edad = 18 

if edad >= mayoria_edad:
    print(f"{nombre} Es mayor de edad")
    
    if continente != "Europa":
        print("El user no Europeo")
    else:
        print("El user es Europeo")
else:
    print(f"{nombre} No es mayor de edad")


print("\n######   EJEMPLO 4 ########")

dia = int(input("Introduce dia de la Semana :  "))

if dia is 1:
    print("Es lunes")
elif dia is 2:
    print("Es martes")
elif dia is 3:
    print("Es miercoles")
elif dia is 4:
    print("Es jueves")
elif dia is 5:
    print("Es viernes")
else:
    print("Es finde ")

#Operadoredores logicos
print("\n######   EJEMPLO 5 ########")

edad_minima = 18
edad_maxima =65
edad_oficial = 17

if edad_oficial >= edad_minima and edad_oficial <= edad_maxima:
    print("Estas en edad de trabajar")
else:
    print("No estas en edad de trabajar")


print("\n######   EJEMPLO 6 ########")
pais= "Alemania"

if pais is "Mexico" or pais is "Colombia" or pais is "España":
    print(f"{pais} Es un pais de habla Hispana")
else:
    print(f"{pais} No es un pais de habla Hispana")
