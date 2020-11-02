from coche import Coche

carro =  Coche("Negro", "Renault", "Megane", 200, 130, 5)
carro2 =  Coche("Azul", "Seat", "Leon", 250, 200, 4)
carro3 =  Coche("Rojo", "Citroen", "Ds", 180, 100, 5)
carro4 =  Coche("Blanco", "Mercedes", "CLA", 210, 140, 2)



print(carro.getInfo())
print(carro2.getInfo())
print(carro3.getInfo())
print(carro4.getInfo())


#Detectar tipado
if type(carro2) == Coche:
    print("Es un objeto correcto")
else:
    print("Es un no objeto correcto")

print(carro2.getSoy_privado())