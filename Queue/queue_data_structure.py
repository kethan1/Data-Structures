class QueueOverflow(BaseException):
    pass


# Node of a doubly linkedlist
class Node:
    # constructor
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

    # method for setting the data field of the node
    def setData(self, data):
        self.data = data

    # method for getting the data field of the node
    def getData(self):
        return self.data

    # method for setting the next field of the node
    def setNext(self, nextOne):
        self.next = nextOne

    # method for getting the next field of the node
    def getNext(self):
        return self.next

    # return True if the node has a pointer to the next node
    def hasNext(self):
        return self.next is not None

    # method for setting the next field of the node
    def setPrev(self, prevOne):
        self.prev = prevOne

    # method for getting the prev field of the node
    def getPrev(self):
        return self.prev

    # return True if the node has a pointer to the previous node
    def hasPrev(self):
        return self.prev is not None

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


# Linked Queue
class Queue:
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
    Checks if stack has too many elements, and if it does, it raises
    StackOverflow
    '''
    def __isError(self):
        if self.limit is not None and self.limit <= self.Size():
            raise QueueOverflow

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
            to_return = self.head
            self.head = None
            self.tail = None
        else:
            to_return = self.head
            self.head = self.head.next
            self.head.prev = None
        return to_return

    '''
    Returns the last element in stack
    '''
    def Front(self):
        return self.head

    '''
    Returns the size of the stack
    '''
    def Size(self):
        self.current = self.head
        currentNum = 0
        if self.current is not None:
            while self.current.getNext() is not None:
                currentNum += 1
                self.current = self.current.getNext()
            return currentNum+1
        return currentNum

    '''
    Returns a boolean value if the stack is empty or not
    '''
    def isEmptyQueue(self):
        return self.head is None

    '''
    Returns a boolean value depending on if the stack is full
    '''
    def isFullQueue(self):
        if isinstance(self.limit, int):
            if self.limit == self.Size():
                return True
        return False

    '''
    Do not use this, testing only
    '''
    def showAll(self):
        self.current = self.head
        currentNum = 0
        if self.current is not None:
            while self.current.getNext() is not None:
                currentNum += 1
                yield self.current.data
                self.current = self.current.getNext()
            yield self.current.data

    '''
    Returns a copy of the stack
    '''
    def copy(self):
        newStack = Queue()
        self.current = self.head
        currentNum = 0
        if self.current is not None:
            while self.current.getNext() is not None:
                currentNum += 1
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
