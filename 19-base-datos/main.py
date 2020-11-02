import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="master_python"
)

#La conexion ha sido correcto??
print(database)

#Cursor 
cursor= database.cursor()

'''
#crear base Datos
cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")

cursor.execute("SHOW DATABASES")

for db in cursor:
    print(db)
'''

#Crear tabla

cursor.execute("""
CREATE TABLE IF NOT EXISTS vehiculos(
    id int(10) auto_increment not null,
    marca varchar(40) not null,
    modelo varchar(40) not null,
    precio float(10,2) not null,
    CONSTRAINT pk_vehiculo PRIMARY KEY(id)
)
""")

#Ver si existe la tabla sin acceder a PhpMyAdmin
'''cursor.execute("SHOW TABLES")
for tb in cursor:
    print(tb)
'''

#Introducir datos
'''
cursor.execute("INSERT INTO vehiculos VALUES(null,'Opel','Zafira',13500)")
database.commit()

cursor.execute("SELECT * FROM vehiculos")

for vh in cursor:
    print(vh)
'''

#Introducir datos multiples
coches = [
    ("Renault", "Megane",15000),
    ("BMW", "320", 25000),
    ("Hyundai", "I30 N", 31000)
]
'''
cursor.executemany("INSERT INTO vehiculos VALUES(null,%s,%s,%s)",coches)
database.commit()
'''

cursor.execute("SELECT * FROM vehiculos")
resultado = cursor.fetchall()

for vh in resultado:
    print(vh)
