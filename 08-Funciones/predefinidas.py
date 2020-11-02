nombre = "Ruben Beltran"

#funciones generales
print(type(nombre))

#detectar el tipado
comprobar = isinstance(nombre,str)

if comprobar :
    print("Esa varibale no es un String")
else:
    print("no es cadena")

if not isinstance(nombre, float):
    print("La variable no es un numero")

# Limpiar Espacios 
frase = "   mi contenido    "
print(frase)
print(frase.strip())  #Esta funcion limpia los espacios

#Eliminar variable

year = 2022
print(year)
del year
# print(year) #Salta error por no estar definida

# Comprobar variable
texto = "   ffff    "
if len(texto) <= 0:
    print("la variable esta vacia ")
else:
    print("La variabel contiene", len(texto))

#Encontrar caracteres
frase = "La vida es bella"
print(frase.find("vida")) #nos dice a partir de que caracter esta dicha palabra

# Remplazar palabra
nueva_frase = frase.replace("vida","moto")
print(nueva_frase)

# Mayusculas y minusculas
print(nombre)
print(nombre.lower())
print(nombre.upper())