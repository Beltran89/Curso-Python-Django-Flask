#Programacion orientada a objetos (POO o OOP)

#Definir una clase

class Coche:
    
    #Atributos o propiedades
    color = "Rojo"
    marca = "Ferrari"
    modelo = "Aventator"
    velocidad = 300
    caballaje = 500
    plazas = 2 
    
    #Metodos
    
    def acelerar(self):
        self.velocidad += 1
    def frenar(self):
        self.velocidad -= 1
    
    def getVelocidad(self):
        return self.velocidad
    
    def setColor(self,color):
        self.color=color
    
    def getColor(self):
        return self.color
    
    def setModelo(self,modelo):
        self.modelo = modelo
    
    def getModelo(self):
        return self.modelo




coche = Coche()

coche.setColor("Verde")
coche.setModelo("F40")
print(coche.getColor(), coche.getModelo())
print(type(coche))