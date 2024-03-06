import numpy as np

def metodo_newton_v2(def_funcion, def_funcion_prime, a=-10, b=10, tolerancia=0.0000001, max_iter=10000):
    funcion = lambda x: eval(def_funcion)
    funcion_prime = lambda x: eval(def_funcion_prime)
    
    def encontrar(funcion, inicio, fin, paso=0.01):
        x = inicio
        while x <= fin:
            if funcion(x) * funcion(x + paso) < 0:
                yield x, x + paso
                x = x + paso 
            x += paso
    intervalos = encontrar(funcion, a, b)
    raices = []
    for intervalo in intervalos:
        
        a, b = intervalo
        iteracion = 1

        while iteracion <= 1000:
            c = (a + b) / 2
            if abs(funcion(c)) < 0.00001:
                raices.append(c)
                a, b = intervalo
                a = c
            if funcion(c) * funcion(a) < 0:
                b = c
            else:
                a = c
            iteracion += 1
    if not raices:
        raices = [complex(0, 1)] 
    for semilla in raices:
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

