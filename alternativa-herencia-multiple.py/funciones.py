class Ventana:
    def __init__(self, pared, superficie):
        self.pared = pared
        self.superficie = superficie
        

class Pared:
    def __init__(self, nombre):
        self.nombre = nombre
         
         
class Casa(Ventana, Pared):
    def __init__(self, superficie, orientacion):
        Ventana.__init__(self, superficie)
        Pared.__init__(self, orientacion)
        
    def superficie(self):
        #suma = Ventana.superficie
        suma = v_n + v_s + v_e + v_o
        return suma 

#Orientación de las paredes
p_n = Pared("pared norte")
p_s = Pared("pared sur")
p_e = Pared("pared este")
p_o = Pared("pared oeste")

#Superficies de las ventanas
v_n = Ventana (p_n, 3)
v_s = Ventana (p_s, 5)
v_e = Ventana (p_e, 7)
v_o = Ventana (p_o, 0.3)

casa = Casa(v_n, p_n )

