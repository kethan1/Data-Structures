# Creating Set 

## Using Curly braces
print({1,2,3,4})

## Using Set Function (which you pass a lest)
print(set([1,2,3,4]))

# Access Elements in Set

## You Cannot Access Elements in Set By Index, You Have to Use Loop

set1 = {1,2,3,4}
print()
for element in set1:
    print("Print All:", element)

try:
    ### This gives error
    element[0]
except:
    print("Error Caught (with try and except) When Trying to Access Set By Index")

# Add Element Using Add Method

set1.add(12)
print()
for element in set1:
    print("Add:", element)

# Remove Element Using Discard Method

set1.discard(1)
print()
for element in set1:
    print("Discard:", element)

# Union of Sets Using | (Adds all elements together, but duplicated are not add because set does not allow duplicates)

set2 = {4,2,5}
print("\nUnion:", set1|set2)

# Intersection Using & (Add Common Element and Remove Duplicates)
print("\nIntersection:", set1&set2)

# Difference Using - (Takes all elements from first one, but subtract items from second that is in first one)
print("\nDifference:", set1-set2)

# Superset Using >= and Subset using <=

quiz1=set(['Data Types','Data Type Conversion','Logic Operations'])
quiz2=set(['Data Types','Data Type Conversion','Logic Operations','String Operation'])
other = set(["Hi"])
print(quiz1 <= quiz2)
print(quiz2>=quiz1)
print(quiz2>=other)

# Length Using Len

print("\nLength:", len(set1))
