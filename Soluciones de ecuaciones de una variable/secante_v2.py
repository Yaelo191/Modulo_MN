import numpy as np

def funcion(x):
    return eval(def_funcion)

def secante(P0=1, P1=10, tolerancia=0.000001, max_iter=10000):
    iteracion = 2  
    q0 = funcion(P0)
    q1 = funcion(P1)
    for i in range(max_iter):
        x = P1 -q1*(P1 - P0)/(q1 - q0)
        if (abs(x - P1) < tolerancia):
            print(f"Raíz encontrada: {x}")
            return
        P0 = P1
        q0 = q1
        P1 = x
        q1 = funcion(x)
    print(f"Se alcanzó el número máximo de iteraciones ({max_iter}). La aproximación actual es: {x}")
    return 
def_funcion = input("Ingrese una función de x (por ejemplo 'x**2 + 7*x + 12'): ")
d0 = float(input("Ingrese una semilla: "))
d1 = float(input("Ingrese una segunda semilla: "))
res = secante(P0=d0, P1=d1)