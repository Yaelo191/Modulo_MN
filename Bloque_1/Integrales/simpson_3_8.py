import numpy as np

#def f(x):
    #return 1 / np.sqrt(x**2 + 1)
    
#a = 0.
#b = 1.
#Npuntos=51

def integracion_simpson_3_8(f, a , b , Npuntos=100):

    if not Npuntos % 3 == 0:
        corrector = Npuntos % 3
        Npuntos -= corrector
        print(f"Se requiere un número de puntos múltiplo de 3, los puntos ahora son {Npuntos}")
    Npuntos += 1
    h = (b-a)/(Npuntos-1)
    Resultado = 0
    
    for i in range(1, Npuntos+1):
        x = a + (i-1) * h
        if i == 1 or i == Npuntos:
            contribucion = f(x)*(3/8)*h
            #print(f'3/8 {contribucion}')
        elif (i-1) % 3 == 0:
            contribucion = f(x)*(6/8)*h
            #print(f'6/8 {contribucion}')
        else:
            contribucion = f(x)*(9/8)*h
            #print(f'9/8 {contribucion}')
        Resultado += contribucion
    print(f"La integral da como resultado: ")
    print(Resultado)
    return
    
#integracion_simpson_3_8(f, a , b, Npuntos)