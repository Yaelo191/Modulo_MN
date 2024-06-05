import numpy as np

def rk4_vec(fs, a, b, n, yinits, neq):
    h = (b-a)/(n-1)
    xs = a + np.arange(n)*h
    ys = np.zeros((n, neq))
    yvals = np.copy(yinits).astype(np.float64) 
    for j, x in enumerate(xs):
        ys[j, :] = yvals
        k0 = h * fs(x, yvals)
        k1 = h * fs(x + h/2, yvals + k0/2)
        k2 = h * fs(x + h/2, yvals + k1/2)
        k3 = h * fs(x + h, yvals + k2)
        yvals += (k0 + 2*k1 + 2*k2 + k3)/6
    return xs, ys