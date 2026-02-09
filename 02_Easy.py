# Question: Build a 3×3 matrix filled with zeros.

import numpy as np

# Method 01
x = np.zeros([3, 3], dtype=int)
print(x, "\n")

# Method 02
# This avoids initializing with zeros directly, then fills the array.
x = np.empty((3, 3), dtype=int)
x.fill(0)
print(x, "\n")

# Method 03
# This is semantically clear: "create a matrix filled with 0."
x = np.full((3, 3), 0, dtype=int)
print(x, "\n")

# Method 04
# This replicates the scalar 0 into a 3×3 matrix.
x = np.tile(0, (3, 3))
print(x)