import numpy as np

numbers = list(map(int, input().split()))
array = np.array(numbers).reshape(3,3)
print(array)