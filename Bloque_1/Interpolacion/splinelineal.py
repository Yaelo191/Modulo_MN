import numpy as np

def linear_spline_interpolation(points_x, points_y, x_interp):

    x = np.array(points_x)
    y = np.array(points_y)

    if len(x) != len(y):
        raise ValueError("")

    indices = np.searchsorted(x, x_interp)
    slopes = (y[indices] - y[indices - 1]) / (x[indices] - x[indices - 1])
    interpolated_values = y[indices - 1] + slopes * (x_interp - x[indices - 1])

    return interpolated_values