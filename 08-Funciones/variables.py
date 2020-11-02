"""

Variables Locales : Se definen dentro de la funcion y no se puede usar
fuera de ellas, solo estan disponible dentro. A no ser que hagamos return

Variable Globales : Son las que se declaran fuera de una funcion y estan
disponobles dentro y fuera de ellas

"""

#Variable Globales
frase = " DE mi para ti y de tu pa mi"

print(frase)
website = ""

def holaMundo():
    frase = " Hola mundo"
    print (frase)
    
    year = 2021
    print(year)
    
    
    website = "rubendeveloper.com"
    print(f"Dento {website}")
    return "Dato devuelto " + str(year)

holaMundo()
print(f"fuera{website}")