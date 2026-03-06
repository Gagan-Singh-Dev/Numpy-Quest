# Question: Normalize a 1D array to range [0, 1] using vectorized operations.

import numpy as np

x = np.array([3, 6, 9, 2, 5], dtype=int)
normalised = (x - x.min()) / (x.max() - x.min())

print(f"Original Array: {x}")
print(f"Normalised Array: {normalised}")