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


```
Segundo ejercicio: Inmortal

```

```

El diagrama UML del tercer ejercicio ejercicio: La alternativa a la herencia múltiple, es:

![diagrama uml la alternativa](/alternativa-herencia-multiple/alternativa.jpg)

```

```
