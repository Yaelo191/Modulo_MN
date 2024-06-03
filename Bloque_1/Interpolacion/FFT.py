import numpy as np

def fft(ys):
    n = ys.size
    if n <= 1:
        return ys
    else:
        evens = fft(ys[::2])
        odds = fft(ys[1::2])
        T = np.exp(-2j * np.pi * np.arange(n//2) / n)
        return np.concatenate([evens + T * odds, evens + T * -odds])
def fftinterp(ytils, x):
      n = ytils.size
      m = n//2
      val = ytils[:m]@np.exp(np.arange(m)*x*1j)
      val += ytils[m]*np.cos(m*x)
      val += ytils[m+1:]@np.exp(np.arange(-m+1,0)*x*1j)
      return val/n