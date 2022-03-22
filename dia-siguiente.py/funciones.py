class Ciudades:
    def __init__(self, nombre):
        self.nombre = nombre # NY LA
        self.l_edif = [] #lista donde guardamos los edificios que pertenecen a una ciudad

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