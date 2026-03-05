# Question: Create a 6×6 matrix with sequential values from 0 to 35.

import numpy as np

x = np.fromiter(range(0, 36), dtype=int).reshape(6, 6)
print(x)