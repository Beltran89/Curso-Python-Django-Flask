import os,shutil



#Crear carpeta
if not os.path.isdir("./14-sistema-de-ficheros/mi_carpeta"):
    os.mkdir("./14-sistema-de-ficheros/mi_carpeta")
else:
    print("Ya exite el directorio")


'''
#Copiar
ruta_original = "./14-sistema-de-ficheros/mi_carpeta" 
ruta_nueva = "/14-sistema-de-ficheros/mi_carpeta_copiada"
shutil.copytree(ruta_original,ruta_nueva)

#Eliminar
os.rmdir("./14-sistema-de-ficheros/mi_carpeta_copiada")
'''

#Mostrar contenido
print("Contenido de mi carpeta : ")
contenido = os.listdir("./14-sistema-de-ficheros/mi_carpeta")
print(contenido)

for fichero in contenido:
    print("Fichero ",fichero)
