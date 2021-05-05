'''
---------------------------------------------
Stack - My version of the data structure stacak
Author: Kethan Vegunta
---------------------------------------------
Description:
My version of the stack. This includes the ListStack (made with a list), and Stack (made with
Nodes, similar to a LinkedList).
'''

class StackOverflow(BaseException):
    pass

# List Implementation of a Stack
class ListStack:
    '''
    Create a ListStack
    :param limit, maximum number of elements in ListStack. Default is None, which means no
    limit on number of elements. 
    '''
    def __init__(self, limit=None):
        self.stck = []
        self.limit = limit

    '''
    Adds element to end of ListStack, raises StackOverflow is there are more elements than the limit
    :param data, the data to add to the ListStack
    '''
    def Push(self, data):
        if isinstance(self.limit, int):
            if self.limit is not None and self.limit < len(self.stck)+1:
                raise StackOverflow
            self.stck.append(data)
        else:
            self.stck.append(data)

    '''
    Pops element from end of ListStack. Returns the popped element
    '''
    def Pop(self):
        last_element = self.stck[-1]
        self.stck = self.stck[:-1]
        return last_element

    '''
    Returns the last element in the ListStack
    '''
    def Top(self):
        return self.stck[-1]

    '''
    Returns the size of the ListStack
    '''
    def Size(self):
        return len(self.stck)

    '''
    Returns a boolean value (True or False) depending on whether the stack is empty
    '''
    def isEmptyStack(self):
        return not(bool(self.stck))

    '''
    Returns a boolean value (True or False) depending on whether the stack is full
    '''
    def isFullStack(self):
        if isinstance(self.limit, int):
            if self.limit == len(self.stck)+1:
                return True
        return False

    '''
    Returns size of the stack
    '''
    def __len__(self):
        return self.Size()


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

# Linked Stack
class Stack:
    '''
    Initialize method, creates Stack
    :param limit, max amount of elements in stack
    '''
    def __init__(self, limit=None):
        self.limit = limit
        self.head = None
        self.tail = None

    '''
    Used to convert data to Node if data is not already Node
    :param data, the data converted
    '''
    def __toNode(self, data):
        if isinstance(data, Node):
            return data.copy()
        return Node(data)

    '''
    Checks if stack has too many elements, and if it does, it raises StackOverflow
    '''
    def __isError(self):
        if self.limit is not None and self.limit <= self.Size():
            raise StackOverflow

    '''
    Add elements to end of stack
    :param data, element to add to stack
    '''
    def Push(self, data):
        self.__isError()
        data = self.__toNode(data)
        if self.head is None:
            self.head = data
            self.tail = data
        else:
            data.prev = self.tail
            self.tail.next = data
            self.tail = data

    '''
    Removes last element in stack, returns the element popped
    '''
    def Pop(self):
        if self.head == self.tail:
            last_element = self.head
            self.head = None
            self.tail = None
        else:
            last_element = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
        return last_element

    '''
    Returns the last element in stack
    '''
    def Top(self):
        return self.tail

    '''
    Returns the size of the stack
    '''
    def Size(self):
        self.current=self.head
        currentNum = 0
        if self.current is not None:
            while self.current.getNext() is not None:
                currentNum+=1
                self.current = self.current.getNext()
            return currentNum+1
        return currentNum

    '''
    Returns a boolean value if the stack is empty or not
    '''
    def isEmptyStack(self):
        return self.head is None

    '''
    Returns a boolean value depending on if the stack is full
    '''
    def isFullStack(self):
        if isinstance(self.limit, int):
            if self.limit == self.Size():
                return True
        return False

    '''
    Do not use this, testing only
    '''
    def showAll(self):
        self.current=self.head
        currentNum = 0
        if self.current is not None:
            while self.current.getNext() is not None:
                currentNum+=1
                yield self.current.data
                self.current = self.current.getNext()
            yield self.current.data

    '''
    Returns a copy of the stack
    '''
    def copy(self):
        newStack = Stack()
        self.current=self.head
        currentNum = 0
        if self.current is not None:
            while self.current.getNext() is not None:
                currentNum+=1
                newStack.Push(self.current.data)
                self.current = self.current.getNext()
            newStack.Push(self.current.data)
        return newStack

    def load_from_iterable(self, iterable):
        for item in iterable:
            self.Push(item)

    '''
    Returns length of Stack
    '''
    def __len__(self):
        return self.Size()

    def __repr__(self):
        return self

    def __str__(self):
        return str(list(self.showAll()))

if __name__ == "__main__":

    failed = False

    linkedstack1 = Stack()
    linkedstack1.Push("hi")
    linkedstack1.Push("hi1")
    linkedstack1.Push(1)
    print(linkedstack1)
    if not str(linkedstack1) == "['hi', 'hi1', 1]": raise ValueError
    if not linkedstack1.Pop().data == 1: raise ValueError
    print(linkedstack1)

    print("\n")

    linkedstack1 = Stack(5)
    linkedstack1.Push("1")
    linkedstack1.Push("2")
    linkedstack1.Push(1)
    linkedstack1.Push(2)
    if linkedstack1.isFullStack(): raise ValueError 
    linkedstack1.Push("3")
    if not linkedstack1.isFullStack(): raise ValueError
    try:
        linkedstack1.Push("5")
    except StackOverflow:
        print("StackOverflow raised")
    else:
        print("Failed, StackOverflow Not Raised")
        failed = True
    if not linkedstack1.Top().data == "3": raise ValueError
    print(linkedstack1)
