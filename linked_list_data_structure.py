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
    def setPrev(self, prevOne):
        self.prev = prevOne
    # method for getting the next field of the node
    def getNext(self):
        return self.next
    def getPrev(self):
        return self.prev
    # return True if node pointer next another node
    def hasNext(self):
        return self.next != None

    def copy(self):
        return Node(self.data)

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
        if self.head is not None:
            toInsert.setNext(self.head)
            self.head.prev = toInsert
            self.head = toInsert
        else:
            self.head = toInsert

    def insertAtEnd(self, data):
        if isinstance(data, Node):
            toInsert = data
        else:
            toInsert = Node(data)
        if self.tail is not None:
            self.tail.setNext(toInsert)
            toInsert.prev = self.tail
            self.tail = toInsert
        else:
            self.head = toInsert

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
            tmp = self.current.getNext()
            toInsert.setNext(tmp)
            toInsert.prev = self.current
            self.current.setNext(toInsert)
            tmp.prev = toInsert
            

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
            if tmp is not None:
                self.current.setNext(tmp)
                tmp.prev = self.current
            else:
                self.current.setNext(tmp)

    def GetAtBeginning(self):
        return self._head

    def GetAtEnd(self):
        return self.tail

    def GetAtPos(self, pos):
        if pos > self.GetLength() or self.GetLength() == 0:
            raise IndexError("index out of range")
        elif pos == 0:
            return self._head
        elif pos == self.GetLength():
            return self.tail
        else:
            if pos < 0:
                pos = self.GetLength()-(abs(pos)-1)
            self.current=self.head
            currentNum = 0
            while currentNum < (self.GetLength()-(abs(pos)-1)):
                currentNum+=1
                self.current = self.current.getNext()
            return self.current

    def UpdateAtBeginning(self, data):
        self.head.data = data

    def UpdateAtEnd(self, data):
        self.tail.data = data

    def UpdateAtPos(self, pos, data):
        if pos > self.GetLength() or pos < 0 or self.GetLength() == 0:
            raise IndexError("update index out of range")
        elif pos == 0:
            return self.UpdateAtBeginning(data)
        elif pos == self.GetLength():
            return self.UpdateAtEnd(data)
        else:
            self.current=self.head
            currentNum = 0
            while currentNum < pos:
                currentNum+=1
                self.current = self.current.getNext()
            self.current.data = data

    def index(self, element_to_find):
        currentNum = 0
        for element in self.DisplayAllNodes():
            if element == element_to_find:
                return currentNum
            currentNum+=1

    def copy(self):
        to_return_copy = LinkedList()
        to_return_copy.head = Node(self.head.data)
        for i in range(1, self.GetLength()):
            to_return_copy.insertAtEnd(Node(self.GetAtPos(i).data))
        return to_return_copy

    def load_from_list(self, lst):
        for element in lst:
            self.insertAtEnd(Node(element))

    def __len__(self):
        return self.GetLength()

    def __getitem__(self, index):
        if not isinstance(index, slice):
            return self.GetAtPos(index)
        else:
            start = 0 if index.start is None else index.start
            stop = self.GetLength() if index.stop is None else index.stop
            step = 1 if index.step is None else index.step
            if start < 0:
                start = self.GetLength()-(abs(start)-1)
            if stop < 0:
                stop = self.GetLength()-(abs(stop)-1)
            copy_of_current_linked_list = LinkedList()
            currentIndex = 0
            if step != 1:
                if step == 0:
                    raise ValueError("slice step cannot be zero")
                elif step < 0:
                    if step == -1:
                        step_startIndex = None
                        for element in self.DisplayAllNodes(getObj=True):
                            if start <= currentIndex < stop:
                                if step_startIndex == None:
                                    step_startIndex = 0
                                if step_startIndex == 0:
                                    copy_of_current_linked_list.insertAtEnd(Node(element.data))
                                else:
                                    if step_startIndex%step == 0:
                                        copy_of_current_linked_list.insertAtEnd(Node(element.data))
                                step_startIndex+=1
                            currentIndex+=1
                    else:
                        self.current = self.tail
                        currentNum = self.GetLength()-1
                        while currentNum >= 0:
                            if start <= currentIndex < stop:
                                copy_of_current_linked_list.insertAtEnd(Node(self.current.data))
                            currentIndex+=1
                            self.current = self.current.getPrev()
                        return copy_of_current_linked_list
                else:
                    step_startIndex = None
                    for element in self.DisplayAllNodes(getObj=True):
                        if start <= currentIndex < stop:
                            if step_startIndex == None:
                                step_startIndex = 0
                            if step_startIndex == 0:
                                copy_of_current_linked_list.insertAtEnd(Node(element.data))
                            else:
                                if step_startIndex%step == 0:
                                    copy_of_current_linked_list.insertAtEnd(Node(element.data))
                            step_startIndex+=1
                        currentIndex+=1
                return copy_of_current_linked_list
            for element in self.DisplayAllNodes(getObj=True):
                if start <= currentIndex < stop:
                    copy_of_current_linked_list.insertAtEnd(Node(element.data))
                currentIndex+=1
            return copy_of_current_linked_list

    def __iter__(self):
        self.current=self.head
        while self.current is not None:
            yield self.current.getData()
            self.current = self.current.getNext()

    @property
    def head(self):
        return self._head

    @head.setter
    def head(self, value):
        if isinstance(value, Node):
            self._head = value
            if self.tail == None:
                self.tail = self._head
        else:
            self._head = Node(value)
            if self.tail == None:
                self.tail = self._head

# Testing
# linkedlist1 = LinkedList()
# linkedlist1.head = Node(1)
# print("Last Element:", linkedlist1.tail.getData())
# linkedlist1.insertAtEnd(Node("2"))
# print("Last Element:", linkedlist1.tail.getData())
# print("Length:", linkedlist1.GetLength())
# linkedlist1.insertAtEnd("3")
# print(list(linkedlist1.DisplayAllNodes()))
# linkedlist1.insertAtPos(1, 39)
# print("Last Element:", linkedlist1.tail.getData())
# print("Length:", linkedlist1.GetLength())
# print(list(linkedlist1.DisplayAllNodes()))
# linkedlist1.deleteAtPos(1)
# print(list(linkedlist1.DisplayAllNodes()))
# print("Last Element:", linkedlist1.tail.getData())
# linkedlist1.insertAtEnd(Node("4"))
# print("Last Element:", linkedlist1.tail.getData())
# linkedlist1.deleteAtEnd()
# print("Last Element:", linkedlist1.tail.getData())
# print("Length:", linkedlist1.GetLength())
# print(list(linkedlist1.DisplayAllNodes()))
