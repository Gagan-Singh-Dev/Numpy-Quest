# Question: Count elements greater than 50 in a random integer array.

import numpy as np

x = np.random.randint(30, 100, 20)
count = np.sum(x>50)

print(f"Array: {x}")
print(f"Count of numbers greater than 50: {count}")