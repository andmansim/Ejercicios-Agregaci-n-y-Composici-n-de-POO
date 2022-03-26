class Ciudades:
    def __init__(self, nombre):
        self.nombre = nombre # NY, LA
        self.l_edif = [] #lista donde guardamos los edificios que pertenecen a una ciudad
        
    def añadir_edificios(self, edificio):
        self.l_edif.append(edificio)
        
    def devolver(self):
        return self.l_edif
    
class Edificios:
    def __init__(self, nomEdif, ciudad):
        self.nomEdif = nomEdif # A, B, C
        self.ciudad = ciudad
        ciudad.Edificios.append(nomEdif) 


class Empresa: #me crea los atributos para luego guardármelos fuera
    def __init__(self, nomEmpr):
        self.nomEmpr = nomEmpr # Nombre de la empresa (Yoohoo)
        self.l_empl = [] #lista de los empleados
        self.l_edificios = [] #lista que contiene todos los edificios de la empresa

class Empleados: #clase que nos crea los atributos asociados a los nombres de los empleados
    def __init__(self, nomEmpl, empre):
        self.nomEmpl = nomEmpl
        self.empre = empre

#Empresa
empresa = Empresa("Yoohoo")
       
#Empleados
emp1 = Empleados("Martin", empresa)
emp2 = Empleados("Salim", empresa)
emp3 = Empleados("Xing", empresa)     


#Edificios
edif1 = Edificios("A", empresa)
edif2 = Edificios("B", empresa)
edif3 = Edificios("C", empresa)




#Ciudad
ciudad1 = Ciudades("NY")
ciudad2 = Ciudades("Los Ángeles")
ciudad1.añadir_edificios(edif1) # nos añade a NY A
ciudad1.añadir_edificios(edif2) # nos añade a NY B
ciudad2.añadir_edificios(edif3) # nos añade a LA C

