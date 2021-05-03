'''
---------------------------------------------
MyDict - My version of the class Dictionary
Author: Kethan Vegunta
---------------------------------------------
Description:
My version of the python dictionary. It's syntax is very similar to a regular python dict. 
'''


class MyDict:
    '''
    Create MyDict object:
    myDict1 = MyDict()
    '''
    def __init__(self):
        pass

    '''
    Get Item:
    myDict1["hi"]
    '''
    def __getitem__(self, key):
        return getattr(self, str(key))

    '''
    Set Item:
    myDict1["hi"] = 1
    '''
    def __setitem__(self, key, value):
        setattr(self, str(key), value)

    '''
    Delete Item:
    del myDict1["hi"]
    or
    myDict1.pop("hi")
    '''
    def __delitem__(self, key):
        delattr(self, str(key))

    '''
    Iterate Through MyDict:
    for key in myDict1:
        print(key)
    '''
    def __iter__(self):
        for key in list(vars(self)):
            yield key

    '''
    keys() returns a set containing all the keys
    Iterate Through MyDict Keys:
    for key in myDict1.keys():
        print(key)
    '''
    def keys(self):
        return set(vars(self))

    '''
    values() returns a set containing the value of all the keys
    Iterate Through MyDict Values:
    for key in myDict1.values():
        print(key)
    '''
    def values(self):
        return {self[i] for i in list(vars(self))}

    '''
    items() returns a set of tuples, with each tuple containing a key, value pair
    Iterate Through MyDict Keys and Values:
    for key, value in myDict1.items():
        print(key, value)
    '''
    def items(self):
        return {(i, self[i]) for i in list(vars(self))}

    '''
    Update MyDict:
    Goes throught values and updates or adds key, value pairs
    myDict1.update()
    '''
    def update(self, to_update_dict):
        for key, value in to_update_dict.items():
            self[key] = value

    '''
    Pop Item out of MyDict:
    pops key out of MyDict instance
    myDict1.pop("key")
    You can also use the `del` keyword:
    del myDict1["key"]
    '''
    def pop(self, key):
        del self[key]

    '''
    Clearing MyDict:
    Removes all key, value pairs from dictionary
    myDict1.clear()
    '''
    def clear(self):
        for key in self.keys():
            del self[key]

    '''
    Copying MyDict:
    Returns a copy of MyDict
    myDict1_copy = myDict1.copy()
    '''
    def copy(self):
        newMyDict = MyDict()
        for key, value in self.items():
            newMyDict[key] = value
        return newMyDict


myDict1 = MyDict()
myDict1["test1"] = "hi"
print(myDict1["test1"])
print(f"Keys: {myDict1.keys()}")
print(f"Values: {myDict1.values()}")
print(f"Items: {myDict1.items()}")
myDict1.update({"1": "9", "test2": "new hi"})
print(f"MyDict after update: {myDict1.items()}")
print(f"MyDict Copy: {myDict1.copy().items()}")
myDict1.pop("1")
print(f"MyDict after deleting key 1: {myDict1.items()}")
myDict1.clear()
print(f"MyDict Cleared: {myDict1.items()}")
