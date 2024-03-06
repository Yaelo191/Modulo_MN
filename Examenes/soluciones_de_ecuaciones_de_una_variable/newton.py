import numpy as np
    
def metodo_newton(def_funcion, def_funcion_prime, P0=1, tolerancia=0.000001, max_iter=10000):
    """
    Metodo de newton
    In:
    def_funcion: Recibe una funcion f(x) a modo de string.
    def_funcion_prime: Recibe la derivada de la funcion f(x) a modo de string.
    P0: semilla o aproximado de la raiz
    tolerancia: indica la diferencia maxima en la busqueda de raices. 0.00001 por defecto.
    max_iter: indica la cantidad maxima de iteraciones. 10000 por defecto
    
    Out:
    imprime las raices encontradas e indica que alcanzo el maxmo de iteraciones
    """
    iteracion = 1  
    funcion = lambda x: eval(def_funcion)
    funcion_prime = lambda x: eval(def_funcion_prime)
    for i in range(max_iter):
        x = P0 - funcion(P0)/funcion_prime(P0)
        if (abs(x - P0) < tolerancia):
            print(f"Raíz encontrada: {x}")
            return
        P0 = x 
    print(f"Se alcanzó el número máximo de iteraciones ({max_iter}).")
    return 
def_funcion = input("Ingrese una función de x (por ejemplo 'x**2 + 7*x + 12': ")
def_funcion_prime = input("Ingrese la derivada de la funcion anterior (por ejemplo para '2*x +7': ")
d0 = float(input("Ingrese una semilla: "))
res = metodo_newton(def_funcion, def_funcion_prime, P0=d0)