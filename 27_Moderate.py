# Question: Compute the dot product of two 1D arrays efficiently.

import numpy as np

x = np.random.randint(1, 11, 5, dtype=int)
y = np.random.randint(1, 11, 5, dtype=int)
result = np.dot(x, y)

print(f"Array x: {x}")
print(f"Array y: {y}")
print(f"Result: {result}")