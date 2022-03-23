class Ventana:
    def __init__(self, superficie):
        self.superficie = superficie

class Pared:
    def __init__(self, orientacion):
        self.orientacion = orientacion

class Casa(Ventana, Pared):
    def __init__(self, superficie, orientacion):
        Ventana.__init__(self, superficie)
        Pared.__init__(self, orientacion)

