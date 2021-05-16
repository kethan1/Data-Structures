import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from queue_data_structure import Queue

import timeit
import sys

books = Queue()
books.load_from_iterable(['Cooking1', 'Computer1', 'Literature1', 'Literature2', 'Cooking2176', 'Computer207', 'Computer208', 'Literature172', 'Cooking185', 'Computer209', 'Literature175', 'Science195', 'Computer212', 'Literature176', 'Literature177', 'Computer216', 'Cooking193', 'Science200', 'Computer217', 'Science201', 'Literature184', 'Science203', 'Computer218', 'Literature185', 'Computer219', 'Literature189', 'Science212', 'Science213', 'Literature190', 'Computer227', 'Computer228', 'Computer229', 'Computer230', 'Science214', 'Literature191', 'Science215', 'Cooking204', 'Science216', 'Cooking205', 'Cooking206', 'Computer231', 'Cooking207', 'Science217', 'Computer232', 'Cooking208', 'Literature192', 'Literature193', 'Computer233', 'Cooking209', 'Cooking210', 'Science218', 'Literature194', 'Computer234', 'Literature195', 'Computer235', 'Computer236', 'Computer237', 'Science219', 'Literature196', 'Science220', 'Computer238', 'Cooking211', 'Cooking212', 'Cooking213', 'Literature201', 'Computer245', 'Computer246', 'Science232', 'Literature205', 'Computer247', 'Computer248', 'Cooking218', 'Science233', 'Literature206', 'Science234', 'Cooking219', 'Computer249', 'Science235', 'Science236', 'Cooking220', 'Cooking221', 'Cooking222', 'Computer250', 'Literature207', 'Literature208', 'Computer251', 'Computer252', 'Literature209', 'Science237', 'Literature210', 'Cooking223', 'Computer253', 'Science238', 'Literature211', 'Cooking224', 'Computer254', 'Computer255', 'Cooking225', 'Computer256', 'Cooking226', 'Cooking227', 'Computer257', 'Cooking228', 'Science239', 'Computer258', 'Literature212', 'Cooking229'])

booksSorted = {
    "Science": Queue(),
    "Computers": Queue(),
    "Cooking": Queue(),
    "Literature": Queue()
}

start_time = timeit.default_timer()
while not books.isEmptyQueue():
    book = books.Pop()
    if "Science" in book.data:
        booksSorted["Science"].Push(book)
    elif "Computer" in book.data:
        booksSorted["Computers"].Push(book)
    elif "Cooking" in book.data:
        booksSorted["Cooking"].Push(book)
    elif "Literature" in book.data:
        booksSorted["Literature"].Push(book)
end_time = timeit.default_timer()
time1 = end_time-start_time

failed = False
for key, value in booksSorted.items():
    print(key, list(value.showAll()))
    if key == "Science":
        if set(value.showAll()) != {'Science239', 'Science238', 'Science237', 'Science236', 'Science235', 'Science234', 'Science233', 'Science232', 'Science220', 'Science219', 'Science218', 'Science217', 'Science216', 'Science215', 'Science214', 'Science213', 'Science212', 'Science203', 'Science201', 'Science200', 'Science195'}:
            print("Sorting Science Books Failed")
            failed = True
    elif key == "Computers":
        if set(value.showAll()) != {'Computer258', 'Computer257', 'Computer256', 'Computer255', 'Computer254', 'Computer253', 'Computer252', 'Computer251', 'Computer250', 'Computer249', 'Computer248', 'Computer247', 'Computer246', 'Computer245', 'Computer238', 'Computer237', 'Computer236', 'Computer235', 'Computer234', 'Computer233', 'Computer232', 'Computer231', 'Computer230', 'Computer229', 'Computer228', 'Computer227', 'Computer219', 'Computer218', 'Computer217', 'Computer216', 'Computer212', 'Computer209', 'Computer208', 'Computer207', 'Computer1'}:
            print("Sorting Computer Books Failed")
            failed = True
    elif key == "Cooking":
        if set(value.showAll()) != {'Cooking229', 'Cooking228', 'Cooking227', 'Cooking226', 'Cooking225', 'Cooking224', 'Cooking223', 'Cooking222', 'Cooking221', 'Cooking220', 'Cooking219', 'Cooking218', 'Cooking213', 'Cooking212', 'Cooking211', 'Cooking210', 'Cooking209', 'Cooking208', 'Cooking207', 'Cooking206', 'Cooking205', 'Cooking204', 'Cooking193', 'Cooking185', 'Cooking2176', 'Cooking1'}:
            print("Sorting Cooking Books Failed")
            failed = True
    elif key == "Literature":
        if set(value.showAll()) != {'Literature212', 'Literature211', 'Literature210', 'Literature209', 'Literature208', 'Literature207', 'Literature206', 'Literature205', 'Literature201', 'Literature196', 'Literature195', 'Literature194', 'Literature193', 'Literature192', 'Literature191', 'Literature190', 'Literature189', 'Literature185', 'Literature184', 'Literature177', 'Literature176', 'Literature175', 'Literature172', 'Literature2', 'Literature1'}:
            print("Sorting Literature Books Failed")
            failed = True

print(f"Time to sort Stack: {time1}")
print(f"Failed: {failed}")
if failed:
    sys.exit(1)