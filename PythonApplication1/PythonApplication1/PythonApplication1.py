import numpy as np

def lagrange_interpolation(x, y, x_val):
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

x_val = float(input("Enter value of x_val: "))

ans = lagrange_interpolation(x, y, x_val)
print("Interpolated value at x =", x_val, "is", ans)
