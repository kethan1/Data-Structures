import os
import sys
import inspect

sys.path.insert(0, os.path.dirname(os.path.dirname(
    os.path.abspath(inspect.getfile(inspect.currentframe())))))

from list_data_structure import MyList

list1 = MyList([1, 2, 3])
assert list1 == [1, 2, 3]
list1[1] = 9
assert list1 == [1, 9, 3]
list1.sort()
assert list1 == [1, 3, 9]
list1.remove(9)
assert list1 == [1, 3]
list1.pop(1)
assert list1 == [1]

nested = MyList([1, 2, MyList([3, 4])])
assert nested == [1, 2, [3, 4]]
assert [99] + nested == [99, 1, 2, [3, 4]]
assert nested + [99] == [1, 2, [3, 4], 99]
assert nested*9 == [1, 2, [3, 4], 1, 2, [3, 4], 1, 2, [3, 4], 1, 2, [3, 4], 1, 2, [3, 4], 1, 2, [3, 4], 1, 2, [3, 4], 1, 2, [3, 4], 1, 2, [3, 4]]
assert 9 * nested == [1, 2, [3, 4], 1, 2, [3, 4], 1, 2, [3, 4], 1, 2, [3, 4], 1, 2, [3, 4], 1, 2, [3, 4], 1, 2, [3, 4], 1, 2, [3, 4], 1, 2, [3, 4]]
nested.extend([9, 1, 2])
assert nested == [1, 2, [3, 4], 9, 1, 2]
assert nested.count(1) == 2
del nested[0]
assert nested == [2, [3, 4], 9, 1, 2]
nested.reverse()
assert nested == [2, 1, 9, [3, 4], 2]
nested.clear()
assert nested == []
assert MyList() == []
