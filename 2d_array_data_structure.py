from array import *

M = [
    [89,76,93,83],
    [78,84,88,77],
    [88,72,91,78]
]

def twoD_array_print_all(array_var):
    for r in array_var:
        for c in r:
            print(c,end=" ")
        print()

twoD_array_print_all(M)
M[0][0] = 99
print("\n")
twoD_array_print_all(M)
M[0] = [1,2]
print("\n")
twoD_array_print_all(M)
M.append([1,4,2])
print("\n")
twoD_array_print_all(M)
M.insert(1, [1,223])
print("\n")
twoD_array_print_all(M)
del M[0]
print("\n")
twoD_array_print_all(M)
del M[0][0]
print("\n")
twoD_array_print_all(M)
