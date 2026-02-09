# Question: Generate 20 evenly spaced numbers between 0 and 1.

import numpy as np

# Method 01
x = np.linspace(0, 1, 20)
print(x, "\n")

# Method 02: Using  with step size (but you need to calculate step manually)
x = np.arange(0, 1.05, 1/19)
print(x)