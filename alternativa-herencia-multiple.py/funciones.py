class Ventana:
    def __init__(self, v_norte, v_sur, v_este, v_oeste):
        self.v_norte = v_norte
        self.v_sur = v_sur
        self.v_este = v_este
        self.v_oeste = v_oeste
        
    

class Pared:
    def __init__(self, orientacion):
        self.orientacion = orientacion

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
ventana = Ventana (3, 5, 7, 0.3)

