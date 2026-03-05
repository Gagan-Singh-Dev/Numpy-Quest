# Question: Reverse a 1D array without using loops.

import numpy as np

x = np.fromiter(range(1, 7), dtype=int)
result = x[::-1]

print(f"Original Array: {x}")
print(f"Reversed Array: {result}")