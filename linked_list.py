# # Node of a singly linked list
# class Node:
#     # constructor
#     def __init__(self, data=None):
#          self.data = data
#          self.next = None
#     # method for setting the data field of the node
#     def setData(self, data):
#         self.data=data
#     # method for getting the data field of the node
#     def getData(self):
#         return self.data
#     # method for setting the next field of the node
#     def setNext(self, next):
#         self.next=next
#     # method for getting the next field of the node
#     def getNext(self):
#         return self.next
#     # return True if node pointer next another node
#     def hasNext(self):
#         return self.next != None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def DisplayAllNodes(self):
#         current=self.head
#         while current is not None:
#             print(current.getData())
#             current = current.getNext()

#     def GetLength(self):
#         current=self.head
#         count = 0
#         while current is not None:
#             count+=1
#             current = current.getNext()
#         return count

#     # Appending Methods

#     def insertAtBeginning(self, data):
#         toInsert = Node(data)
#         toInsert.setNext(self.head)
#         self.head = toInsert

#     def insertAtEnd(self, data):
#         toInsert = Node(data)
#         current=self.head
#         while current.getNext() is not None:
#             current = current.getNext()
#         current.setNext(toInsert)

#     def insertAtPos(self, pos, data):
#         if pos > self.GetLength() or pos < 0:
#             raise IndexError("linked list assignment index out of range")
#         elif pos == 0:
#             self.insertAtBeginning(data)
#         elif pos == self.GetLength():
#             self.insertAtEnd(data)
#         else:
#             toInsert = Node(data)
#             current=self.head
#             count = 0
#             while count < pos-1:
#                 count+=1
#                 current = current.getNext()
#             toInsert.setNext(current.getNext())
#             current.setNext(toInsert)

#     # Deleting Methods

#     def deleteAtBeginning(self):
#         tmp = self.head.getNext()
#         self.head = tmp

#     def deleteAtEnd(self):
#         current=self.head
#         while current.getNext() is not None:
#             if current.getNext().getNext():
#                 current = current.getNext()
#             else:
#                 break
#         current.setNext(None)

#     def deleteAtPos(self, pos):
#         if pos > self.GetLength() or pos < 0 or self.GetLength() == 0:
#             raise IndexError("delete index out of range")
#         elif pos == 0:
#             self.deleteAtBeginning()
#         elif pos == self.GetLength:
#             self.deleteAtEnd()
#         else:
#             current=self.head
#             count = 0
#             while count < pos-1:
#                 count+=1
#                 current = current.getNext()
#             if current.getNext().getNext() != None:
#                 tmp = current.getNext().getNext()
#                 current.setNext(tmp)
#             else:
#                 current.setNext(None)

# Homework: Add Previous like next to Node class aka doubled linked list

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
    def setNext(self, nextOne, silence=False):
        if not silence:
            try:
                self.parentClass.next = nextOne
            except:
                self.next=nextOne
        else:
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
        self.currentNum = None
        self.tail = None

    def DisplayAllNodes(self, getObj=False):
        self.current=self.head
        self.currentNum = 0
        while self.current is not None:
            if getObj:
                yield self.current
            else:
                yield self.current.getData()
            self.current = self.current.getNext()
            self.currentNum += 1

    def GetLength(self):
        self.current=self.head
        self.currentNum = 0
        while self.current is not None:
            if self.current.getNext() is not None:
                self.currentNum+=1
                self.current = self.current.getNext()
            else: break
        return self.currentNum+1

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
        self.tail.setNext(toInsert, silence=True)
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
            while self.currentNum != pos-1:
                if self.currentNum < pos-1:
                    self.currentNum+=1
                    self.current = self.current.getNext()
                elif self.currentNum > pos-1:
                    self.currentNum-=1
                    self.current = self.current.prev
            toInsert.setNext(self.current.getNext(), silence=True)
            toInsert.prev = self.current
            self.current.getNext().prev = toInsert
            self.current.setNext(toInsert, silence=True)

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
            while self.currentNum != pos-1:
                if self.currentNum < pos-1:
                    self.currentNum+=1
                    self.current = self.current.getNext()
                elif self.currentNum > pos-1:
                    self.currentNum-=1
                    self.current = self.current.prev
            tmp = self.current.getNext().getNext()
            self.current.setNext(tmp, silence=True)
            tmp.prev = self.current

    @property
    def head(self):
        return self._head
    
    @property
    def next(self):
        return self.tail.getNext()

    @head.setter
    def head(self, value):
        self._head = value
        if self.tail == None:
            self.tail = self.head
            self.tail.parentClass = self

    @next.setter
    def next(self, value):
        if self.tail != None:
            if value != None:
                if isinstance(value, Node):
                    self.tail.setNext(value, silence=True)
                else:
                    self.tail.setNext(Node(value), silence=True)
                oldtail = self.tail
                self.tail = self.tail.getNext()
                if self.head != self.tail:
                    self.tail.prev = oldtail
                self.tail.parentClass = self

linkedlist1 = LinkedList()
linkedlist1.head = Node(1)
print("Last Element:", linkedlist1.tail.getData())
linkedlist1.tail.setNext(Node("2"))
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
linkedlist1.next = Node("4")
print("Last Element:", linkedlist1.tail.getData())
linkedlist1.deleteAtEnd()
print("Last Element:", linkedlist1.tail.getData())
print("Length:", linkedlist1.GetLength())
print(list(linkedlist1.DisplayAllNodes()))
