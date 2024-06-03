import numpy as np

def lege_interpol(puntosx, puntosy, x):
    n = puntosx.size
    pesos = np.ones_like(puntosx)
    for i in range(n):
        for j in range(n):
            if j != i:
                pesos[i] *= (puntosx[i]-puntosx[j])
    pesos = 1/pesos
    if not np.any(puntosx == x):
        numerador = np.sum(pesos*puntosy/(x-puntosx))
        denominador = np.sum(pesos/(x-puntosx))
        predic = numerador/denominador
    else:
        k = np.where(x == puntosx)[0]
        predic = puntosy[k[0]]
    
        
    return predic