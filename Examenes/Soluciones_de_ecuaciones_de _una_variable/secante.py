import numpy as np

def secante(def_funcion, P0=1, P1=10, tolerancia=0.000001, max_iter=10000):
        """
    metodo secante
    In:
    def_funcion: Recibe una funcion f(x) a modo de string.
    P0: Primer semilla/aproximacion
    P1: Segunda semilla/aproximacion
    tolerancia: indica la diferencia maxima en la busqueda de raices. 0.000001 por defecto.
    max_iter: indica la cantidad maxima de iteraciones. 10000 por defecto
    
    Out: Imprime las raices encontradas, posteriormente indica cuando acabo las iteraciones.
    """
    funcion = lambda x: eval(def_funcion)
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
    print(f"Se alcanzó el número máximo de iteraciones ({max_iter}).")
    return 
def_funcion = input("Ingrese una función de x (por ejemplo 'x**2 + 7*x + 12'): ")
d0 = float(input("Ingrese una semilla: "))
d1 = float(input("Ingrese una segunda semilla: "))
res = secante(def_funcion, d0, d1)