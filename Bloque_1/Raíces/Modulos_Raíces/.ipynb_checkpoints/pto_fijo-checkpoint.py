import numpy as np

def metodo_punto_fijo(def_funcion, P0=1, tolerancia=1e-05, max_iter=10000):
    """
    metodo de punto fijo
    In:
    def_funcion: Recibe una funcion f(x) a modo de string.
    P0: semilla o aproximado de la raiz
    tolerancia: indica la diferencia maxima en la busqueda de raices. 0.00001 por defecto.
    max_iter: indica la cantidad maxima de iteraciones. 10000 por defecto
    
    Out:
    imprime las raices encontradas e indica la aproximacion actual en caso contrario
    """
    funcion = lambda x: eval(def_funcion)
    for i in range(2, max_iter):
        x = funcion(P0)
        if abs(x - P0) < tolerancia:
            print(f"Raíz encontrada: {x}")
            break
        elif i == max_iter:
            print(f"Se alcanzó el número máximo de iteraciones ({max_iter}).")
        P0 = x 
    return 