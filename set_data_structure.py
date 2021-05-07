'''
---------------------------------------------
MySet - My version of the class Set
Author: Kethan Vegunta
---------------------------------------------
Description:
My version of the python set. It's syntax is very similar to a regular python set. 
'''

import pickle

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
        setattr(self, self.__convert_item_to_str(item), True)

    '''
    Clears the set. Removes all items. 
    '''
    def clear(self):
        for item in self:
            delattr(self, item)

    '''
    Adds item from another set. Duplicate items will be ignored. 
    '''
    def update(self, otherSet):
        for item in otherSet:
            self.add(item)

    '''
    Removes item from set. AttributeError is item not found. 
    '''
    def remove(self, item):
        delattr(self, self.__convert_item_to_str(item))

    '''
    Similar to remove, but will not raise error if item not found. 
    '''
    def discard(self, item):
        if hasattr(self, self.__convert_item_to_str(item)):
            delattr(self, self.__convert_item_to_str(item))

    def __convert_item_to_str(self, item):
        return pickle.dumps(item).decode('unicode_escape')

    def __convert_str_to_item(self, item):
        return pickle.loads(item.encode('utf-8', 'unicode_escape').replace(b'\xc2', b''))

    def __str__(self):
        to_return = []
        for item in list(vars(self)):
            to_return.append(str(self.__convert_str_to_item(item)))
        return "{" + ', '.join(to_return) + "}"

    def return_as_python_set(self):
        return {item for item in self}
    
    '''
    Iterable through the set with a for loop. 
    '''
    def __iter__(self):
        for item in list(vars(self)):
            yield self.__convert_str_to_item(item)
