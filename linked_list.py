# Node of a singly linked list
class Node:
    # constructor
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None
    # method for setting the data field of the node
    def setData(self, data):
        self.data=data
    # method for getting the data field of the node
    def getData(self):
        return self.data
    # method for setting the next field of the node
    def setNext(self, nextOne):
        self.next=nextOne
    # method for getting the next field of the node
    def getNext(self):
        return self.next
    # return True if node pointer next another node
    def hasNext(self):
        return self.next != None

class LinkedList:
    def __init__(self):
        self._head = None
        self.current = None
        self.tail = None

    def DisplayAllNodes(self, getObj=False):
        self.current=self.head
        while self.current is not None:
            if getObj:
                yield self.current
            else:
                yield self.current.getData()
            self.current = self.current.getNext()

    def GetLength(self):
        self.current=self.head
        currentNum = 0
        while self.current is not None:
            if self.current.getNext() is not None:
                currentNum+=1
                self.current = self.current.getNext()
            else: break
        return currentNum+1

    # Appending Methods

    def insertAtBeginning(self, data):
        if isinstance(data, Node):
            toInsert = data
        else:
            toInsert = Node(data)
        toInsert.setNext(self.head)
        self.head.prev = toInsert
        self.head = toInsert

    def insertAtEnd(self, data):
        if isinstance(data, Node):
            toInsert = data
        else:
            toInsert = Node(data)
        self.tail.setNext(toInsert)
        toInsert.prev = self.tail
        self.tail = toInsert

    def insertAtPos(self, pos, data):
        if pos > self.GetLength() or pos < 0:
            raise IndexError("linked list assignment index out of range")
        elif pos == 0:
            self.insertAtBeginning(data)
        elif pos == self.GetLength():
            self.insertAtEnd(data)
        else:
            if isinstance(data, Node):
                toInsert = data
            else:
                toInsert = Node(data)
            self.current=self.head
            currentNum = 0
            while currentNum < pos-1:
                currentNum+=1
                self.current = self.current.getNext()
            toInsert.setNext(self.current.getNext().getNext())
            toInsert.prev = self.current
            self.current.setNext(toInsert)

    # Deleting Methods

    def deleteAtBeginning(self):
        tmp = self.head.getNext()
        if tmp == None:
            self.tail = None
        self.head = tmp
        self.head.prev = None

    def deleteAtEnd(self):
        self.tail = self.tail.prev
        self.tail.setNext(None)

    def deleteAtPos(self, pos):
        if pos > self.GetLength() or pos < 0 or self.GetLength() == 0:
            raise IndexError("delete index out of range")
        elif pos == 0:
            self.deleteAtBeginning()
        elif pos == self.GetLength():
            self.deleteAtEnd()
        else:
            self.current=self.head
            currentNum = 0
            while currentNum < pos-1:
                currentNum+=1
                self.current = self.current.getNext()
            tmp = self.current.getNext().getNext()
            self.current.setNext(tmp)
            tmp.prev = self.current

    @property
    def head(self):
        return self._head

    @head.setter
    def head(self, value):
        self._head = value
        if self.tail == None:
            self.tail = self.head
            self.tail.parentClass = self

# Testing
linkedlist1 = LinkedList()
linkedlist1.head = Node(1)
print("Last Element:", linkedlist1.tail.getData())
linkedlist1.insertAtEnd(Node("2"))
print("Last Element:", linkedlist1.tail.getData())
print("Length:", linkedlist1.GetLength())
linkedlist1.insertAtEnd("3")
print(list(linkedlist1.DisplayAllNodes()))
linkedlist1.insertAtPos(1, 39)
print("Last Element:", linkedlist1.tail.getData())
print("Length:", linkedlist1.GetLength())
print(list(linkedlist1.DisplayAllNodes()))
linkedlist1.deleteAtPos(1)
print(list(linkedlist1.DisplayAllNodes()))
print("Last Element:", linkedlist1.tail.getData())
linkedlist1.insertAtEnd(Node("4"))
print("Last Element:", linkedlist1.tail.getData())
linkedlist1.deleteAtEnd()
print("Last Element:", linkedlist1.tail.getData())
print("Length:", linkedlist1.GetLength())
print(list(linkedlist1.DisplayAllNodes()))
