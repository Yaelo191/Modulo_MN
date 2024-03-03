import numpy as np

def funcion(x):
    return eval(def_funcion) 
def funcion_prime(x):
    return eval(def_funcion_prime)
    
def metodo_newton(P0=1, tolerancia=0.000001, max_iter=10000):
    iteracion = 1  
    for i in range(max_iter):
        x = P0 - funcion(P0)/funcion_prime(P0)
        if (abs(x - P0) < tolerancia):
            print(f"Raíz encontrada: {x}")
            return
        P0 = x 
    print(f"Se alcanzó el número máximo de iteraciones ({max_iter}). La aproximación actual es: {x}")
    return 
def_funcion = input("Ingrese una función de x (por ejemplo 'x**2 + 7*x + 12': ")
def_funcion_prime = input("Ingrese la derivada de la funcion anterior (por ejemplo para '2*x +7': ")
d0 = float(input("Ingrese una semilla: "))
res = metodo_newton(P0=d0)