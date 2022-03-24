'''
Se muestra antes el signo de intrrogación que el mensaje, porque solo va pasa a la función
yang.__del__() cuando termina el programa o cuando se borran todos los objetos. Pero al haber un print("?")
justo depués del del(yang), entonces se imprimirá cuando ya haya impreso "?". Esto se debe a que tenemos dos objetos
idénticos, donde el del(yang) solo elimina yang, por tanto queda ying.yang que se elimina tras print("?")
'''

'''
Para resolver esto, la manera más fácil y obvia sería colocar el print("?") justo antes del del(yang). 
Otra manera sería destruir todos los objetos, los cuales serían yang y ying.yang. Así si ponemos del(yang) y 
del(yin.yang) antes del print("?"), lo tendríamos.
'''