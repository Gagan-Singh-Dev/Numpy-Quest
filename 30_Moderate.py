# Question: Find indices of elements between 20 and 40 in a matrix.

import numpy as np

matrix = np.array([[10, 25, 40],
                   [30, 50, 20],
                   [35, 15, 45]])

mask = (matrix >= 20) & (matrix <= 40)
indices = np.argwhere(mask)

print(f"Array: \n{matrix}")
print(f"Indices: \n{indices}")