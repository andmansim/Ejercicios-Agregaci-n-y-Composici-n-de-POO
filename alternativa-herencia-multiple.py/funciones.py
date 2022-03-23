class Ventana:
    def __init__(self, orientacion):
        self.orientacion = orientacion
        self.superficie = []
        
    def añadir_orientacion(self, orientacion):
        self.l_edif.append(edificio)
        
    def devolver(self):
        return self.l_edif  
        

class Pared:
    def __init__(self, nombre):
        self.nombre = nombre
        
    def devolver (self):
        return self.nombre   
         
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
v_n = Ventana (3)
v_s = Ventana (5)
v_e = Ventana (7)
v_o = Ventana (0.3)

casa = Casa(v_n, p_n )

