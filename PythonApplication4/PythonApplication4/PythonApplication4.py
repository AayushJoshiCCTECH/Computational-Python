
import numpy as np


A = np.array([[2, 3, -1], [1, -1, 2], [3, 2, 1]])
b = np.array([[7], [5], [12]])


x = np.linalg.solve(A, b)

print("Ans:")
print(x)