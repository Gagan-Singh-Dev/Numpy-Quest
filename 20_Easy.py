# Question: Swap the first and last rows of a 5×5 matrix.

import numpy as np

x = np.arange(1, 26, dtype=int).reshape(5, 5)
print(f"Original Array: \n {x}")
x[[0, -1]] = x[[-1, 0]]
print(f"Swapped Array: \n {x}")