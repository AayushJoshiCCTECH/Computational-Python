import numpy as np


def lagrange_Interpolation(x, y, x_val):
    n = len(x)
    result = 0.0
    for i in range(n):
        term = y[i]
        for j in range(n):
            if i != j:
                term *= (x_val - x[j]) / (x[i] - x[j])
        result += term
    return result


x = np.array([0, 20, 40, 60, 80, 100], float)
y = np.array([1.000, 0.889, 0.745, 0.582, 0.412, 0.248], float)


temperature_to_Interpolation = [10, 30, 50, 70, 90]

print("Interpolated pressure:")
for temp in temperature_to_Interpolation:
    interpolated_pressure = lagrange_Interpolation(x, y, temp)
    print(f"At {temp}\u00b0C: {interpolated_pressure}")
    
