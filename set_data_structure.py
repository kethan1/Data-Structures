'''
---------------------------------------------
MySet - My version of the class Set
Author: Kethan Vegunta
---------------------------------------------
Description:
My version of the python set. It's syntax is very similar to a regular python set. 
'''

class MySet:

    '''
    Creates a set. Pass a iterable and it will add those elements to the set
    '''
    def __init__(self, iterable=None):
        if iterable is not None:
            for item in iterable:
                self.add(item)

    '''
    Add an item to the set. Take an argument item, which is the item to be inserted. Duplicate
    items will be ignored
    '''
    def add(self, item):
        setattr(self, str(item), True)

    '''
    Clears the set. Removes all items. 
    '''
    def clear(self):
        for item in self:
            delattr(self, str(item))

    '''
    Adds item from another set. Duplicate items will be ignored. 
    '''
    def update(self, otherSet):
        for item in otherSet:
            setattr(self, str(item), True)

    '''
    Removes item from set. AttributeError is item not found. 
    '''
    def remove(self, item):
        delattr(self, str(item))

    '''
    Similar to remove, but will not raise error if item not found. 
    '''
    def discard(self, item):
        if hasattr(self, str(item)):
            delattr(self, str(item))
    
    '''
    Iterable through the set with a for loop. 
    '''
    def __iter__(self):
        for item in list(vars(self)):
            yield item

mySet1 = MySet((1,2,3))
mySet1.add("hi")
mySet1.add(1)
for i in mySet1:
    print(i)
print()
mySet1.remove(1)
mySet1.update((1,2,3))
for i in mySet1:
    print(i)
