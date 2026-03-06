# Question: Create a 4×4 checkerboard matrix of 0s and 1s.

import numpy as np

x = np.zeros([4, 4], dtype=int)

x[1::2, ::2] = 1
x[::2, 1::2] = 1

print(x)