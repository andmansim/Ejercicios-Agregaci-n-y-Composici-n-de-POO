class Ciudades:
    def __init__(self, NY, LAS):
        self.NY = NY
        self.LAS = LAS

class Edificios(Ciudades):
    def __init__(self, NY, LAS, A, B, C):
        super().__init__(NY, LAS)
        self.A = A
        self.B = B
        self.C = C

