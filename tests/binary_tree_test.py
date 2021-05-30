import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

from binary_tree import Node

root = Node(9)
root.set_left(11)
root.set_right(6)
root.left.set_left(120)
root.left.set_right(10)
root.right.set_left(120)
print(root)
if not str(root) == '       9\n  11        6   \n120  10    120  ':
    raise ValueError