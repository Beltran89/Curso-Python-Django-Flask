from io import open
import pathlib # Saber ruta alternativa
import shutil # Copiar y remplazar
import os #eliminar

ruta = str(pathlib.Path().absolute()) +"/14-sistema-de-ficheros/fichero_texto.txt"
#print(ruta)
archivo = open(ruta,"r")
#archivo = open("/14-sistema-de-ficheros/fichero_texto.txt","r")

#Escribir archivo
#archivo.write("******* Soy un texto metido en Python")


#Leer Archivo
contenido =archivo.readlines()  # en el open propiedad "r"(read)
archivo.close()

for elemento in contenido:
    print(elemento)

#Copiar 
'''
ruta_original = str(pathlib.Path().absolute()) +"/14-sistema-de-ficheros/fichero_texto.txt" 
ruta_nueva = str(pathlib.Path().absolute()) +"/14-sistema-de-ficheros/fichero_copiado.txt"
ruta_alternativa = str(pathlib.Path().absolute()) +"./06-bucles/fichero_copiado_alternativo.txt"
shutil.copyfile(ruta_original,ruta_nueva)
shutil.copyfile(ruta_original,ruta_alternativa)
'''

#Mover
'''
ruta_original = str(pathlib.Path().absolute()) +"/14-sistema-de-ficheros/fichero_copiado.txt"
ruta_nueva = str(pathlib.Path().absolute()) +"/14-sistema-de-ficheros/fichero_copiado_nuevo.txt"  

shutil.move(ruta_original,ruta_nueva)
'''

#Eliminar
'''
ruta_nueva = str(pathlib.Path().absolute()) +"/14-sistema-de-ficheros/fichero_copiado_nuevo.txt"
os.remove(ruta_nueva)
'''

#Compobar si exite
print(os.path.abspath("./"))

if os.path.isfile(os.path.abspath("./")+"/14-sistema-de-ficheros/fichero_texto.txt"):
    print("El fichero existe")
else:
    print("El fichero no existe")