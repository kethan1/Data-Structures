from queue_data_structure import Queue, QueueOverflow

linkedstack1 = Queue()
linkedstack1.Push("hi")
linkedstack1.Push("hi1")
linkedstack1.Push(1)
print(linkedstack1)
if not str(linkedstack1) == "['hi', 'hi1', 1]": raise ValueError
if not linkedstack1.Pop().data == 'hi': raise ValueError
print(linkedstack1)

print("\n")

linkedqueue1 = Queue(5)
linkedqueue1.Push("1")
linkedqueue1.Push("2")
linkedqueue1.Push(1)
linkedqueue1.Push(2)
if linkedqueue1.isFullQueue(): raise ValueError 
linkedqueue1.Push("3")
if not linkedqueue1.isFullQueue(): raise ValueError
try:
    linkedqueue1.Push("5")
except QueueOverflow:
    print("QueueOverflow raised")
else:
    print("Failed, QueueOverflow Not Raised")
    raise ValueError
if not linkedqueue1.Front().data == "1": raise ValueError
print(linkedqueue1)
