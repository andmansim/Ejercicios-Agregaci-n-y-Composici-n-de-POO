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