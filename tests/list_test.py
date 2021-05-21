import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

from list_data_structure import MyList

list1 = MyList([1, 2, 3])
if not str(list1) == "[1, 2, 3]": raise ValueError
list1[1] = 9
if not str(list1) == "[1, 9, 3]": raise ValueError
list1.sort()
if not str(list1) == "[1, 3, 9]": raise ValueError
list1.remove(9)
if not str(list1) == "[1, 3]": raise ValueError
list1.pop(1)
if not str(list1) == "[1]": raise ValueError

nested = MyList([1, 2, MyList([3, 4])])
if not str(nested) == "[1, 2, [3, 4]]": raise ValueError
if not str([99] + nested) == "[99, 1, 2, [3, 4]]": raise ValueError
if not str(nested + [99]) == "[1, 2, [3, 4], 99]": raise ValueError
if not str(nested*9) == "[1, 2, [3, 4], 1, 2, [3, 4], 1, 2, [3, 4], 1, 2, [3, 4], 1, 2, [3, 4], 1, 2, [3, 4], 1, 2, [3, 4], 1, 2, [3, 4], 1, 2, [3, 4]]": raise ValueError
if not str(9*nested) == "[1, 2, [3, 4], 1, 2, [3, 4], 1, 2, [3, 4], 1, 2, [3, 4], 1, 2, [3, 4], 1, 2, [3, 4], 1, 2, [3, 4], 1, 2, [3, 4], 1, 2, [3, 4]]": raise ValueError
nested.extend([9,1,2])
if not str(nested) == "[1, 2, [3, 4], 9, 1, 2]": raise ValueError
if not nested.count(1) == 2: raise ValueError
del nested[0]
if not str(nested) == "[2, [3, 4], 9, 1, 2]": raise ValueError
nested.reverse()
if not str(nested) == "[2, 1, 9, [3, 4], 2]": raise ValueError
nested.clear()
if not str(nested) == "[]": raise ValueError
if not str(MyList()) == "[]": raise ValueError
