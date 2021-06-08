from list_data_structure import MyList

myList1 = MyList([1, 3, 2, 4, 5, 6])  # Can create using iterable

print(myList1)
myList1.append(10)
print(f"Appended 10: {myList1}")
myList1.insert(2, 12)
print(f"Inserted 12 at position 2: {myList1}")
myList1.remove(6)
print(f"Removed 6: {myList1}")
myList1.pop(0)
print(f"Popped the element from index 0: {myList1}")
del myList1[0]
print(f"Deleted element in position 0 with del keyword: {myList1}")
print(f"Get element in position 0: {myList1[0]}")
print(f"Get elements from 0 to 2: {myList1[0:2]}")
myList1.reverse()
print(f"Reversed the list: {myList1}")
print(f"Copied the list: {myList1.copy()}")
print(f"Got the index of element 4: {myList1.index(4)}")
print(myList1)
myList1.extend(MyList([1, 4, 2, 6]))
print(f"Extended the list with [1,4,2,6]: {myList1}")
print(myList1.count(4))
myList1.sort()
print(myList1)
myList1.clear()
print(myList1)

nested_linked_list = MyList([1, 2, 3, MyList([1, 3, 24])])
print(nested_linked_list[3][1])
print(nested_linked_list)
