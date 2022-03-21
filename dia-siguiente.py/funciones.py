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

class Empresa(Edificios):
    def __init__(self, NY, LAS, A, B, C, empleados):
        super().__init__(NY, LAS, A, B, C)
        self.empleados = empleados
        
        self.empleados = ['Martin', 'Salim', 'Xing']
        
ciudad = Ciudades()
edificio = Edificios()
empresa = Empresa()

class destruccion_NY(Edificios):
    def __init__(self, NY, LAS, A, B, C):
        super().__init__(NY, LAS, A, B, C)
    def __del__(self):
        Ciudades.remove(self.NY)
        Edificios.remove(self.A, self.B)