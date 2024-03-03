def metodo_newton(P0=1, tolerancia=0.000001, max_iter=10000):
    iteracion = 1  
    for i in range(max_iter):
        x = P0 - funcion(P0)/funcion_prime(P0)
        if (abs(x - P0) < tolerancia):
            print(f"Raíz encontrada: {x}")
            return
        P0 = x 
    print(f"Se alcanzó el número máximo de iteraciones ({max_iter}). La aproximación actual es: {x}")
    return 