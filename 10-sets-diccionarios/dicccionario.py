"""
Diccionario:
Un tipo de dato que almacena un conjunto de datos.
En formato clave > valor
Es un parecido a un array asiciativo o un objeto Json
"""

personas = {
    "nombre":"Ruben",
    "apellido":"beltran",
    "edad":31
}

print(personas["nombre"]) #Para ver el valor de key nombre


# Lista con diccionarios

contactos = [
    {
        "nombre" : "Ruben",
        "email" : "ruben@ruben.es"
    },
    {
        "nombre" : "Luis",
        "email" : "luis@luis.com"
    },{
        "nombre" : "manolo",
        "email" : "manolo@rmanoño.es"
    }
]
print(contactos[1]["nombre"])
contactos[1]["nombre"] = "Luisito"
print(contactos[1]["nombre"])

for contacto in contactos:
    print("Nombre :" + contacto["nombre"])  # print(f"Nombre : + {contacto["nombre"]}") Tambien valdria
    print("Email :" + contacto["email"] + "\n")