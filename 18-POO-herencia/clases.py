

class Persona:
    
    def getNombre(self):
        return self.nombre
    def setNombre(self, nombre):
        self.nombre=nombre
    
    def getApellido(self):
        return self.apellido
    def setApellido(self, apellido):
        self.apellido= apellido
    
    def getAltura(self):
        return self.altura
    def setAltura(self,altura):
        self.altura = altura
    
    def getEdad(self):
        return self.edad
    def setEdad(self, edad):
        self.edad = edad
    
    def hablar(self):
        return "Estoy hablando"
    
    def caminar(self):
        return "Estoy caminando"
    
    def dormir(self):
        return "Estoy durmiendo"

class Informatico(Persona):
    
    def __init__(self):
        self.experiencia = 5
        self.leguanjes = "HTML, CSS, JAVASCRIPT, PHP"
    
    def getLenguajes(self):
        return self.leguanjes
    def setLenguajes(self, lenguajes):
        self.leguanjes+= ", " + lenguajes
    
    def programar(self):
        return "Estoy programando"
    
    def repararPC(self):
        return "He reparado tu PC"

class TecnicoRedes(Informatico):
    
    def __init__(self):
        super().__init__()
        self.auditarRedes= "experto"
        self.experienciaRedes=15
    #En este constructor no tenemos las propiedades del objeto Informatico
    #para heredarlas necesitamos la funcion super
    
    def auditar(self):
        return "Estoy auditando una red"
