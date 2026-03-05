# Question: Flatten a 2D array.

import numpy as np

x = np.fromiter(range(1, 7), dtype=int).reshape(2, 3)

print(f"Original Array: \n{x}")
print(f"Flatten Array: {x.flatten()}")

# Memory Efficient when modification isn’t required
print(np.ravel(x))
print(np.ravel(x, order='F'))