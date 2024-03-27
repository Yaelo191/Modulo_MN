import numpy as np

#def f(x):
    #return 1 / np.sqrt(x**2 + 1)
    
#a = 0.
#b = 1.
#Npuntos=50

def integracion_rect(f, a , b , Npuntos=100):

    if not Npuntos % 2 == 0:
        corrector = Npuntos % 2
        Npuntos -= corrector
        print(f"Se requiere un número de puntos múltiplo de 2, los puntos ahora son {Npuntos}")
    Npuntos += 1
    h = (b-a)/(Npuntos-1)
    Resultado = 0
    
    for i in range(1, Npuntos):
        x = a + (i-1) * h
        contribucion = f(x)*h
        #print(contribucion)
        Resultado += contribucion
    print(f"La integral da como resultado: ")
    print(Resultado)
    return Resultado
    
#integracion_rect(f, a , b, Npuntos)