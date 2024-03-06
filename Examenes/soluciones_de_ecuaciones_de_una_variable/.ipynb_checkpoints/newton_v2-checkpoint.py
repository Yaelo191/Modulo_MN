import numpy as np

def encontrar_intervalo_n(funcion, inicio, fin, paso=0.1):
    x = inicio
    while x <= fin:
        if funcion(x) * funcion(x + paso) < 0:
            yield x, x + paso
            x = x + paso 
        x += paso

def metodo_biseccion_n(funcion, inicio, fin, tolerancia=0.00001, max_iter=1000):
    
    intervalos = encontrar_intervalo_n(funcion, inicio, fin)
    raices = []
    for intervalo in intervalos:
        a, b = intervalo
        iteracion = 1

        while iteracion <= max_iter:
            c = (a + b) / 2
            if abs(funcion(c)) < tolerancia:
                raices.append(c)
                a, b = intervalo
                a = c
            if funcion(c) * funcion(a) < 0:
                b = c
            else:
                a = c
            iteracion += 1

    return raices

def metodo_newton_v2(funcion, funcion_prime, a=-10, b=10, tolerancia=0.000001, max_iter=10000):
    funcion = lambda x: eval(def_funcion)
    funcion_prime = lambda x: eval(def_funcion_prime)
    raices_biseccion = metodo_biseccion_n(funcion, a, b)
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
def_funcion_prime = input("Ingrese la derivada de la función anterior (por ejemplo para '2*x + 7'): ")

metodo_newton(def_funcion, def_funcion_prime)
