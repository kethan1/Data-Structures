'''
---------------------------------------------
LinkedList - My version of the class List
Author: Kethan Vegunta
---------------------------------------------
Description:
This is my version of the python list. It is a double linkedlist, so you can traverse the
linkedlist forward or backward.
'''

from typing import Union, Iterable, Any

# Node of a doubly linkedlist
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

    # return True if the node has a pointer to the next node
    def hasNext(self):
        return self.next != None

    # method for setting the next field of the node
    def setPrev(self, prevOne):
        self.prev = prevOne

    # method for getting the prev field of the node
    def getPrev(self):
        return self.prev

    # return True if the node has a pointer to the previous node
    def hasPrev(self):
        return self.prev != None

    '''
    returns a copy of the current Node's data
    if include_pointers is set to True, the pointers
    next and prev will be added to the returned node
    '''
    def copy(self, include_pointers=False):
        if include_pointers:
            to_return = Node(self.data)
            to_return.next = self.next
            to_return.prev = self.prev
            return to_return
        return Node(self.data)

class LinkedList:
    def __init__(self):
        self.__head = None
        self.current = None
        self.tail = None

    '''
    Method to display all the Nodes. Returns the data of then Node. 
    :param getObj, returns the Node object instead of the data
    '''    
    def DisplayAllNodes(self, getObj=False):
        self.current=self.head
        while self.current is not None:
            if getObj:
                yield self.current
            else:
                yield self.current.getData()
            self.current = self.current.getNext()

    '''
    Returns the length of the linkedlist
    '''
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

    '''
    # Inserts an element at the start of the linkedlist
    :param data accepts either an instance of the class Node or some other data
    '''
    def insertAtBeginning(self, data):
        if isinstance(data, Node):
            toInsert = data
        else:
            toInsert = Node(data)
        if self.head is not None:
            toInsert.next = self.head
            self.head.prev = toInsert
            self.head = toInsert
        else:
            self.head = toInsert

    '''
    # Inserts an element at the end of the linkedlist
    :oaram data accepts either an instance of the class Node or some other data
    '''
    def insertAtEnd(self, data):
        if isinstance(data, Node):
            toInsert = data
        else:
            toInsert = Node(data)
        if self.tail is not None:
            toInsert.prev = self.tail
            self.tail.next = toInsert
            self.tail = toInsert
        else:
            self.head = toInsert

    '''
    # Inserts an element at the specified position in the linkedlist
    :param data accepts either an instance of the class Node or some other data
    :param pos takes an integer with the position to insert the element
    '''
    def insertAtPos(self, pos: int, data):
        if pos > self.GetLength() or pos < 0:
            raise IndexError("linkedlist assignment index out of range")
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
            toInsert.next = tmp
            toInsert.prev = self.current
            self.current.next = toInsert
            tmp.prev = toInsert
            

    # Deleting Methods

    '''
    # Deletes the head of the linkedlist
    '''
    def deleteAtBeginning(self):
        tmp = self.head.getNext()
        if tmp == None:
            self.tail = None
        self.head = tmp
        self.head.prev = None

    '''
    # Deletes the tail of the linkedlist
    '''
    def deleteAtEnd(self):
        self.tail = self.tail.prev
        self.tail.next = None

    def deleteAtPos(self, pos: int):
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
                self.current.next = tmp
                tmp.prev = self.current
            else:
                self.current.next = tmp

    '''
    # Returns the head (as a node class) of the linkedlist
    '''
    def getAtBeginning(self):
        return self.__head

    '''
    # Returns the tail (as a node class) of the linkedlist
    '''
    def getAtEnd(self):
        return self.tail

    '''
    # Returns the node at the specified position in the linkedlist
    :param pos - int specifing position at which to return element
    '''
    def getAtPos(self, pos: int):
        if pos > self.GetLength() or self.GetLength() == 0:
            raise IndexError("index out of range")
        elif pos == 0:
            return self.__head
        elif pos == self.GetLength():
            return self.tail
        else:
            if pos < 0:
                pos = self.GetLength()-(abs(pos)-1)
            self.current=self.head
            currentNum = 0
            while currentNum < pos:
                currentNum+=1
                self.current = self.current.getNext()
            return self.current

    def updateAtBeginning(self, data):
        self.head.data = data

    def updateAtEnd(self, data):
        self.tail.data = data

    def updateAtPos(self, pos: int, data):
        if pos > self.GetLength() or pos < 0 or self.GetLength() == 0:
            raise IndexError("update index out of range")
        elif pos == 0:
            self.head.data = data
        elif pos == self.GetLength():
            self.tail.data = data
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

    def copy(self) -> "LinkedList":
        to_return_copy = LinkedList()
        to_return_copy.head = Node(self.head.data)
        for i in range(1, self.GetLength()):
            to_return_copy.insertAtEnd(Node(self.getAtPos(i).data))
        return to_return_copy

    def load_from_iterable(self, lst: Iterable):
        for element in lst:
            self.insertAtEnd(Node(element))

    '''
    Returns length of linkedlist. 
    '''
    def __len__(self):
        return self.GetLength()

    '''
    Linkedlist supports indexing: linkedlist_var[0].
    It also supports slices though step is not yet implemented. 
    '''
    def __getitem__(self, index: Union[int, slice]) -> Union["LinkedList", Node]:
        if not isinstance(index, slice):
            return self.getAtPos(index)
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

    '''
    # Iterating Through linkedlist
    You can iterate through the linkedlist with a for loop. 
    '''
    def __iter__(self) -> Iterable:
        self.current=self.head
        while self.current is not None:
            yield self.current.getData()
            self.current = self.current.getNext()

    @property
    def head(self):
        return self.__head

    @head.setter
    def head(self, value: Any):
        if isinstance(value, Node):
            self.__head = value
            if self.tail == None:
                self.tail = self.__head
        else:
            self.__head = Node(value)
            if self.tail == None:
                self.tail = self.__head
