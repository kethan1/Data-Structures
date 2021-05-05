import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

from linked_list_data_structure import LinkedList, Node

linkedlist1 = LinkedList()
linkedlist1.head = Node(1)
print("Last Element:", linkedlist1.tail.getData())
assert linkedlist1.tail.getData() == 1
linkedlist1.insertAtEnd("2")
print("Last Element:", linkedlist1.tail.getData())
assert linkedlist1.tail.getData() == "2"
print("Length:", linkedlist1.GetLength())
assert linkedlist1.GetLength() == 2
linkedlist1.insertAtEnd("3")
print(list(linkedlist1.DisplayAllNodes()))
assert list(linkedlist1.DisplayAllNodes()) == [1, "2", "3"]
linkedlist1.insertAtPos(1, 4)
print("Last Element:", linkedlist1.tail.getData())
assert linkedlist1.tail.getData() == "3"
print("Length:", linkedlist1.GetLength())
assert linkedlist1.GetLength() == 4
print(list(linkedlist1.DisplayAllNodes()))
assert list(linkedlist1.DisplayAllNodes()) == [1, 4, "2", "3"]
linkedlist1.deleteAtPos(1)
print(list(linkedlist1.DisplayAllNodes()))
assert list(linkedlist1.DisplayAllNodes()) == [1, "2", "3"]
print("Last Element:", linkedlist1.tail.getData())
assert linkedlist1.tail.getData() == "3"
linkedlist1.insertAtEnd(Node("5"))
print("Last Element:", linkedlist1.tail.getData())
assert linkedlist1.tail.getData() == "5"
linkedlist1.deleteAtEnd()
print("Last Element:", linkedlist1.tail.getData())
assert linkedlist1.tail.getData() == "3"
print("Length:", linkedlist1.GetLength())
assert linkedlist1.GetLength() == 3
print(list(linkedlist1.DisplayAllNodes()))
assert list(linkedlist1.DisplayAllNodes()) == [1, "2", "3"]