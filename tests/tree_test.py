import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parents[1].absolute()))

from tree_data_structure import Node

root = Node("Udo")
root.insert("Marc")
root[0].insert("Lian")
root[0][0].insert("Lian")
root.insert("Dan")
root[1].insert("Jet")
root[1].insert("Jan")
root[1].insert("Joe")
root.insert("Joe")

assert root.hasChildren()
assert str(root) == "Udo\n├── Marc\n│   └── Lian\n│       └── Lian\n├── Dan\n│   ├── Jet\n│   ├── Jan\n│   └── Joe\n└── Joe"
print(root)
