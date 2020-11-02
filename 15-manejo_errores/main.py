# Manejar errores y manejar excepciones
'''
try:
    nombre  = input(" Cual es tu nombre : ")
    print(nombre)

    if len(nombre)> 1 :
        nombre_user = "Su nombre es " + nombre

    print(nombre_user)

except:
    print("introduce bien el nombre ")

else:
    print("todo funciono correcto")

finally:
    print("Fin de la iteracion")
'''

#Multiples excepciones
'''
try:
    numero  = int(input("Numero para elevar al cuadrado "))
    print("El cuadrado es " + str(numero*numero))
    
except TypeError:
    print("debes convertir tus cadenas a enteros")
#except ValueError:
#    print("introduce dato correcto")
except Exception as e:
    print (" Ha ocurrido el error ", type(e).__name__)
'''

# Excepciones Personalizadas o lanzar excepciones:
try:
    nombre = input(" Introuce tu Nombre: ")
    edad = int(input(" Introduce edad "))

    if edad < 5 or edad > 110:
        raise ValueError("La edad introducida no es real")
    elif len(nombre)<=1:
        raise ValueError("EL nombre no es completo")
    else:
        print(f"Bienvenido {nombre} al curso ")
except ValueError:
    print("Intoduce los datos correctamente")