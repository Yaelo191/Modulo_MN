from .legengre import lege_interpol
from .splinelineal import linear_spline_interpolation
from .gaussNewton import gaussnewton, getKrs, relErrorTot
from .FFT import fftinterp, fft
__all__ = [
    'legengre',
    'linear_spline_interpolation',
    'gaussnewton',
    'getKrs',
    'relErrorTot',
    'fftinterp',
    'fft'
]

