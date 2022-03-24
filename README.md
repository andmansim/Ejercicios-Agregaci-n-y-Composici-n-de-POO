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

```

El diagrama UML del tercer ejercicio ejercicio: La alternativa a la herencia múltiple, es:

![diagrama uml la alternativa](/alternativa-herencia-multiple/alternativa.jpg)

```

```
