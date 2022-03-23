class Casa: #tiene paredes
    def __init__(self):
        pass

class Pared: #La pared contiene ventanas
    def __init__(self, nombre):
        self.nombre = nombre
        self.ventana = [] 
        
    def añadir_ventanas(self, v):
        self.ventana.append(v)

class Ventana:
    def __init__(self, pared, superficie):
        self.pared = pared
        self.superficie = superficie
        
        


         


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

