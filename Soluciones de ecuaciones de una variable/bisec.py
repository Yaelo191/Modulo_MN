def funcion_a_evaluar(x):
    # Define la función que quieres encontrar la raíz
    return x**2 - 4

def metodo_biseccion(funcion, a, b, tol=0.0001, max_iter=1000):
    # Verifica si los valores iniciales cumplen con el teorema de Bolzano
    if funcion_a_evaluar(a) * funcion_a_evaluar(b) > 0:
        print("")
        return None

    iteracion = 1

    while iteracion <= max_iter:
        # Encuentra el punto medio
        c = (a + b) / 2

        # Verifica si c es la raíz
        if abs(funcion_a_evaluar(c)) < tolerancia:
            print(f"La raíz aproximada es: {c}")
            return c

        # Actualiza los extremos del intervalo
        if funcion_a_evaluar(c) * funcion_a_evaluar(a) < 0:
            b = c
        else:
            a = c

        iteracion += 1

    print(f"El método de bisección no convergió después de {iteracion}")
    return None
resultado = metodo_biseccion(a, b, tolerancia, max_iter)

