import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from stack_data_structure import Stack, StackOverflow

linkedstack1 = Stack()
linkedstack1.Push("hi")
linkedstack1.Push("hi1")
linkedstack1.Push(1)
print(linkedstack1)
if not str(linkedstack1) == "['hi', 'hi1', 1]": raise ValueError
if not linkedstack1.Pop().data == 1: raise ValueError
print(linkedstack1)

print("\n")

linkedstack1 = Stack(5)
linkedstack1.Push("1")
linkedstack1.Push("2")
linkedstack1.Push(1)
linkedstack1.Push(2)
if linkedstack1.isFullStack(): raise ValueError 
linkedstack1.Push("3")
if not linkedstack1.isFullStack(): raise ValueError
try:
    linkedstack1.Push("5")
except StackOverflow:
    print("StackOverflow raised")
else:
    print("Failed, StackOverflow Not Raised")
    raise ValueError
if not linkedstack1.Top().data == "3": raise ValueError
print(linkedstack1)