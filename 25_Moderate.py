# Question: Find common elements between two arrays using vectorized operations.

import numpy as np

x = np.array([1, 5, 8, 3, 6, 9, 2])
y = np.array([9, 5, 0, 1, 6, 9, 8])

result = np.intersect1d(x, y)

print(x)
print(y)
print(result)