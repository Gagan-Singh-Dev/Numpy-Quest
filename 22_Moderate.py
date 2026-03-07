# Question: Replace diagonal elements of a square matrix with zeros.

import numpy as np

x = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

result = x.copy()
np.fill_diagonal(result, 0)

print(f"Original Matrix: \n{x}")
print(f"Result Matrix: \n{result}")