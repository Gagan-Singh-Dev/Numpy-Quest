# Question: Stack two 1D arrays vertically into a single matrix.

import numpy as np

x = np.fromiter(range(0, 6), dtype=int)
y = np.fromiter(range(6, 12), dtype=int)

print(f"Array 1: {x}")
print(f"Array 2: {y}")

z = np.stack((x, y), 1)
print(f"Stacked Array: \n{z}")