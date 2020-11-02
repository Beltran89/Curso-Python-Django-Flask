#Import
import sqlite3

#Conexion
conexion = sqlite3.connect('./19-base-datos/pruebas.db')

#Crear cursor
cursor =  conexion.cursor()

#Crear tabla
cursor.execute("CREATE TABLE IF NOT EXISTS productos("+
"id INTEGER PRIMARY KEY AUTOINCREMENT, "+
"titulo varchar(255), "+
"descripcion text, "+
"precio int(255)"+
")")

#Guardar cambios
conexion.commit()

#Introducir datos
"""
cursor.execute("INSERT INTO productos VALUES(null,'Primer producto','Descripcion de mi producto', 550)")
conexion.commit()
"""

'''
#Borrar 
cursor.execute("DELETE FROM productos")
conexion.commit()
'''

#Insertar varios datos
productos = [
    ("ordenador Protatil", "buen pc", 700),
    ("Telefono movil", "buen telefono", 140),
    ("Palca base", "buen placa", 80),
    ("tablet", "buen tablet", 300),
]

cursor.executemany("INSERT INTO productos Values(null, ?, ?, ?)", productos)
conexion.commit()


#Actualizar datos de tuplas (update)
cursor.execute("UPDATE productos SET precio = 123 WHERE precio = 80")
conexion.commit()

#Lectura datos
cursor.execute("SELECT * FROM productos WHERE precio >= 100")

productos = cursor.fetchall()


for producto in productos:
    print("Id : " , producto[0])
    print("Titulo : " , producto[1])
    print("Descripcion : ", producto[2])
    print("Precio : " , producto[3], "\n")


cursor.execute("SELECT TITULO FROM productos")
producto = cursor.fetchone()
print(producto)


#Cerrar conexion
conexion.close

