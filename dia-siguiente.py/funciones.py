class Ciudades:
    def __init__(self, nombre):
        self.nombre = nombre
        

class Edificios(Ciudades):
    def __init__(self, nombre, nomEdif):
        super().__init__(nombre)
        self.nomEdif = nomEdif
        

class Empresa(Edificios):
    def __init__(self, NY, LAS, A, B, C, empleados):
        super().__init__(NY, LAS, A, B, C)
        self.empleados = empleados
        
        self.empleados = ['Martin', 'Salim', 'Xing']
        
ciudad = Ciudades("NY")
ciudad1 = Ciudades("LAS")
edificio = Edificios()
empresa = Empresa()

class destruccion_NY(Edificios):
    def __init__(self, NY, LAS, A, B, C):
        super().__init__(NY, LAS, A, B, C)
    def __del__(self):
        Ciudades.remove(self.NY)
        Edificios.remove(self.A, self.B)