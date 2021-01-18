# Node of a singly linked list
class Node:
    # constructor
    def __init__(self, data=None):
         self.data = data
         self.next = None
    # method for setting the data field of the node
    def setData(self, data):
         self.data=data
    # method for getting the data field of the node
    def getData(self):
         return self.data
    # method for setting the next field of the node
    def setNext(self, next):
         self.next=next
    # method for getting the next field of the node
    def getNext(self):
         return self.next
    # return True if node pointer next another node
    def hasNext(self):
         return self.next != None

class LinkedList:
    def __init__(self):
        self.head = None

    def DisplayAllNodes(self):
        current=self.head
        while current is not None:
            print(current.getData())
            current = current.getNext()

    def GetLength(self):
        current=self.head
        count = 0
        while current is not None:
            count+=1
            current = current.getNext()
        return count

    # Appending Methods

    def insertAtBeginning(self, data):
        toInsert = Node(data)
        toInsert.setNext(self.head)
        self.head = toInsert

    def insertAtEnd(self, data):
        toInsert = Node(data)
        current=self.head
        while current.getNext() is not None:
            current = current.getNext()
        current.setNext(toInsert)

    def insertAtPos(self, pos, data):
        if pos > self.GetLength() or pos < 0:
            raise IndexError("linked list assignment index out of range")
        elif pos == 0:
            self.insertAtBeginning(data)
        elif pos == self.GetLength():
            self.insertAtEnd(data)
        else:
            toInsert = Node(data)
            current=self.head
            count = 0
            while count < pos-1:
                count+=1
                current = current.getNext()
            toInsert.setNext(current.getNext())
            current.setNext(toInsert)

    # Deleting Methods

    def deleteAtBeginning(self):
        tmp = self.head.getNext()
        self.head = tmp

    def deleteAtEnd(self):
        current=self.head
        while current.getNext() is not None:
            if current.getNext().getNext():
                current = current.getNext()
            else:
                break
        current.setNext(None)

    def deleteAtPos(self, pos):
        if pos > self.GetLength() or pos < 0 or self.GetLength() == 0:
            raise IndexError("delete index out of range")
        elif pos == 0:
            self.deleteAtBeginning()
        elif pos == self.GetLength:
            self.deleteAtEnd()
        else:
            current=self.head
            count = 0
            while count < pos-1:
                count+=1
                current = current.getNext()
            if current.getNext().getNext() != None:
                tmp = current.getNext().getNext()
                current.setNext(tmp)
            else:
                current.setNext(None)
