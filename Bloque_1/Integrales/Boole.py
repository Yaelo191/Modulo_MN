#def f(x):
    #return 1/np.sqrt(x**2+1)
    
#a = 0.
#b = 1.
#Npuntos=52

def integracion_boole(f, a , b , Npuntos=100):

    if not Npuntos % 4 == 0:
        corrector = Npuntos % 4
        Npuntos -= corrector
        print(f"Se requiere un número de puntos múltiplo de 4, los puntos ahora son {Npuntos}")
    Npuntos += 1
    h = (b-a)/(Npuntos-1)
    Resultado = 0
    
    for i in range(1, Npuntos+1):
        x = a + (i-1) * h
        if i == 1 or i == Npuntos:
            contribucion = f(x)*(14/45)*h
            #print(f'14/45 {contribucion}')
        elif (i-1) % 4 == 0:
            contribucion = f(x)*(28/45)*h  
            #print(f'28/45 {contribucion}')
        elif (i+1) % 4 == 0:
            contribucion = f(x)*(24/45)*h
            #print(f'24/45 {contribucion}')
        else:
            contribucion = f(x)*(64/45)*h
            #print(f'64/45 {contribucion}')
        Resultado += contribucion
    print(f"La integral da como resultado: ")
    print(Resultado)
    return Resultado
    
    
#integracion_boole(f, a , b, Npuntos)