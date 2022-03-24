# Ejercicios-Agregaci-n-y-Composici-n-de-POO

Mi dirección de GitHub para este repositorio es la siguiente: [GitHub](https://github.com/andmansim/Ejercicios-Agregaci-n-y-Composici-n-de-POO.git)
https://github.com/andmansim/Ejercicios-Agregaci-n-y-Composici-n-de-POO.git

He realizado tres ejercicios, los cuales tratan de la agregación y la composición. Al igual que he resuelto varias preguntas en el segundo ejercicio.
El diagrama UML del primer ejercicio: El día siguiente, es:

![diagrama uml el dia siguiente](/dia-siguiente/el-dia-siguiente.jpg)


```
import funciones

if __name__ == "__main__":
    print("La empresa " + funciones.empresa.nomEmpr + " tiene sus instalaciones en las ciudades:")
    print(funciones.ciudad1.nombre)
    print(funciones.ciudad2.nombre)
    print("En " + funciones.ciudad1.nombre + " sus edicicios son:")
    print(funciones.ciudad1.l_edif.pop().devolver())
    print(funciones.ciudad1.l_edif.pop().devolver())
    print("En " + funciones.ciudad2.nombre + " su edicicio es:")
    print(funciones.ciudad2.l_edif.pop().devolver())
    print("Los empleados de " + funciones.empresa.nomEmpr + "son: ") 
    print(funciones.empresa.l_empl.pop().nomEmpl)
    print(funciones.empresa.l_empl.pop().nomEmpl)
    print(funciones.empresa.l_empl.pop().nomEmpl)
    
    print("¿Quiere destruir NY? Y/N")
    usuario = input()
    if usuario == "Y":
        del funciones.ciudad1.l_edif
        del funciones.ciudad1
        print(funciones.ciudad1)
        print("Se ha destruido toda la ciudad de NY")
        
    elif usuario == "N":
        print("Perfecto, gracias por no destruir NY")   
    else:
        print("Esa opción no es válida, por favor intentelo de nuevo")

class Ciudades:
    def __init__(self, nombre):
        self.nombre = nombre # NY, LA
        self.l_edif = [] #lista donde guardamos los edificios que pertenecen a una ciudad
        
    def añadir_edificios(self, edificio):
        self.l_edif.append(edificio)
        
    def devolver(self):
        return self.l_edif
    
class Edificios:
    def __init__(self, nomEdif):
        self.nomEdif = nomEdif # A, B, C
        
    def devolver (self):
        return self.nomEdif
        

class Empresa: #me crea los atributos para luego guardármelos fuera
    def __init__(self, nomEmpr, l_empl, l_edificios):
        self.nomEmpr = nomEmpr # Nombre de la empresa (Yoohoo)
        self.l_empl = l_empl #lista de los empleados
        self.l_edificios = l_edificios #lista que contiene todos los edificios de la empresa

class Empleados: #clase que nos crea los atributos asociados a los nombres de los empleados
    def __init__(self, nomEmpl):
        self.nomEmpl = nomEmpl
        
#Empleados
emp1 = Empleados("Martin")
emp2 = Empleados("Salim")
emp3 = Empleados("Xing")     
lista_empleados = [emp1, emp2, emp3]

#Edificios
edif1 = Edificios("A")
edif2 = Edificios("B")
edif3 = Edificios("C")
lista_edificio = [edif1, edif2, edif3]

#Empresa
empresa = Empresa("Yoohoo", lista_empleados, lista_edificio)

#Ciudad
ciudad1 = Ciudades("NY")
ciudad2 = Ciudades("Los Ángeles")
ciudad1.añadir_edificios(edif1) # nos añade a NY A
ciudad1.añadir_edificios(edif2) # nos añade a NY B
ciudad2.añadir_edificios(edif3) # nos añade a LA C
```
Segundo ejercicio: Inmortal

```
'''
Se muestra antes el signo de interrogación que el mensaje, porque solo pasa a la función
yang.__del__() cuando termina el programa o cuando se borran todos los objetos. Pero al haber un print("?")
justo depués del del(yang), entonces se imprimirá cuando ya haya impreso "?". Esto se debe a que tenemos dos objetos
idénticos, donde el del(yang) solo elimina yang, por tanto queda ying.yang que se elimina tras print("?")
'''

'''
Para resolver esto, la manera más fácil y obvia sería colocar el print("?") justo antes del del(yang). 
Otra manera sería destruir todos los objetos, los cuales serían yang y ying.yang. Así, si ponemos del(yang) y 
del(yin.yang) antes del print("?"), lo tendríamos.
'''
```

El diagrama UML del tercer ejercicio: La alternativa a la herencia múltiple, es:

![diagrama uml la alternativa](/alternativa-herencia-multiple/alternativa.jpg)

```
import funciones

if __name__ == "__main__":
    #Miramos la proteccion que quiere en las ventanas
    print("Seleccione una protección para cada una de las ventanas")
    print("Opciones: ")
    opciones = ["persiana", "estor", "cortinas", "mosquitera"]
    print(opciones)

    print("En la ventana norte, ¿qué protección quiere?")
    r_n = input()
    if r_n not in opciones:
        raise Exception("No se ha escogido ninguna proteccion de la lista")

    print("En la ventana sur, ¿qué protección quiere?")
    r_s = input()
    if r_s not in opciones:
        raise Exception("No se ha escogido ninguna proteccion de la lista")

    print("En la ventana este, ¿qué protección quiere?")
    r_e = input()
    if r_e not in opciones:
        raise Exception("No se ha escogido ninguna proteccion de la lista")

    print("En la ventana oeste, ¿qué protección quiere?")
    r_o = input()
    if r_o not in opciones:
        raise Exception("No se ha escogido ninguna proteccion de la lista")
        
        
    #Orientación de las paredes
    p_n = funciones.Pared("pared norte")
    p_s = funciones.Pared("pared sur")
    p_e = funciones.Pared("pared este")
    p_o = funciones.Pared("pared oeste")

    #Superficies de las ventanas
    v_n = funciones.Ventana (p_n,3, r_n)
    v_s = funciones.Ventana (p_s,5, r_s)
    v_e = funciones.Ventana (p_e,7, r_e)
    v_o = funciones.Ventana (p_o,0.3, r_o)


    casa = funciones.Casa(p_n, p_s, p_e, p_o)
    print(casa.sumar())
    
    pared_cortina = funciones.ParedCortina("pared sur", 10)
    casa.pared2 = pared_cortina
    print(casa.sumar())

class Casa: #tiene paredes
    def __init__(self, pared1, pared2, pared3, pared4):
        self.pared1 = pared1
        self.pared2 = pared2
        self.pared3 = pared3
        self.pared4 = pared4
      
    def sumar(self):
        #abrimos cada objeto para obtener loa atributos asociados a ellos
        suma = 0
        for v in self.pared1.ventana1:
            suma = suma + v.superficie
            
        for v in self.pared2.ventana1:
            suma = suma + v.superficie       
        for v in self.pared3.ventana1:
            suma = suma + v.superficie
        for v in self.pared4.ventana1:
            suma = suma + v.superficie
            
        return suma

class Pared: #La pared contiene ventanas
    def __init__(self, nombre):
        self.nombre = nombre
        self.ventana1 = [] 

class Ventana:
    def __init__(self, pared, superficie, proteccion):
        self.pared = pared
        cristal = Cristal(superficie)
        self.superficie = cristal.superficie #llamamos a la clase Cristal para que coja de ahí superficie
        self.proteccion = proteccion
        self.pared.ventana1.append(self)

class ParedCortina(Pared, Ventana):
    def __init__(self, nombre, superficie):
        Pared.__init__(self, nombre)
        Ventana.__init__(self, self, superficie, proteccion = 0) #tiene otro self, porque el atributo pared es lo mismo que en Pared el atributo nombre
#En Ventana.__init__(....) ponemos proteccion = 0, para que no nos pida ese atributo en ParedCortina, dado que no lo necesitamos

#nueva clase con los elementos en común entre la clase Ventana y ParedCortina
class Cristal:
    def __init__(self, superficie):
        self.superficie = superficie
    
    def devolver(self):
        return self.superficie
```
