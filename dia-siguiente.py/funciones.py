class Ciudades:
    def __init__(self, nombre):
        self.nombre = nombre
        self.edificio = [] #los edificios que pertenecen a una ciudad

class Edificios:
    def __init__(self, nomEdif):
        self.nomEdif = nomEdif
        self.ciudad = None
        

class Empresa:
    def __init__(self, empleados):
        self.empleados = empleados
        self.edificio = []
        self.empleados = ['Martin', 'Salim', 'Xing']
        

edificio = (Edificios() for i in range (2))
ciudad = Ciudades("NY")
ciudad.edificio = edificio
for j in edificio: 
    j.ciudad = ciudad

print(ciudad.nombre, edificio.ciudad[0])
'''empresa = Empresa()

class destruccion_NY(Edificios):
    def __init__(self, NY, LAS, A, B, C):
        super().__init__(NY, LAS, A, B, C)
    def __del__(self):
        Ciudades.remove(self.NY)
        Edificios.remove(self.A, self.B)'''