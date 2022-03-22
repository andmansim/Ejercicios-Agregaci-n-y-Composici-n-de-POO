class Ciudades:
    def __init__(self, nombre):
        self.nombre = nombre # NY, LA
        self.l_edif = [] #lista donde guardamos los edificios que pertenecen a una ciudad
        return self.l_edif

class Edificios:
    def __init__(self, nomEdif):
        self.nomEdif = nomEdif # A, B, C
        return self.nomEdif
        

class Empresa:
    def __init__(self, nomEmp, l_empl, l_edificios):
        self.nomEmp = nomEmp # Nombre de la empresa (Yoohoo)
        self.l_empl = l_empl #lista de los empleados
        self.edificio = []
        self.empleados = ['Martin', 'Salim', 'Xing']
        

edificio = (Edificios() for i in range (2))
ciudad = Ciudades("NY")
ciudad.edificio = edificio
for j in edificio: 
    j.ciudad = ciudad

print(ciudad.nombre, edificio.ciudad[0])