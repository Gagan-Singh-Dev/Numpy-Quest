# Question: Replace all even numbers in an array with -1.

import numpy as np

x = np.fromiter(range(1, 11), dtype="int")
print(f"Original Array: {x}")

x[x%2==0] = -1
print(f"Replaced Array: {x}")