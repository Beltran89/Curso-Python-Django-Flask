"""
SET es un tipo de dato, para tener una coleccion de valores,
pero no tiene ni indice ni orden

"""

personas = {
    "Victor",
    "Ruben",
    "Paco",
    "Manolo"
}
print(personas)
personas.remove("Paco")
personas.add("Pepe")
print(personas)