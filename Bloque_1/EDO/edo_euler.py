import numpy as np

def edo_euler(f, a, b, n, yinit):
    h = (b-a)/(n-1)
    xs = a+np.arange(n)*h
    ys = np.zeros(n)
    y = yinit
    for j,x in enumerate(xs):
        ys[j] = y
        y += h*f(x, y)
    return xs, ys
    
def mejorado_euler(f, a, b, n, yinit):
    h =(b-a)/(n-1)
    xs = a+np.arange(n)*h
    ys = np.zeros(n)
    y = yinit
    for j, x in enumerate(xs):
        ys[j] = y
        y_pred = y+h*f(x, y) 
        y += h*(f(x, y)+f(x + h, y_pred))/2 
    return xs, ys
