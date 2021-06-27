from typing import Any


class Node:
    def __init__(self, data: Any, left=None, right=None):
        self.data: Any = data
        if left is not None:
            left = Node(left)
        if right is not None:
            right = Node(right)
        self.left = left
        self.right = right

    def set_left(self, data: Any):
        self.left = Node(data)

    def set_right(self, data: Any):
        self.right = Node(data)

    def __str__(self, top: bool = True) -> str:
        lines: list = []
        lines.append(str(self.data))
        for child in [self.left, self.right]:
            if child is not None:
                for index, data in enumerate(child.__str__(top=False).split("\n")):
                    data = str(data)
                    space_after_line = "  " * index
                    if len(lines)-1 > index:
                        lines[index+1] += "  " + data
                        if top:
                            lines[index+1] += space_after_line
                    else:
                        lines.append(data)
                        if top:
                            lines[-1] += space_after_line
                    for line_number in range(1, len(lines) - 1):
                        if len(lines[line_number + 1]) > \
                                len(lines[line_number]):
                            lines[line_number] += \
                                " " * (len(lines[line_number + 1]) -
                                       len(lines[line_number]))

        lines[0] = \
            " " * int((len(max(lines, key=len)) - len(str(self.data))) / 2) \
            + lines[0]
        return '\n'.join(lines)

    def hasChildren(self) -> bool:
        return self.left is not None and self.right is not None
