import numpy as np
from .bisec import metodo_biseccion, encontrar_intervalo

def metodo_newton_v2(funcion, funcion_prime, a=-100, b=100, tolerancia=0.000001, max_iter=10000):
    """
    Metodo de newton v2
    In:
    def_funcion: Recibe una funcion f(x) a modo de string.
    def_funcion_prime: Recibe la derivada de la funcion f(x) a modo de string.
    a: Indica desde donde puede encontrar raices. -100 por defecto
    b: Indica hasta donde puede encontrar raices. 100 por defecto
    tolerancia: indica la diferencia maxima en la busqueda de raices. 0.000001 por defecto.
    max_iter: indica la cantidad maxima de iteraciones. 10000 por defecto
    
    Out:
    imprime las aproximaciones dadas por el metodo de biseccion y posteriormente las raices 
    """
    raices_biseccion = metodo_biseccion(funcion, a, b)
    funcion = lambda x: eval(def_funcion)
    funcion_prime = lambda x: eval(def_funcion_prime)
    for semilla in raices_biseccion:
        P0 = semilla
        iteracion = 1  
        for i in range(max_iter):
            x = P0 - funcion(P0) / funcion_prime(P0)
            if abs(x - P0) < tolerancia:
                print(f"Raíz encontrada: {x}")
                break
            P0 = x 
        else:
            print(f"Se alcanzó el número máximo de iteraciones ({max_iter}).")

def_funcion = input("Ingrese una función de x (por ejemplo 'x**2 + 7*x + 12'): ")
def_funcion_prime = input("Ingrese la derivada de la función anterior (por ejemplo para '2*x +7'): ")
# Llamada a la función con las raíces iniciales
metodo_newton_v2(def_funcion, def_funcion_prime)
