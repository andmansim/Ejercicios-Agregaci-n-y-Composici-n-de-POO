class Casa: #tiene paredes
    def __init__(self, pared1, pared2, pared3, pared4):
        self.pared1 = pared1
        self.pared2 = pared2
        self.pared3 = pared3
        self.pared4 = pared4
      
    def sumar(self):
        #abrimos cada objeto para obtener loa atributos asociados a ellos
        suma = 0
        for v in self.pared1.ventana1:
            suma = suma + v.superficie
        for v in self.pared2.ventana1:
            suma = suma + v.superficie       
        for v in self.pared3.ventana1:
            suma = suma + v.superficie
        for v in self.pared4.ventana1:
            suma = suma + v.superficie
            
        return suma

class Pared: #La pared contiene ventanas
    def __init__(self, nombre):
        self.nombre = nombre
        self.ventana1 = [] 

class Ventana:
    def __init__(self, pared, superficie, proteccion):
        self.pared = pared
        self.superficie = Cristal(superficie) #llamamos a la clase Cristal para que coja de ahí superficie
        self.proteccion = proteccion
        self.pared.ventana1.append(self)

class ParedCortina(Pared, Ventana):
    def __init__(self, nombre, superficie):
        Pared.__init__(self, nombre)
        Ventana.__init__(self, self, superficie, proteccion = 0) #tiene otro self, porque el atributo pared es lo mismo que en Pared el atributo nombre
#En Ventana.__init__(....) ponemos proteccion = 0, para que no nos pida ese atributo en ParedCortina, dado que no lo necesitamos

#nueva clase con los elementos en común entre la clase Ventana y ParedCortina
class Cristal:
    def __init__(self, superficie):
        self.superficie = superficie
    
    def devolver(self):
        return self.superficie