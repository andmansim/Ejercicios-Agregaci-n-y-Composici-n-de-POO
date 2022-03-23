class Casa: #tiene paredes
    def __init__(self):
        pass

class Pared: #La pared contiene ventanas
    def __init__(self, nombre):
        self.nombre = nombre
        self.ventana = [] 
        
    def añadir_ventanas(self, v):
        self.ventana.append(v)
    
    def devolver(self):
            return self.ventana

class Ventana:
    def __init__(self, superficie):
        self.superficie = superficie

#Orientación de las paredes
p_n = Pared("pared norte")
p_s = Pared("pared sur")
p_e = Pared("pared este")
p_o = Pared("pared oeste")

#Superficies de las ventanas
v_n = Ventana (3)
v_s = Ventana (5)
v_e = Ventana (7)
v_o = Ventana (0.3)

#asociamos a cada pared con una ventana y su superficie
p_n.añadir_ventanas(v_n)
p_s.añadir_ventanas(v_s)
p_e.añadir_ventanas(v_e)
p_o.añadir_ventanas(v_o)

