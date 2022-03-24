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
            suma = suma +   (v.superficie)
        for v in self.pared2.ventana1:
            suma = suma +   (v.superficie)        
        for v in self.pared3.ventana1:
            suma = suma +   (v.superficie)
        for v in self.pared4.ventana1:
            suma = suma +   (v.superficie)
            
        return suma

class Pared: #La pared contiene ventanas
    def __init__(self, nombre):
        self.nombre = nombre
        self.ventana1 = [] 

class Ventana:
    def __init__(self, pared, superficie):
        self.pared = pared
        self.superficie = superficie
        self.pared.ventana1.append(self)

#Orientación de las paredes
p_n = Pared("pared norte")
p_s = Pared("pared sur")
p_e = Pared("pared este")
p_o = Pared("pared oeste")

#Superficies de las ventanas
v_n = Ventana (p_n,3)
v_s = Ventana (p_s,5)
v_e = Ventana (p_e,7)
v_o = Ventana (p_o,0.3)

casa = Casa(p_n, p_s, p_e, p_o)

print(casa.sumar())


