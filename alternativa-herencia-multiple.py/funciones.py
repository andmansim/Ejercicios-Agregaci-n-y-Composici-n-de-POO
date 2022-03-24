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
            suma = suma +   (v.superficie)
        for v in self.pared2.ventana1:
            suma = suma +   (v.superficie)        
        for v in self.pared3.ventana1:
            suma = suma +   (v.superficie)
        for v in self.pared4.ventana1:
            suma = suma +   (v.superficie)
            
        return suma

class Pared: #La pared contiene ventanas
    def __init__(self, nombre):
        self.nombre = nombre
        self.ventana1 = [] 

class Ventana:
    def __init__(self, pared, superficie):
        self.pared = pared
        self.superficie = superficie
        self.pared.ventana1.append(self)


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
p_n = Pared("pared norte")
p_s = Pared("pared sur")
p_e = Pared("pared este")
p_o = Pared("pared oeste")

#Superficies de las ventanas
v_n = Ventana (p_n,3)
v_s = Ventana (p_s,5)
v_e = Ventana (p_e,7)
v_o = Ventana (p_o,0.3)

ventana = Ventana.proteccion

casa = Casa(p_n, p_s, p_e, p_o)

print(casa.sumar())

class ParedCortina(Pared, Ventana):
    def __init__(self, nombre, superficie):
        Pared.__init__(self, nombre)
        Ventana.__init__(self, self, superficie) #tiene otro self, porque el atributo pared es lo mismo que en Pared el atributo nombre

pared_cortina = ParedCortina("pared sur", 10)
casa.pared2 = pared_cortina
print(casa.sumar())
