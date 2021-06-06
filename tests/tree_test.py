import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from tree_data_structure import Node

root = Node("Languages Good For")
root.insert("Serverside Web Development")
root.insert("For Speed")
root[0].insert("Python")
root[0].insert("NodeJS")
root[0].insert("Ruby")
root[0].insert("PHP")
root[0].insert("C")
root[0].insert("C++")
root[0].insert("Java")
root[0].insert("C#")
root[0][0].insert("Flask")
root[0][0].insert("Django")
root[0][2].insert("Ruby on Rails")
root[0][0][0].insert(1.1)
root[0][0][0].insert(2.0)
root[0][0][0][0].insert("1.0.1")
root[0][0][0][1].insert("2.0.1")
root[0][0][0][1].insert("2.0.0")

# if not str(root) == "                               Languages Good For\n                     Serverside Web Development                         For Speed\n          Python             NodeJS      Ruby  PHP  C  C++  Java  C#  \n       Flask         Django  Ruby on Rails    \n 1.1       2.0             \n1.0.1  2.0.1  2.0.0        ":  raise ValueError
print(root)
"""
Udo
├── Marc
│   └── Lian
└── Dan
    ├── Jet
    ├── Jan
    └── Joe
"""
