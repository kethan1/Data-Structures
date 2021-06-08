from array import array

# Array Types:
# Typecode |                  Value
# ---------|-------------------------------------|
#     b    |   signed integer size 1 bytes       |
# ---------|-------------------------------------|
#     B    |   unsigned integer of size 1 byte   |
# ---------|-------------------------------------|
#     i    |   signed integer of size 2 bytes    |
# ---------|-------------------------------------|
#     I    |   unsigned integer of size 2 bytes  |
# ---------|-------------------------------------|
#     f    |   floating point of size 4 bytes    |
# ---------|-------------------------------------|
#     d    |   floating point of size 8 bytes    |
# ---------|-------------------------------------|

'''
Signed integers allow that negative numbers.

b is an signed integer of 1 byte.
This means that when an array uses typecode b, numbers in the range of -128 to
127 are allowed.

B is an unsigned integer of 1 byte.
This means that when an array uses typecode B, numbers in the range of 0 to
255 are allowed.

i is a signed integer of 2 bytes (larger).
This means that when an array uses typecode i, numbers in the range of
-2147483648 to 2147483647 are allowed.

I is an unsigned integer of 2 bytes (larger).
This means that when an array uses typecode I, numbers in the range of 0 to
4294967295 are allowed.

f is a floating point number of 4 bytes.

If you need larger floating point numbers, you can use d, floating point
numbers of 8 bytes.
'''
array1 = array('b', [127, -128, 99, 81])
array2 = array('B', [255, 99, 81, 0])
array3 = array('i', [2147483647, 21474836, -2147483648, 81])
array4 = array('I', [4294967295, 1023910293])
array5 = array('f', [-112.1, -1.1231])
array6 = array('d', [-1123.1, 1023910293])
