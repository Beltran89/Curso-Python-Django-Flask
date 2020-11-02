class Coche:
    
    soy_publico= "Hola, soy publico"
    __soy_privado = "Hola soy privado"
    #contructor
    def __init__(self, color, marca, modelo, velocidad, cv, plazas):
        self.color= color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.cv = cv
        self.plazas = plazas 
        
    #Metodos
    
    def acelerar(self):
        self.velocidad += 1
    def frenar(self):
        self.velocidad -= 1
    
    def getVelocidad(self):
        return self.velocidad
    def getMarca(self):
        return self.marca

    def SetMarca(self,marca):
        self.marca=marca
    
    def setColor(self,color):
        self.color=color
    
    def getColor(self):
        return self.color
    
    def setModelo(self,modelo):
        self.modelo = modelo
    
    def getModelo(self):
        return self.modelo
    
    def getInfo(self):
        info = "--- Info Coche -----"
        info += "\n Color : "+ self.getColor()
        info += "\n Marca: "+ self.getMarca()
        info += "\n Modelo : "+ self.getModelo()
        info += "\n Velocidad : "+ str(self.getVelocidad())
        
        return info 
    def getSoy_privado(self):
        return self.__soy_privado