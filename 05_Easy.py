# Question: Fill a 4×4 matrix with random integers from 1 to 100.

import numpy as np

#Method 01
x = np.random.randint(1, 101, (4, 4))
print(x, "\n")

#Method 02
x = np.random.choice(np.arange(1, 101), size=(4, 4))
print(x, "\n")

#Method 03
x = (np.random.random((4, 4)) * 100).astype(int) + 1
print(x)