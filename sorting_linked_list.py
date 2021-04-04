from linked_list_data_structure import LinkedList

# Sorting!

import time
import random

linkedlist2 = LinkedList()
linkedlist2.load_from_list([
    3, 98319, 32786, 65561, 32797, 29, 98336, 38, 46, 57, 32826, 98375, 98377, 98378, 65618, 98396, 
    5633, 65638, 98407, 98419, 65657, 121, 98427, 65673, 98441, 98443, 98445, 98451, 65692, 32929, 
    32930, 32935, 98474, 98482, 65715, 32948, 190, 98497, 65737, 205, 207, 32979, 219, 98525, 65757,
    222, 32989, 32992, 98530, 248, 33018, 33020, 98558, 98559, 65793, 259, 260, 261, 65798, 65800, 
    65801, 265, 33041, 65810, 65811, 65815, 280, 33049, 283, 65820, 289, 33063, 65835, 65841, 98616, 
    98621, 65866, 65874, 98645, 345, 98650, 349, 98654, 65887, 33129, 98667, 33138, 383, 65923, 
    65931, 98701, 65933, 98705, 65942, 33174, 65945, 33180, 65957, 422, 98728, 33193, 427, 65963, 
    65965, 98739, 65974, 33214, 98762, 98764, 98772, 98774, 66007, 479, 66015, 33249, 482, 66018, 
])

def insertion_sort(numbers):
    newlist = numbers.copy()
    for loop_index1 in range(0, newlist.GetLength()-1):
        for loop_index2 in range(loop_index1, newlist.GetLength()-1):
            if newlist.GetAtPos(loop_index1).data > newlist.GetAtPos(loop_index2).data:
                a = newlist.GetAtPos(loop_index2)
                newlist.deleteAtPos(loop_index2)
                newlist.insertAtPos(loop_index1, a)
    return newlist

def swapper(numbers, a, b):
    tmp_numbers = numbers.copy()
    pos1_data = tmp_numbers.GetAtPos(a).data
    pos2_data = tmp_numbers.GetAtPos(b).data
    tmp_numbers.UpdateAtPos(a, pos2_data)
    tmp_numbers.UpdateAtPos(b, pos1_data)
    return tmp_numbers

def issorted(numbers):
    for thing in range(numbers.GetLength()-1):
        if numbers.GetAtPos(thing).data > numbers.GetAtPos(thing+1).data:
            return False
    return True

def bubble_sort(lst):
    copy_of_lst = lst.copy()
    while not issorted(copy_of_lst):
        for thing in range(0, copy_of_lst.GetLength()-1):
            if copy_of_lst.GetAtPos(thing).data > copy_of_lst.GetAtPos(thing+1).data:
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

print("!!Starting Sorting!!")

print("!Insertion Sort!")

x = time.time()
print(list(insertion_sort(linkedlist2).DisplayAllNodes()))
y = time.time()
print(y-x)

print("\n", "!Bubble Sort!", "\n", sep="")

x = time.time()
print(list(bubble_sort(linkedlist2).DisplayAllNodes()))
y = time.time()
print(y-x)

print("\n", "!Selection Sort!", "\n", sep="")

x = time.time()
print(list(selection_sort(linkedlist2).DisplayAllNodes()))
y = time.time()
print(y-x)