import numpy as np

def encontrar_intervalo(funcion, inicio=-10, fin=10, paso=0.1):
    """
    Buscador de intervalos
    In:
    funcion: Recibe una funcion f(x) a modo de funcion lambda.
    inicio: Marca desde donde comienza a buscar intervalos. -10 por defecto
    final: Marca hasta donde para su busqueda de intervalos. 10 por defecto
    paso: Indica el avance en la busqueda de cada intervalo. 0.1 por defecto
    
    Out:
    intervalos a modo de lista
    """
    x = inicio
    while x <= fin:
        if funcion(x) * funcion(x + paso) <= 0 :
            yield x, x + paso #Crea y devuelve una especie de lista con los pares de intervalos
            x = x + paso  # Actualiza el valor de inicio
        x += paso

def metodo_biseccion(def_funcion, inicio=-10, fin=10, tolerancia=0.00001, max_iter=1000):
     """
    Metodo de biseccion
    In:
    def_funcion: Recibe una funcion f(x) a modo de string.
    inicio: Marca desde donde comienza a buscar intervalos. -10 por defecto
    final: Marca hasta donde para su busqueda de intervalos. 10 por defecto
    tolerancia: indica la diferencia maxima en la busqueda de raices. 0.00001 por defecto.
    max_iter: indica la cantidad maxima de iteraciones. 1000 por defecto
    
    Out:
    imprime las raices encontradas
    raices: raices contenidas en una lista 
    """
    funcion = lambda x: eval(def_funcion)
    intervalos = encontrar_intervalo(funcion, inicio, fin)
    raices = [] 
    
    for intervalo in intervalos:
        a, b = intervalo
        iteracion = 1

        while iteracion <= max_iter:
            # Encuentra el punto medio
            c = (a + b) / 2

            # Verifica si c es la raíz
            if abs(funcion(c)) < tolerancia:
                raices.append(c)
                print(f"La raíz aproximada es: {c}")

                # Actualiza los extremos del intervalo para buscar la siguiente raíz
                a, b = intervalo
                a = c

            # Actualiza los extremos del intervalo
            if funcion(c) * funcion(a) < 0:
                b = c
            else:
                a = c

            iteracion += 1

    print("Fin del programa")
    return raices #Devuelve las raices en forma de array para sser utlizadas despues
    
def_funcion = input("Ingrese una función de x (por ejemplo, 'x**2 - 4'): ")
metodo_biseccion(def_funcion, -10, 10)
