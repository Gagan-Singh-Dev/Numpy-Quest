# Question: Extract all negative values from an array.

import numpy as np

x = np.array([-4, 5, 67, -9, -5, -48, 345, 12])
mask = x < 0
result = x[mask]

print(f"Original Array: {x}")
print(f"Negative Array: {result}")