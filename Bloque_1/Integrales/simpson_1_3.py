import numpy as np

#def f(x):
    #return 1 / np.sqrt(x**2 + 1)
    
#a = 0.
#b = 1.
#Npuntos=51

def integracion_simpson_1_3(f, a , b , Npuntos=100):

    if not Npuntos % 2 == 0:
        corrector = Npuntos % 2
        Npuntos -= corrector
        print(f"Se requiere un número de puntos múltiplo de 2, los puntos ahora son {Npuntos}")
    Npuntos += 1
    h = (b-a)/(Npuntos-1)
    Resultado = 0
    
    for i in range(1, Npuntos+1):
        x = a + (i-1) * h
        if i == 1 or i == Npuntos:
            contribucion = f(x)*(1/3)*h
            #print(f'1/3 {contribucion}')
        elif i % 2 == 0:
            contribucion = f(x)*(4/3)*h  
            #print(f'4/3 {contribucion}')
        else:
            contribucion = f(x)*(2/3)*h
            #print(f'2/3 {contribucion}')
        Resultado += contribucion
    print(f"La integral da como resultado: ")
    print(Resultado)
    return
    
#integracion_simpson_1_3(f, a , b, Npuntos)