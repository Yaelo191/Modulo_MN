import numpy as np

def metodo_secante_gauss(def_funcion, P0=1, P1=10, tolerancia=0.000001, max_iter=10000):
    """
    Método de la secante.
    
    Args:
        def_funcion (función): Función f(x) a modo de string.
        P0 (float): Primer semilla/aproximación.
        P1 (float): Segunda semilla/aproximación.
        tolerancia (float): Diferencia máxima en la búsqueda de raíces. Por defecto 0.000001.
        max_iter (int): Cantidad máxima de iteraciones. Por defecto 10000.
    
    Returns:
        float: La raíz encontrada.
        
    Prints:
        Mensajes indicando las raíces encontradas o si se alcanzó el número máximo de iteraciones.
    """
    funcion = def_funcion
    q0 = funcion(P0)
    q1 = funcion(P1)
    for i in range(2, max_iter):
        x = P1 - q1 * (P1 - P0) / (q1 - q0)
        if abs(x - P1) < tolerancia:
            return x
        P0, P1, q0, q1 = P1, x, q1, funcion(x)
    print(f"Se alcanzó el número máximo de iteraciones ({max_iter}).")
