class Ciudades:
    def __init__(self, nombre):
        self.nombre = nombre # NY, LA
        self.l_edif = [] #lista donde guardamos los edificios que pertenecen a una ciudad
        
    
class Edificios:
    def __init__(self, nomEdif, ciudad):
        self.nomEdif = nomEdif # A, B, C
        self.Ciudades = ciudad
        ciudad.l_edif.append(nomEdif) 


class Empresa: #me crea los atributos para luego guardármelos fuera
    def __init__(self, nomEmpr):
        self.nomEmpr = nomEmpr # Nombre de la empresa (Yoohoo)
        self.l_empl = [] #lista de los empleados
        #self.l_edificios = [] #lista que contiene todos los edificios de la empresa

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
edif1 = Edificios("A", empresa)
edif2 = Edificios("B", empresa)
edif3 = Edificios("C", empresa)

#Edificios en las ciudades
edif_1 = Edificios("A", ciudad1)
edif_2 = Edificios("B", ciudad1)
edif_3 = Edificios("C", ciudad2)

def destruirCiudades(objeto):
    print("¿Quiere destruir " + objeto.nombre + " ? Y/N")
    usuario = input()
    borrarciudad = objeto.nombre
    if usuario == "Y":
        for i in range(len(objeto.l_edif)):
            e = objeto.l_edif[i - 1]
            del e
            print("Se ha destruido el edifico " + e + " de la ciudad " + borrarciudad)
        del objeto
        print("Se ha destruido toda la ciudad de " + borrarciudad)
        
    elif usuario == "N":
        print("Perfecto, gracias por no destruir "+ objeto.nombre)   
    else:
        print("Esa opción no es válida, por favor intentelo de nuevo")