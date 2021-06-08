import os
import sys
import inspect

sys.path.insert(0, os.path.dirname(
        os.path.dirname(
            os.path.abspath(inspect.getfile(inspect.currentframe()))
        )
    )
)

from binary_tree import Node

root = Node(9)
root.set_left(11)
root.set_right(6)
root.left.set_left(120)
root.left.set_right(10)
root.right.set_left(120)
print(root)
assert str(root) == '       9\n  11        6   \n120  10    120  '
