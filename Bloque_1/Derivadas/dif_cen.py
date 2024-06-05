import numpy as np

def dif_central(f, x, h=1e-05):
    
    dfc = (f(x+h/2) - f(x-h/2))/h
    print(f"Derivada central de 2do orden aproximada: {dfc}")
    
    return dfc

def dif_central_4to(f, x, h=1e-05):
    
    dfc4 = (-f(x+2*h) + 8*f(x+h) - 8*f(x-h) + f(x-2*h))/(12*h)
    print(f"Derivada central de 4to orden aproximada: {dfc4}")
    
    return dfc4
    
def segunda_dif_central(f, x, h=1e-05):
    d2fc = (f(x + h/2) + f(x - h/2) - 2*f(x)) / (h**2)
    print(f"Segunda derivada central aproximada: {d2fc}")
    
    return d2fc
