# Question: Generate a boolean mask for elements divisible by 3.

import numpy as np

x = np.array([1, 4, 7, 9, 12, 15, 16, 17, 30])

mask = x % 3 == 0

print(f"Array: {x}")
print(f"Boolean Masks: {mask}")
print(f"Elements divisible by 03: {x[mask]}")