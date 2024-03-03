import numpy as np

def funcion(x):
    return eval(def_funcion) 
def funcion_prime(x):
    return eval(def_funcion_prime)

def_funcion = input("Ingrese una función de x (por ejemplo 'x**2 + 7*x + 12': ")
def_funcion_prime = input("Ingrese la derivada de la funcion anterior (por ejemplo para '2*x +7': ")
d0 = float(input("Ingrese una semilla: "))
res = metodo_newton(P0=d0)