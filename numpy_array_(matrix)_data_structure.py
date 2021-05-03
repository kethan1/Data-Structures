import numpy as np

s=np.array([['Math',89,87,75],['English',75,78,83],['Science',85,89,78]])

print(s)

# Reshape
record=np.reshape(s,(4,3))
print("\nReshape:", record)

# Print By Indexes
print("\nIndexes:", s[0], s[0][0])

# Append
print(
    "\nAppend as row:", np.append(s, [[0,1,0,4]], 0),
    "\nAppend as column:", np.append(s, [[1], [2], [3]], 1), 
    "\nAppend (don't specify axis so flatten):", np.append(s, [[0,1,0,4]])
)

# Delete
print(
    "\nDelete from row:", np.delete(s, [2], 0),
    "\nDelete from column:", np.delete(s, [2], 1), 
    "\nDelete (don't specify axis so flatten and delete from as column from first row):", np.delete(s, [1])
)

# Update
s_copy = np.copy(s)
s_copy[0] = [12]
print("\nUpdate row:", s_copy)
s_copy[0][0] = "39999"
print("\nUpdate column in row:", s_copy)

