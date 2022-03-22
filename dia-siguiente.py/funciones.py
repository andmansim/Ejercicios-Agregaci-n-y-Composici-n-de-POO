class Ciudades:
    def __init__(self, nombre):
        self.nombre = nombre # NY, LA
        self.l_edif = [] #lista donde guardamos los edificios que pertenecen a una ciudad
        return self.l_edif

class Edificios:
    def __init__(self, nomEdif):
        self.nomEdif = nomEdif # A, B, C
        return self.nomEdif
        

class Empresa: #me crea los atributos para luego guardármelos fuera
    def __init__(self, nomEmpr, l_empl, l_edificios):
        self.nomEmp = nomEmpr # Nombre de la empresa (Yoohoo)
        self.l_empl = l_empl #lista de los empleados
        self.l_edificios = l_edificios #lista que contiene todos los edificios de la empresa

class Empleados: #clase que nos crea los atributos asociados a los nombres de los empleados
    def __init__(self, nomEmpl):
        self.nomEmpl = nomEmpl

emp1 = Empleados("Martin")
emp2 = Empleados("Salim")
emp3 = Empleados("Xing")     
lista_empleados = [emp1, emp2, emp3]
print(lista_empleados)
        