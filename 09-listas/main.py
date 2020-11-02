'''
LISTAS (Arrays)
Son colecciones o conjuntos de datos/valores, bajo
un unico nombre
Para acceder a esos valores podemos usar un indeice númerico
'''

pelicula = "Batman"

#Definir lista
peliculas = ["Batman", "Spiderman", "Iron man"]
cantantes = list(("2pac", "Tote King", "Morodo", "RapsusKley"))
años = list(range(2020,2050))
variada = ["Ruben",250, True, 4.4]

'''
print(peliculas)
print(cantantes)
print(años)
print(variada)
'''

#Indices
pelicula =  "Otra Cosa"
peliculas[1]= "Gran Torino"

print(peliculas)
print(peliculas[-2])
print(cantantes[1:3])#Datos entre el 1 y el 3 RapsusKley pertenece al 3 y no esta entre 1 y 3 

#Añadir Elementos a una lista
cantantes.append("Kase O")
print(cantantes)

#Recorrer Lista
'''
nueva_pelicula= ""
while nueva_pelicula != "parar":
    nueva_pelicula= input("Introduce Peliculas ")
    if nueva_pelicula != "parar":
        peliculas.append(nueva_pelicula)


print("******************* Listado PELICULAS ***************")
for pelicula in peliculas:
    print(f"{peliculas.index(pelicula)} - {pelicula}")

'''
# Lista Multidimensional 
print("\n******************* Lista Contactos  **********************")

contactos = [
    [
        "antonio",
        "antonio@lll.com"
    ],
    [
        "manolo",
        "manolo@djdjdjd.com"
    ],
    [
        "juan"
        "juan@sadasdas.com"
    ]
]

#print(contactos[1][0])

for contacto in contactos:
    print(contacto[0]) # Mostramos solo los nombres
    for elemento in contacto:
        print(elemento) #Nos muestra todos los datos nombre y correo