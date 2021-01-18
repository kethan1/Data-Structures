from array import *
array1 = array('i', [1, 2, 3])

# Array Types:
# Typecode |                  Value 
# ---------|-------------------------------------|
#     b    |   signed integer size 1 bytes/td>   |
# ---------|-------------------------------------|
#     B    |   unsigned integer of size 1 byte   |
# ---------|-------------------------------------|
#     c    |      character of size 1 byte       |
# ---------|-------------------------------------|
#     i    |   signed integer of size 2 bytes    |
# ---------|-------------------------------------|
#     I    |   unsigned integer of size 2 bytes  |
# ---------|-------------------------------------|
#     f    |   floating point of size 4 bytes    |
# ---------|-------------------------------------|
#     d    |   floating point of size 8 bytes    |
# ---------|-------------------------------------|

array1[1] = -1
print(array1[1])
print(array1.index(1))
array1.insert(2,6)
array1.remove(3)
print(array1)

for x in array1:
    print(x)