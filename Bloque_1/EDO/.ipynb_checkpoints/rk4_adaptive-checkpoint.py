import numpy as np

def rk4_global(f, a, b, n, yinit, eps=1e-05, maxiter=10):
    def edo_rk4(f, a, b, n, yinit):
        h = (b-a)/(n-1)
        xs = a + np.arange(n)*h
        ys = np.zeros(n)
        y = yinit
        for j, x in enumerate(xs):
            ys[j] = y
            k0 = h*f(x, y)
            k1 = h*f(x+h/2, y+k0/2)
            k2 = h*f(x+h/2, y+k1/2)
            k3 = h*f(x+h, y+k2)
            y += (k0 + 2*k1 + 2*k2 + k3)/6
        return xs, ys
    x0, y0 = edo_rk4(f, a, b, n, yinit)
    i = 0
    epsprime = eps + 1
    while eps<=epsprime:
        N = 2*n - 1
        xs, ys = edo_rk4(f, a, b, N, yinit)    
        epsprime = (ys[-1]-y0[-1])/15
        if maxiter<=i:
            continue
        else:
            print(f'No se alcanzo la tolerancia deseada en {i} iteraciones')
            break
    return xs, ys

def rk4_local(f, a, b, n, yinit, eps=1e-05, maxiter=10):
    def edo_rk4(f, a, b, n, h, yinit):
        xs = a + np.arange(n)*h
        ys = np.zeros(n)
        y = yinit
        for j, x in enumerate(xs):
            ys[j] = y
            k0 = h*f(x, y)
            k1 = h*f(x+h/2, y+k0/2)
            k2 = h*f(x+h/2, y+k1/2)
            k3 = h*f(x+h, y+k2)
            y += (k0 + 2*k1 + 2*k2 + k3)/6
        return xs, ys
    h = (b-a)/(n-1)
    x0, y0 = edo_rk4(f, a, b, n, h, yinit)
    x0, y0 = edo_rk4(f, a, b, n, h/2, yinit)
    
    return xs, ys