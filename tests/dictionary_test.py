import os
import sys
import inspect

sys.path.insert(0, os.path.dirname(
        os.path.dirname(
            os.path.abspath(inspect.getfile(inspect.currentframe()))
        )
    )
)

from dictionary_data_structure import MyDict
from class_for_testing import TestClass


myDict1 = MyDict()
myDict1["key1"] = "value1"
print(myDict1["key1"])
assert myDict1["key1"] == "value1"
print(f"Keys: {myDict1.keys()}")
print(f"Values: {myDict1.values()}")
print(f"Items: {myDict1.items()}")
assert myDict1.keys() == {'key1'}
assert myDict1.values() == {'value1'}
assert myDict1.items() == {('key1', 'value1')}
myDict1.update({1: 9, TestClass(11): "value2"})
print(f"MyDict after update: {myDict1.items()}")


def compare(d1, d2, n):
    for item in d1:
        if item not in d2:
            TestClass_found = False
            for item2 in item:
                if isinstance(item2, TestClass):
                    TestClass_found = True
                    if item2.x != n:
                        raise AssertionError
            if not TestClass_found:
                raise AssertionError
    for item in d2:
        if item not in d1:
            TestClass_found = False
            for item2 in item:
                if isinstance(item2, TestClass):
                    TestClass_found = True
            if not TestClass_found:
                raise AssertionError


compare(myDict1.items(), {(1, 9), (TestClass(11), 'value2'), ('key1', 'value1')}, 11)
print(f"MyDict Copy: {myDict1.copy().items()}")
compare(myDict1.copy().items(), {(1, 9), (TestClass(11), 'value2'), ('key1', 'value1')}, 11)
myDict1.pop(1)
print(f"MyDict after deleting key 1: {myDict1.items()}")
compare(myDict1.items(), {(TestClass(11), 'value2'), ('key1', 'value1')}, 11)
myDict1.clear()
print(f"MyDict Cleared: {myDict1.items()}")
assert myDict1.items() == set()
