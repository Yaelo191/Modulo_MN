def metodo_secante(P0=1, P1=10, tolerancia=0.000001, max_iter=10000):
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
    print(f"Se alcanzó el número máximo de iteraciones ({max_iter}). La aproximación actual es: {x}")
    return 
