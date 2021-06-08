import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from set_data_structure import MySet
from class_for_testing import TestClass


def test_condition(condition):
    if not condition: raise ValueError

mySet1 = MySet((1, 2, 3))
print(f"After Creating with Iterable As Init Arg: {mySet1}")
test_condition(mySet1.return_as_python_set() == {1, 2, 3})
mySet1.add("hi")
mySet1.add(1)
print(f"After Adding 1 and 'hi': {mySet1}")
test_condition(mySet1.return_as_python_set() == {1, 2, 3, "hi"})
mySet1.remove(1)
print(f"After Removing 1: {mySet1}")
test_condition(mySet1.return_as_python_set() == {2, 3, "hi"})
mySet1.update((1, 2, 3))
print(f"After updating with (1,2,3): {mySet1}")
test_condition(mySet1.return_as_python_set() == {2, 3, "hi", 1})
mySet1.update((4, 2, 3))
print(f"After updating with (4,2,3): {mySet1}")
test_condition(mySet1.return_as_python_set() == {2, 4, 3, "hi", 1})
mySet1.add(TestClass(8, 2, 4))
print(f"After adding TestClass where x=8, y=2, z=4: {mySet1}")
for element in mySet1:
    if element not in {2, 4, 3, "hi", 1}:
        if isinstance(element, TestClass):
            if element.x != 8 or element.y != 2 or element.z != 4:
                raise ValueError
        else:
            raise ValueError
 