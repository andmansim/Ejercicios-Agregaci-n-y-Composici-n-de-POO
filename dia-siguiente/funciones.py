class Ciudades:
    def __init__(self, nombre):
        self.nombre = nombre # NY, LA
        self.l_edif = [] #lista donde guardamos los edificios que pertenecen a una ciudad
        
    
class Edificios:
    def __init__(self, nomEdif, empr, ciudad):
        self.nomEdif = nomEdif # A, B, C
        if ciudad == None:
            self.Empresa = empr
            empr.l_edificios.append(nomEdif) 
            
        if empr == None:
            self.Ciudades = ciudad
            ciudad.l_edif.append(nomEdif) 


class Empresa: #me crea los atributos para luego guardármelos fuera
    def __init__(self, nomEmpr):
        self.nomEmpr = nomEmpr # Nombre de la empresa (Yoohoo)
        self.l_empl = [] #lista de los empleados
        self.l_edificios = [] #lista que contiene todos los edificios de la empresa

class Empleados: #clase que nos crea los atributos asociados a los nombres de los empleados
    def __init__(self, nomEmpl, empre):
        self.nomEmpl = nomEmpl
        self.Empresa = empre
        empre.l_empl.append(nomEmpl)


#Ciudades
ciudad1 = Ciudades("NY")
ciudad2 = Ciudades("Los Ángeles")

#Empresa
empresa = Empresa("Yoohoo")
       
#Empleados de la empresa
emp1 = Empleados("Martin", empresa)
emp2 = Empleados("Salim", empresa)
emp3 = Empleados("Xing", empresa)     


#Edificios de la empresa
edif1 = Edificios("A", empresa, None)
edif2 = Edificios("B", empresa, None)
edif3 = Edificios("C", empresa, None)

#Edificios en las ciudades
edif_1 = Edificios("A", None, ciudad1)
edif_2 = Edificios("B", None, ciudad1)
edif_3 = Edificios("C",  None, ciudad2)

def destruirCiudades(objeto):
    print("¿Quiere destruir " + objeto.nombre + " ? Y/N")
    usuario = input()
    borrarciudad = objeto.nombre
    e = ""
    if usuario == "Y":
        for i in range(len(objeto.l_edif)):
            e = objeto.l_edif[i - 1]
            del objeto.l_edif[i - 1]
            print("Se ha destruido el edificio " + e + " de la ciudad " + borrarciudad)
        del objeto
        print("Se ha destruido toda la ciudad de " + borrarciudad)
        
    elif usuario == "N":
        print("Perfecto, gracias por no destruir "+ objeto.nombre)   
    else:
        print("Esa opción no es válida, por favor intentelo de nuevo")