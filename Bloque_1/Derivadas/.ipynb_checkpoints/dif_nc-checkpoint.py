import numpy as np

def dif_derecha(f, x, h=1e-05):

    dfl = (f(x+h) - f(x))/h
    print(f"Derivada derecha aproximada: {dfl}")
    
    return dfl

def dif_izquierda(f, x, h=1e-05):

    dfr = (f(x) - f(x-h))/h
    print(f"Derivada izquierda aproximada: {dfr}")
    
    return dfr

