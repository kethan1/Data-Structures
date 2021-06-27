import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parents[1].absolute()))

from binary_tree import Node

root = Node(30)
root.set_left(11)
root.set_right(39)
root.left.set_left(5)
root.left.set_right(16)
root.right.set_left(38)
root.right.set_right(320)


def binary_tree_recursive_search(rootNode, numberToFind, pattern=None):
    if pattern is None:
        pattern = []
    if rootNode is not None:
        if numberToFind < rootNode.data:
            pattern.append("left")
            return binary_tree_recursive_search(rootNode.left, numberToFind,
                                                pattern=pattern)
        elif numberToFind > rootNode.data:
            pattern.append("right")
            return binary_tree_recursive_search(rootNode.right, numberToFind,
                                                pattern=pattern)
        else:
            pattern.append("found")
            return pattern
    else:
        pattern.append("not found")
        return pattern


def binary_tree_iterative_search(rootNode, numberToFind):
    pattern = []
    end = False
    while not end:
        if rootNode is not None:
            if numberToFind < rootNode.data:
                pattern.append("left")
                rootNode = rootNode.left
                continue
            elif numberToFind > rootNode.data:
                pattern.append("right")
                rootNode = rootNode.right
                continue
            else:
                pattern.append("found")
                return pattern
        else:
            pattern.append("not found")
            end = True
    return pattern


print(binary_tree_recursive_search(root, 38))
assert binary_tree_recursive_search(root, 38) == ['right', 'left', 'found']
print(binary_tree_iterative_search(root, 38))
assert binary_tree_iterative_search(root, 38) == ['right', 'left', 'found']
print(binary_tree_recursive_search(root, 320))
assert binary_tree_recursive_search(root, 320) == ['right', 'right', 'found']
print(binary_tree_iterative_search(root, 320))
assert binary_tree_iterative_search(root, 320) == ['right', 'right', 'found']
print(binary_tree_recursive_search(root, 300))
assert binary_tree_recursive_search(root, 300) == ['right', 'right', 'left', 'not found']
print(binary_tree_iterative_search(root, 300))
assert binary_tree_iterative_search(root, 300) == ['right', 'right', 'left', 'not found']
