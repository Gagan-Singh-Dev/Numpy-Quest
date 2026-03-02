# Question: Find the maximum and minimum values of an array efficiently.

import numpy as np

x = np.fromiter(range(1, 11), dtype="int")

print(x)
print(f"Max: {x.max()}")
print(f"Min: {x.min()}")

# If you also need the positions of min/max values
print(f"Max: {x[np.argmax(x)]} at index {np.argmax(x)}")
print(f"Min: {x[np.argmin(x)]} at index {np.argmin(x)}")

# For small arrays, Python’s built-ins are fine
# (though slower than NumPy for large arrays)
print(f"Max: {max(x)}")
print(f"Min: {min(x)}")

# These are function equivalents of .max() and .min()
# but sometimes preferred for clarity in functional programming style
print(f"Max: {np.amax(x)}")
print(f"Min: {np.amin(x)}")

# If you want both max and min together, ptp gives the range (max - min).
# You can combine it with min
print(f"Range: {np.ptp(x)}")   # max - min
print(f"Min: {x.min()}, Max: {x.min() + np.ptp(x)}")