import os
import sys
import inspect
import json
import timeit

sys.path.insert(0, os.path.dirname(os.path.dirname(
    os.path.abspath(inspect.getfile(inspect.currentframe())))))

from linked_list_data_structure import LinkedList


# Sorting!

if not os.path.exists("LogFiles/"):
    os.makedirs("LogFiles/")

linkedlist2 = LinkedList()
linkedlist2.load_from_iterable([
    3, 98319, 32786, 65561, 32797, 29, 98336, 38, 46, 57, 32826, 98375, 98377,
    98378, 65618, 98396, 5633, 65638, 98407, 98419, 65657, 121, 98427, 65673,
    98441, 98443, 98445, 98451, 65692, 32929, 32930, 32935, 98474, 98482,
    65715, 32948, 190, 98497, 65737, 205, 207, 32979, 219, 98525, 65757, 222,
    32989, 32992, 98530, 248, 33018, 33020, 98558, 98559, 65793, 259, 260, 261,
    65798, 65800, 65801, 265, 33041, 65810, 65811, 65815, 280, 33049, 283,
    65820, 289, 33063, 65835, 65841, 98616, 98621, 65866, 65874, 98645, 345,
    98650, 349, 98654, 65887, 33129, 98667, 33138, 383, 65923, 65931, 98701,
    65933, 98705, 65942, 33174, 65945, 33180, 65957, 422, 98728, 33193, 427,
    65963, 65965, 98739, 65974, 33214, 98762, 98764, 98772, 98774, 66007, 479,
    66015, 33249, 482, 66018
])


def insertion_sort(numbers):
    newlist = numbers.copy()
    for loop_index1 in range(0, newlist.GetLength()):
        for loop_index2 in range(loop_index1, newlist.GetLength()):
            if newlist[loop_index1].data > newlist[loop_index2].data:
                a = newlist.getAtPos(loop_index2)
                newlist.deleteAtPos(loop_index2)
                newlist.insertAtPos(loop_index1, a)
    return newlist


def swapper(numbers, a, b):
    tmp_numbers = numbers.copy()
    pos1_data = tmp_numbers[a].data
    pos2_data = tmp_numbers[b].data
    tmp_numbers.updateAtPos(a, pos2_data)
    tmp_numbers.updateAtPos(b, pos1_data)
    return tmp_numbers


def issorted(numbers):
    for thing in range(numbers.GetLength()-1):
        if numbers[thing].data > numbers[thing+1].data:
            return False
    return True


def bubble_sort(lst):
    copy_of_lst = lst.copy()
    while not issorted(copy_of_lst):
        for thing in range(0, copy_of_lst.GetLength()-1):
            if copy_of_lst[thing].data > copy_of_lst[thing+1].data:
                copy_of_lst = swapper(copy_of_lst, thing, thing+1)
    return copy_of_lst


def selection_sort(lst):
    copy_of_lst = lst.copy()
    for thing in range(0, len(lst)-1):
        a = copy_of_lst[thing:]
        mn = min(a)
        index_of_mn = copy_of_lst.index(mn)
        copy_of_lst.deleteAtPos(index_of_mn)
        copy_of_lst.insertAtPos(thing, mn)
    return copy_of_lst


print(list(linkedlist2.DisplayAllNodes()))

print("\n!!Starting Sorting!!\n")

print("!Insertion Sort!")

with open("LogFiles/Insertion_Sort.log", "w") as insertion_sort_log:
    print(list(linkedlist2.DisplayAllNodes()), file=insertion_sort_log)
    print("\n", file=insertion_sort_log)
    start = timeit.default_timer()
    output = list(insertion_sort(linkedlist2).DisplayAllNodes())
    end = timeit.default_timer()
    print(output, file=insertion_sort_log)
    print("\n", file=insertion_sort_log)
    print(end-start, file=insertion_sort_log)

print("\n!Bubble Sort!")

with open("LogFiles/Bubble_Sort.log", "w") as bubble_sort_log:
    print(list(linkedlist2.DisplayAllNodes()), file=bubble_sort_log)
    print("\n", file=bubble_sort_log)
    start = timeit.default_timer()
    output = list(bubble_sort(linkedlist2).DisplayAllNodes())
    end = timeit.default_timer()
    print(output, file=bubble_sort_log)
    print("\n", file=bubble_sort_log)
    print(end-start, file=bubble_sort_log)

print("\n!Selection Sort!")

with open("LogFiles/Selection_Sort.log", "w") as selection_sort_log:
    print(list(linkedlist2.DisplayAllNodes()), file=selection_sort_log)
    print("\n", file=selection_sort_log)
    start = timeit.default_timer()
    output = list(selection_sort(linkedlist2).DisplayAllNodes())
    end = timeit.default_timer()
    print(output, file=selection_sort_log)
    print("\n", file=selection_sort_log)
    print(end-start, file=selection_sort_log)


sorted_list = [
    3, 29, 38, 46, 57, 121, 190, 205, 207, 219, 222, 248, 259, 260, 261,
    265, 280, 283, 289, 345, 349, 383, 422, 427, 479, 482, 5633, 32786,
    32797, 32826, 32929, 32930, 32935, 32948, 32979, 32989, 32992, 33018,
    33020, 33041, 33049, 33063, 33129, 33138, 33174, 33180, 33193, 33214,
    33249, 65561, 65618, 65638, 65657, 65673, 65692, 65715, 65737, 65757,
    65793, 65798, 65800, 65801, 65810, 65811, 65815, 65820, 65835, 65841,
    65866, 65874, 65887, 65923, 65931, 65933, 65942, 65945, 65957, 65963,
    65965, 65974, 66007, 66015, 66018, 98319, 98336, 98375, 98377, 98378,
    98396, 98407, 98419, 98427, 98441, 98443, 98445, 98451, 98474, 98482,
    98497, 98525, 98530, 98558, 98559, 98616, 98621, 98645, 98650, 98654,
    98667, 98701, 98705, 98728, 98739, 98762, 98764, 98772, 98774
]

with open("LogFiles/Insertion_Sort.log", "r") as insertion_sort_log:
    for _ in range(3):
        insertion_sort_log.readline()
    if json.loads(insertion_sort_log.readline()) != sorted_list:
        print("Insertion Sort Failed")
        raise AssertionError("Insertion Sort Failed")

with open("LogFiles/Bubble_Sort.log", "r") as bubble_sort_log:
    for _ in range(3):
        bubble_sort_log.readline()
    if json.loads(bubble_sort_log.readline()) != sorted_list:
        print("Bubble Sort Failed")
        raise AssertionError("Bubble Sort Failed")

with open("LogFiles/Selection_Sort.log", "r") as selection_sort_log:
    for _ in range(3):
        selection_sort_log.readline()
    if json.loads(selection_sort_log.readline()) != sorted_list:
        print("Selection Sort Failed")
        raise AssertionError("Selection Sort Failed")
