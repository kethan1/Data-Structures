'''
---------------------------------------------
MyDict - My version of the class Dictionary
Author: Kethan Vegunta
---------------------------------------------
Description:
My version of the python dictionary. It's syntax is very similar to a regular
python dict.
'''
import pickle


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
        return getattr(self, self.__convert_item_to_str(key))

    '''
    Set Item:
    myDict1["hi"] = 1
    '''
    def __setitem__(self, key, value):
        setattr(self, self.__convert_item_to_str(key), value)

    '''
    Delete Item:
    del myDict1["hi"]
    or
    myDict1.pop("hi")
    '''
    def __delitem__(self, key):
        delattr(self, self.__convert_item_to_str(key))

    '''
    Iterate Through MyDict:
    for key in myDict1:
        print(key)
    '''
    def __iter__(self):
        for key in list(vars(self)):
            yield self.__convert_str_to_item(key)

    '''
    keys() returns a set containing all the keys
    Iterate Through MyDict Keys:
    for key in myDict1.keys():
        print(key)
    '''
    def keys(self):
        return {self.__convert_str_to_item(key) for key in vars(self)}

    '''
    values() returns a set containing the value of all the keys
    Iterate Through MyDict Values:
    for key in myDict1.values():
        print(key)
    '''
    def values(self):
        return {
            self[self.__convert_str_to_item(key)] for key in list(vars(self))
        }

    '''
    items() returns a set of tuples, with each tuple containing a key,
    value pair.
    Iterate Through MyDict Keys and Values:
    for key, value in myDict1.items():
        print(key, value)
    '''
    def items(self):
        return {
            (
                self.__convert_str_to_item(key),
                self[self.__convert_str_to_item(key)]
            )
            for key in list(vars(self))
        }

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

    def __convert_item_to_str(self, item):
        return pickle.dumps(item).decode('unicode_escape')

    def __convert_str_to_item(self, item):
        return pickle.loads(
            item.encode('utf-8', 'unicode_escape').replace(b'\xc2', b'')
        )
