import funciones

if __name__ == "__main__":
    print("La empresa " + funciones.empresa.nomEmpr + " tiene sus instalaciones en las ciudades:" + funciones.ciudad1.nombre
          + " y " + funciones.ciudad2.nombre)
    print("Los edificios de la empresa en " + funciones.ciudad1.nombre + " son: " + " ".join(funciones.ciudad1.l_edif))
    print("El edificio de la empresa en " + funciones.ciudad2.nombre + " es: " + " ".join(funciones.ciudad2.l_edif))
    print(funciones.empresa.nomEmpr + "tiene a estos empleados " + " ".join(funciones.empresa.l_empl))

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