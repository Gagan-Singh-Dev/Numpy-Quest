# Question: Create a 5×5 identity matrix.

import numpy as np

# Method 1: Direct identity
x = np.identity(5, dtype=int)
print(x, "\n")

# Method 2: Eye function (more flexible)
x = np.eye(5, dtype=int)
print(x, "\n")

# Method 3: Diagonal from ones
x = np.diag(np.ones(5, dtype=int))
print(x)