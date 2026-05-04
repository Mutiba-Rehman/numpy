import numpy as np

arr = np.array([[1,2,3,4],
                [5,6,7,8],
                [9,10,11,12]])

print("Array: ")
print(arr)
print("\n")
#Dimensions of the Array
print(f"Shape: {arr.shape}")

#Total number of Elements
print(f"Size:{arr.size}")

#Data Type
print(f"Data Type: {arr.dtype}")

#Size of each Element
print(f"Item Size: {arr.itemsize} bytes")

#Total Memory Used
print(f"Number of Bytes: {arr.nbytes} bytes")

#Transpose of the array
print(f"T(transpose): \n{arr.T}")
