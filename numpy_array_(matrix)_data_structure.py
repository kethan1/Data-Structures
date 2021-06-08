import numpy as np

'''
Why Numpy?
Numpy arrays are more efficient (they take up less memory and are faster) for
larger datasets with the same type. Numpy arrays also provide you with lots
to ways to manipulate this data.

Numpy arrays are very inefficent with multiple types in the array.
'''

s = np.array([['Math', 89, 87, 75], ['English', 75, 78, 83], ['Science', 85,
                                                              89, 78]])
print(s)

# Reshape
record = np.reshape(s, (4, 3))
print("\nReshape:", record)

# Print By Indexes
print("\nIndexes:", s[0], s[0][0])

# Append
print(
    "\nAppend as row:", np.append(s, [[0, 1, 0, 4]], 0),
    "\nAppend as column:", np.append(s, [[1], [2], [3]], 1),
    "\nAppend (don't specify axis so flatten):", np.append(s, [[0, 1, 0, 4]])
)

# Delete
print(
    "\nDelete from row:", np.delete(s, [2], 0),
    "\nDelete from column:", np.delete(s, [2], 1),
    """\nDelete (don't specify axis so flatten and delete from as column from
    first row):""", np.delete(s, [1])
)

# Update
s_copy = np.copy(s)
s_copy[0] = [12]
print("\nUpdate row:", s_copy)
s_copy[0][0] = "39999"
print("\nUpdate column in row:", s_copy)

print("Manipulating Array")

"""
Numpy Data Types:

'?': boolean
'b': (signed) byte
'B': unsigned byte
'i': (signed) integer
'u': unsigned integer
'f': floating-point
'c': complex-floating point
'm': timedelta
'M': datetime
'O': (Python) objects
'S', 'a': zero-terminated bytes (not recommended)
'U': Unicode string
'V': raw data (void)
"""

# When specifying dtype, numpy converts every element in the array into the
# specified type. If it cannot turn it into the specified type, it throws an
# error.
array_to_manipulate = np.array([1, 2, 3, "9"], dtype="i4")
#                   ↑
# Array filled with 32 bit signed integers
print(array_to_manipulate)

for item in array_to_manipulate:
    print(type(item))


print("Showcase")

array1 = np.array([1, 2, 3, 4])  # Vector
print(array1)
print()

array2 = np.array([              # Matrix
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print(array2)
print()
array3 = np.array([              # Tensor
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ],
    [
        [5, 2, 63],
        [1, 2, 9],
        [8, 3, 5]
    ]
])
print(array3)

# Create Zeros
print("\nNumpy create zeros")
print(np.zeros(2))

print("\nNumpy creating ones")
print(np.ones(3))

print("Creating and empty numpy array with random values")
# This may be preferred to np.ones or np.zeros, because when creating an empty
# array with an some number of values, and it doesn't matter what those values
# are, it is faster
print(np.empty(3))

print("Using np.arange")
# np.arange acts exactly like range, except
# that it returns an array with the values
print(np.arange(4))
print(np.arange(0, 30, 2))

print("Using np.linspace")
# Returns a numpy array with the number of values specified with num evenly
# gapped, including start and stop.
print(np.linspace(9, 100, num=9))

print("Using np.sort")
input_arr = np.array([1, 5, 2, 3])
print(input_arr, np.sort(input_arr))

print("Using np.concatenate")
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 2, 1])
print(np.concatenate((arr1, arr2)))

"""
ndarray.ndim will tell you the number of axes, or dimensions, of the array.

ndarray.size will tell you the total number of elements of the array. This is
the product of the elements of the array’s shape.

ndarray.shape will display a tuple of integers that indicate the number of
elements stored along each dimension of the array. If, for example, you have a
2-D array with 2 rows and 3 columns, the shape of your array is (2, 3).
"""

arr3 = np.array([
    [1, 2],
    [4, 5],
    [3, 2]
])
print(f"Input Array: {arr3}")
print("Using array.ndin, which gives number of dimensions")
print(arr3.ndim)

print("Using array.size, which gives total number of elements")
print(arr3.size)

print("Using array.shape, which output the length of each index")
print(arr3.shape)


print("Using array.reshape")
# When reshaping an array, make sure that the reshaped array has the same
# amount of elements
# # Input Array was 3 by 2, so 6 elements
# Output Array is 2 by 3, so 6 elements
print(arr3.reshape(2, 3))

print("Using np.newaxis")
arr4 = np.array([1, 2, 3, 4, 5, 6])
arr5 = arr4[np.newaxis, :]
print(arr5)

print("Indexing and Slicing")
arr6 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(arr6[0])      # Accessing first element
print(arr6[1:3])    # Slicing
print(arr6[0:8:2])  # Slicing with step
# Using a < 5 or something similar compares each element in the array and
# returns True or False depending on whether each element satifies that
# condition
print(arr6[arr6 < 5])
print(arr6[arr6 == 5])

print("Using np.vstack and np.hstack")
a1 = np.array([
    [1, 1], [2, 2]
])
a2 = np.array([
    [3, 3], [4, 4]
])

print(np.vstack((a1, a2)))  # Stack Vertically
print(np.hstack((a1, a2)))  # Stack Horizontally

# When modifying a copy of a numpy array, make sure to use .copy()

print("Basic Array Operations")
arr1 = np.arange(10)
arr2 = np.ones(10)
arr3 = np.array([0.5]*10)
print(arr1, arr2, arr3)
print(arr1 + arr2)
print(arr1 - arr2)
print(arr1 * arr3)
print(arr1 / arr3)

# Size of arrays must be equal, or one array must have only 1 element
# You can also do there operations with one integer, the integer will
# be applied to every element in the array

# [1,3,4]
# [1,5,6]
# [2,8,10]

# [1,3,4]
# +1
# [2,4,5]

print(arr1 + 1)
print(arr1 - 1)
print(arr1 / 5)
print(arr1 * 5)

print(arr1.max())
print(arr1.min())
print(arr1.sum())

print("Generating Random Numbers")
print(np.random.random(5))
