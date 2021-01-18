from array import *
array1 = array('i', [1, 2, 3])

array1[1] = -1
print(array1[1])
print(array1.index(1))
array1.insert(2,6)
array1.remove(3)
print(array1)

for x in array1:
    print(x)