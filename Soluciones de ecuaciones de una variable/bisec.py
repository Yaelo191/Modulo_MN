import numpy as np

def funcion(x):
    return eval(def_funcion)

def refinar_intervalo(x1, x2):
    ajuste = 0.1

    while funcion(x1) * funcion(x2) > 0:
        x1 += ajuste
        x2 -= ajuste

        if x1 >= x2:
            print("No se pudo encontrar un intervalo refinado.")
            return 

    return x1, x2

def metodo_biseccion(x1=-10, x2=10, tolerancia=0.0001, max_iter=1000):
   
    ref = refinar_intervalo(x1, x2)
    if ref is None:
        return None

    a, b = ref
    iteracion = 1

    while iteracion <= max_iter:
        # Encuentra el punto medio
        c = (a + b) / 2

        # Verifica si c es la raíz
        if abs(funcion(c)) < tolerancia:
            print(f"La raíz aproximada es: {c}")
            return c

        # Actualiza los extremos del intervalo
        if funcion(c) * funcion(a) < 0:
            b = c
        else:
            a = c

        iteracion += 1

    print("El método de bisección no converge después de las iteraciones especificadas.")
    return None

def_funcion = input("Ingrese una función de x (por ejemplo, 'x**2 - 4'): ")

resultado = metodo_biseccion()
