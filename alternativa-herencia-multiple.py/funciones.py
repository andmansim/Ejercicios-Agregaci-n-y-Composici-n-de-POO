class Ventana:
    def __init__(self, v_norte, v_sur, v_este, v_oeste):
        self.v_norte = v_norte
        self.v_sur = v_sur
        self.v_este = v_este
        self.v_oeste = v_oeste
        
class Pared:
    def __init__(self, p_norte, p_sur, p_este, p_oeste):
        self.p_norte = p_norte
        self.p_sur = p_sur
        self.p_este = p_este
        self.p_oeste = p_oeste

class Casa(Ventana, Pared):
    def __init__(self, p_norte, p_sur, p_este, p_oeste, v_norte, v_sur, v_este, v_oeste):
        Ventana.__init__(self, v_norte, v_sur, v_este, v_oeste)
        Pared.__init__(self, p_norte, p_sur, p_este, p_oeste)
        
    def superficie(self):
        suma = self.v_norte + self.v_sur + self.v_este + self.v_oeste
        return suma 


casa = Casa("pared norte", "pared sur", "pared este", "pared oeste", 3, 5, 7, 0.3)
print("La superficie acristalada es:")
print( casa.superficie())