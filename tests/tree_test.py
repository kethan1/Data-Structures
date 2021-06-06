import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

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

if not str(root) == "Udo\n├── Marc\n│   └── Lian\n│       └── Lian\n├── Dan\n│   ├── Jet\n│   ├── Jan\n│   └── Joe\n└── Joe":  raise ValueError

print(root)
