import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from dictionary_data_structure import MyDict

myDict1 = MyDict()
myDict1["key1"] = "value1"
print(myDict1["key1"])
if not myDict1["key1"] == "value1": raise ValueError
print(f"Keys: {myDict1.keys()}")
print(f"Values: {myDict1.values()}")
print(f"Items: {myDict1.items()}")
if not myDict1.keys() == {'key1'}: raise ValueError
if not myDict1.values() == {'value1'}: raise ValueError
if not myDict1.items() == {('key1', 'value1')}: raise ValueError
myDict1.update({"1": "9", "key2": "value2"})
print(f"MyDict after update: {myDict1.items()}")
if not myDict1.items() == {('1', '9'), ('key2', 'value2'), ('key1', 'value1')}: raise ValueError
print(f"MyDict Copy: {myDict1.copy().items()}")
if not myDict1.copy().items() == {('1', '9'), ('key1', 'value1'), ('key2', 'value2')}: raise ValueError
myDict1.pop("1")
print(f"MyDict after deleting key 1: {myDict1.items()}")
if not myDict1.items() == {('key1', 'value1'), ('key2', 'value2')}: raise ValueError
myDict1.clear()
print(f"MyDict Cleared: {myDict1.items()}")
if myDict1.items(): raise ValueError