"""

Una variable es un contenedor de informacion 
que dentro guardara un dato, se puede crear 
muchas varibales y que cada una tenga un dato distinto

"""
texto= "Master en Python"
texto2="Alumno Rubén"
numero =45
decimal=6.7

print(texto)
print(texto2)
print(numero)
print(decimal)

numero =5
decimal=15.7

print("#################")
print(numero)
print(decimal)

print("#################")

# Concatenacion
print(texto+" " + texto2 + str(numero))
print(f"{texto}                 {texto2}")

nombre= "Ruben"
apellido = "beltran"
edad = 31
print("mi nombre es {} mi apellido {} y mi edad {}".format(nombre,apellido, edad))