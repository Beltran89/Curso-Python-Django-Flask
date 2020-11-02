"""
Modulos : son funcionalidades ya hechas para reutilizar

En python hay modulos, que los puedes consultar aqui:
https://docs.python.org/3/py-modindex.html

"""

from miModulo import * #Con from miModulo import holaMunod, importamos solo ese metodo

# print(miModulo.holaMundo("ruben"))   #Llamamos a la funcion de otro modulos ****OJO ***** ESTA SOLO VALE
#CON import miModulo



print(holaMundo("ruben"))
print(suma(2,2))


# Modulo fecha

import datetime

print(datetime.date.today())

fecha_completa = datetime.datetime.now()
print(fecha_completa)
print(fecha_completa.year)
print(fecha_completa.month) 
print(fecha_completa.day)

fecha_personalizada = fecha_completa.strftime("%d/%m/%Y,%H:%M")
print(fecha_personalizada)