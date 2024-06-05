import numpy as np
import sympy as sym

def lege_interpol(puntosx, puntosy):
    x = sym.Symbol('x')
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
        ecuacion = numerador/denominador
    else:
        k = np.where(x == puntosx)[0]
        ecuacion = puntosy[k[0]] 
    expresion = sym.simplify(ecuacion)
    ecuacion = sym.lambdify(x, expresion)
    return ecuacion, expresion