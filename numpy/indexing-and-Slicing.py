import numpy as np

# 1D indexing
arr1 = np.array([10,20,30,40,50])

print(f"First Element: {arr1[0]}")
print(f"Second Element: {arr1[1]}")

print(f"Last Element: {arr1[-1]}")

# Slicing: [start: stop: step]
print(f"Elements 1 to 3: {arr1[1:4]}") # last index is not included
print("Every other Element: ", arr1[::2]) # start from 0 to the last index with a jump of 2

print("\n")
#2D indexing
arr2 = np.array([[1,2,3],
                 [4,5,6],
                 [7,8,9]])
print(f"2D array: \n{arr2}\n")
#Negative indexing:
print("Reversed printing: \n", arr2[::-1])
# [row, column]
print("Element at row 0, column 0: ", arr2[0,0]) #1
print("Element at row 1, column 2: ", arr2[1,2]) #6
# All columns(Elements) of first row
print("First row: ", arr2[0, :])

# All rows of first column
print("First row: ", arr2[:, 0])

#2 columns
print("First two column: \n", arr2[:, 0:2])

#All rows but every other column
print("Every other column:\n", arr2[:, ::2])

#submatrix
print("Submatrix (first 2 rows, first 2 columns): ")
print(arr2[0:2, 0:2])

print("Submatrix (last 2 rows, last 2 columns):")
print(arr2[1: , 1: ])

