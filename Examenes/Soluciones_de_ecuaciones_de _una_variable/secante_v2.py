import numpy as np

def secante_v2(def_funcion, a=1, b=10, tolerancia=0.000001, max_iter=10000):
            """
    Metodo secante v2
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
    if funcion(a)>0:
        P0 = b
        q0 = funcion(a)
        q1 = funcion(b)
    if funcion(a)<0:
        P0 = a
        q0 = funcion(b)
        q1 = funcion(a)
    else: 
        print(f"{a} es una raiz de la funcion")

    for i in range(max_iter):
        if funcion(a)>0:
                x = P0 - q1*(P0 - a)/(q1 - q0)
        else:
                x = P0 - q1*(b -P0)/(q1 - q0)
        if (abs(x - P0) < tolerancia):
            print(f"Raíz encontrada: {x}")
            return
        P0 = x
        q1 = funcion(x)
    print(f"Se alcanzó el número máximo de iteraciones ({max_iter}). La aproximación actual es: {x}")
    return 
def_funcion = input("Ingrese una función de x (por ejemplo 'x**2 + 7*x + 12'): ")
d0 = float(input("Ingrese extremo a: "))
d1 = float(input("Ingrese extremo b: "))
res = secante_v2(def_funcion, d0, d1)