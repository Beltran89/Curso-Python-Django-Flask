'''
Proyecto Python y Mysql:
- Abrir asistente
- Login o registro
- Si elegimos registro, creara un nuevo usuario
- Si elejimos login, identificara y nos preguntara
- Crear nota, mostrar, borrar

'''

from usuarios import acciones

print("""
Acciones disponibles:
    - registro
    - login
""")
hazEl= acciones.Acciones()
accion = input("¿Que deseas hacer? ")

if accion == "registro":
    
    hazEl.registro()

elif accion == "login":
    hazEl.login()
    