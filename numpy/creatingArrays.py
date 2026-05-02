import numpy as np

arr1 = np.array([23,71,213,43,141,42,41])
print(arr1)
print("2D ARRAY:")
arr2 = np.array([[1,2,3], [4,5,6]])
print(arr2)

print("3D ARRAY:")
arr3 = np.array([[[1,2,3],[4,5,6]],[[2,6,7],[14,5,6]]])
print(arr3)

print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)

