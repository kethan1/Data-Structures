'''
---------------------------------------------
MyList - My version of the class list
Author: Kethan Vegunta
---------------------------------------------
Description:
This is my version of the python list. It is a double LinkedList, so you can
traverse the LinkedList forward or backward. You can use MyList almost exactly
like you would use a regular python list.
'''

from typing import Union, Iterable, Any


# Node of a doubly LinkedList
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


class MyList:
    '''
    Called when an instance of MyList is created.
    :param iterable - All element of the iterable are appending to MyList
    '''
    def __init__(self, iterable: Iterable = None):
        self.__head = None
        self.current = None
        self.tail = None
        if iterable is not None:
            for item in iterable:
                self.append(item)

    '''
    Adds an element to the end of MyList.
    :param data - The data that is added.
    '''
    def append(self, data):
        data = self.__toNode(data)
        if self.tail is not None:
            data.prev = self.tail
            self.tail.next = data
            self.tail = data
        else:
            self.head = data

    '''
    Inserts an element at the specified position in MyList
    :param data accepts either an instance of the class Node or some other data
    :param pos takes an integer with the position to insert the element
    '''
    def insert(self, pos: int, data):
        data = self.__toNode(data)
        if pos > len(self):
            raise IndexError("MyList assignment index out of range")
        elif pos == 0:
            if self.head is not None:
                data.next = self.head
                self.head.prev = data
                self.head = data
            else:
                self.head = data
        elif pos == len(self):
            if self.tail is not None:
                data.prev = self.tail
                self.tail.next = data
                self.tail = data
            else:
                self.head = data
        else:
            if pos < 0:
                pos = len(self)-(abs(pos)-1)
            self.current = self.head
            currentNum = 0
            while currentNum < pos-1:
                currentNum += 1
                self.current = self.current.next
            tmp = self.current.next
            data.next = tmp
            data.prev = self.current
            self.current.next = data
            if tmp is not None:
                tmp.prev = data

    '''
    Removes element depending on the data.
    :param data - The data of the element that is going to be removed.
    '''
    def remove(self, data):
        self.pop(self.index(data))

    def pop(self, pos: int):
        if pos > len(self) or pos < 0 or len(self) == 0:
            raise IndexError("delete index out of range")
        elif pos == 0:
            toReturn = self.head
            tmp = self.head.next
            self.head = tmp
            if tmp is None:
                self.tail = None
                return
            self.head.prev = None
        elif pos == len(self):
            toReturn = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            self.current = self.head
            currentNum = 0
            while currentNum < pos-1:
                currentNum += 1
                self.current = self.current.next
            toReturn = self.current.next
            tmp = self.current.next.next
            if tmp is not None:
                self.current.next = tmp
                tmp.prev = self.current
            else:
                self.current.next = tmp
        return toReturn

    '''
    # Returns the node at the specified position in MyList
    :param pos - int specifing position at which to return element
    '''

    def index(self, element_to_find):
        currentNum = 0
        for element in self:
            if element == element_to_find:
                return currentNum
            currentNum += 1

    def copy(self) -> "MyList":
        to_return_copy = MyList()
        for index in range(0, len(self)):
            to_return_copy.append(Node(self[index]))
        return to_return_copy

    def sort(self, part: "MyList" = None):
        if part is None:
            copyList = self.copy()
        else:
            copyList = part.copy()
        if len(copyList) != 1:
            middle = len(copyList)//2
            left = copyList[:middle]
            right = copyList[middle:]

            mergeSortLeft = self.sort(left)
            mergeSortRight = self.sort(right)

            current = currentLeft = currentRight = 0

            while currentLeft < len(mergeSortLeft) and currentRight < \
                    len(mergeSortRight):
                if mergeSortLeft[currentLeft] < mergeSortRight[currentRight]:
                    copyList[current] = mergeSortLeft[currentLeft]
                    currentLeft += 1
                else:
                    copyList[current] = mergeSortRight[currentRight]
                    currentRight += 1
                current += 1

            while currentLeft < len(mergeSortLeft):
                copyList[current] = mergeSortLeft[currentLeft]
                currentLeft += 1
                current += 1

            while currentRight < len(mergeSortRight):
                copyList[current] = mergeSortRight[currentRight]
                currentRight += 1
                current += 1
        if part is None:
            for index, data in enumerate(copyList):
                self[index] = data
        else:
            return copyList

    def extend(self, iterable: Iterable) -> None:
        for item in iterable:
            self.append(item)

    def count(self, itemToFind: Any) -> int:
        found = 0
        for item in self:
            if item == itemToFind:
                found += 1
        return found

    def clear(self):
        for item in self.copy():
            self.remove(item)

    def reverse(self):
        prev = None
        self.current = self.head
        self.tail = self.head
        while self.current is not None:
            next = self.current.next
            self.current.next = prev
            if prev is not None:
                prev.prev = self.current
            prev = self.current
            self.current = next
        self.head = prev

    def __toNode(self, data):
        if not isinstance(data, Node):
            return Node(data)
        return data

    def __toData(self, data):
        if isinstance(data, Node):
            return data.data
        return data

    '''
    Returns length of MyList.
    '''
    def __len__(self):
        self.current = self.head
        currentNum = 0
        if self.current is not None:
            while self.current is not None:
                if self.current.next is not None:
                    currentNum += 1
                    self.current = self.current.next
                else:
                    break
            return currentNum+1

    '''
    MyList supports item assignment: mylist_var[0] = 99
    This updates the item's data at the specified position, to the specified
    data.
    '''
    def __setitem__(self, pos: int, data):
        data = self.__toData(data)
        if pos > len(self) or pos < 0 or len(self) == 0:
            raise IndexError("update index out of range")
        elif pos == 0:
            self.head.data = data
        elif pos == len(self):
            self.tail.data = data
        else:
            self.current = self.head
            currentNum = 0
            while currentNum < pos:
                currentNum += 1
                self.current = self.current.next
            self.current.data = data

    '''
    MyList supports item indexing: mylist_var[0].
    It also supports slices, though step is not yet implemented.
    '''
    def __getitem__(self, index: Union[int, slice]) -> Union["MyList", Node]:
        if not isinstance(index, slice):
            if index > len(self) or len(self) == 0:
                raise IndexError("index out of range")
            elif index == 0:
                return self.__head.data
            elif index == len(self):
                return self.tail.data
            else:
                if index < 0:
                    index = len(self)-(abs(index)-1)
                self.current = self.head
                currentNum = 0
                while currentNum < index:
                    currentNum += 1
                    self.current = self.current.next
                return self.current.data
        else:
            start = 0 if index.start is None else index.start
            stop = len(self) if index.stop is None else index.stop
            step = 1 if index.step is None else index.step
            if start < 0:
                start = len(self)-(abs(start)-1)
            if stop < 0:
                stop = len(self)-(abs(stop)-1)
            copy_of_current_my_list = MyList()
            currentIndex = 0
            if step != 1:
                if step == 0:
                    raise ValueError("slice step cannot be zero")
                elif step < 0:
                    if step == -1:
                        step_startIndex = None
                        for element in self.DisplayAllNodes(getObj=True):
                            if start <= currentIndex < stop:
                                if step_startIndex is not None:
                                    step_startIndex = 0
                                if step_startIndex == 0:
                                    copy_of_current_my_list.insertAtEnd(
                                        Node(element.data)
                                    )
                                else:
                                    if step_startIndex % step == 0:
                                        copy_of_current_my_list.insertAtEnd(
                                            Node(element.data)
                                        )
                                step_startIndex += 1
                            currentIndex += 1
                    else:
                        self.current = self.tail
                        currentNum = len(self)-1
                        while currentNum >= 0:
                            if start <= currentIndex < stop:
                                copy_of_current_my_list.insertAtEnd(
                                    Node(self.current.data)
                                )
                            currentIndex += 1
                            self.current = self.current.prev
                        return copy_of_current_my_list
                else:
                    step_startIndex = None
                    for element in self.DisplayAllNodes(getObj=True):
                        if start <= currentIndex < stop:
                            if step_startIndex is not None:
                                step_startIndex = 0
                            if step_startIndex == 0:
                                copy_of_current_my_list.insertAtEnd(
                                    Node(element.data)
                                )
                            else:
                                if step_startIndex % step == 0:
                                    copy_of_current_my_list.insertAtEnd(
                                        Node(element.data)
                                    )
                            step_startIndex += 1
                        currentIndex += 1
                return copy_of_current_my_list
            for element in self.__iter__(getObj=True):
                if start <= currentIndex < stop:
                    copy_of_current_my_list.append(Node(element.data))
                currentIndex += 1
            return copy_of_current_my_list

    def __delitem__(self, pos: int) -> None:
        self.pop(pos)

    '''
    # Iterating Through MyList
    You can iterate through the MyList with a for loop. By default, it returns
    the data, but can pass back a Node object depending on getObj.
    :param getObj, returns the Node object instead of the data
    '''
    def __iter__(self, getObj: bool = False) -> Iterable:
        self.current = self.head
        while self.current is not None:
            if getObj:
                yield self.current
            else:
                yield self.current.data
            self.current = self.current.next

    def __add__(self, value) -> "MyList":
        copyList = self.copy()
        for item in value:
            copyList.append(item)
        return copyList

    def __radd__(self, value) -> "MyList":
        copyList = self.copy()
        for item in value:
            copyList.insert(0, item)
        return copyList

    def __mul__(self, value) -> "MyList":
        if not isinstance(value, int):
            raise TypeError(f"cannot multiple MyList by {type(value)}")
        copyList = MyList()
        for _ in range(value):
            for item in self:
                copyList.append(item)
        return copyList

    def __rmul__(self, value) -> "MyList":
        return self.__mul__(value)

    def __eq__(self, value):
        if isinstance(value, Iterable):
            to_return = True
            try:
                for index, data in enumerate(self):
                    if value[index] != data:
                        to_return = False
            except IndexError:
                return False
            return to_return
        else:
            return False

    def __str__(self) -> str:
        return f"[{', '.join(str(item) for item in self)}]"

    @property
    def head(self):
        return self.__head

    @head.setter
    def head(self, value: Any):
        self.__head = value
        if self.tail is None:
            self.tail = self.__head
