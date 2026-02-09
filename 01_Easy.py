# Question: Create a NumPy array of integers from 10 to 49.

import numpy as np

# Method 01
x = np.arange(10, 50)
print(x, "\n")

# Method 02
# Needs the number of elements because
# it creates duplicates if not defined.
x = np.linspace(10, 49, 40, dtype=int)
print(x, "\n")

# Method 03
# This is slightly more memory-efficient
# if you’re building from a Python iterator.
x = np.fromiter(range(10, 50), dtype=int)
print(x)