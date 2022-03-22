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
        #funciones.ciudad1.eliminar_NY()
        funciones.ciudad1.l_edif.remove()
        del funciones.ciudad1
        
        print("Se ha destruido toda la ciudad de NY")
        
    elif usuario == "N":
        print("Perfecto, gracias por no destruir NY")   
    else:
        print("Esa opción no es válida, por favor intentelo de nuevo")