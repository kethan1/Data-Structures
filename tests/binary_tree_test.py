import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parents[1].absolute()))

from binary_tree import Node

root = Node(9)
root.set_left(11)
root.set_right(6)
root.left.set_left(120)
root.left.set_right(10)
root.right.set_left(120)
assert root.hasChildren()
print(root)
assert str(root) == '       9\n  11        6   \n120  10    120  '
