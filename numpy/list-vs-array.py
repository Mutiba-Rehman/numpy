import time
import numpy as np
size = 5000000
list1 = list[int](range(size))
numpy_array = np.arange(size)

#python list
start = time.time()
# time.time() return the number of seconds passed since a fixed point in history calles the Epoch
xResult = [x + 10 for x in list1]
xtime = time.time() - start
print(f"Python list addition: {xtime:.5f} seconds")

#numpy array (vectorized)
start = time.time()
yresult = numpy_array + 10
ytime = time.time() - start
print(f"Numpy Array addition: {ytime:.5f} seconds")

#comparison
print(f"For {size} elements: Numpy Array is {xtime/ytime:.1f} x faster than python lists...")