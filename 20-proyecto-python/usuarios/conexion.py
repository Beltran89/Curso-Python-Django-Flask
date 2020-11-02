import mysql.connector

def conectar():
    
    database =  mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="master_python",
    )

    #print(database) "" ***** NOS SIRVE PARA VER SI HAY CONEXION  ******* """"
    cursor= database.cursor(buffered=True)
    
    return[database, cursor]
