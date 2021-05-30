from typing import Union, Any

class Node:
    def __init__(self, data: Any):
        self.data: Any = data
        self.children: list = []
    
    def insert(self, data: Any):
        self.children.append(Node(data))

    def __str__(self, top: bool=True) -> str:
        lines: list = []
        lines.append(str(self.data))
        for child in self.children:
            for index, data in enumerate(child.__str__(top=False).split("\n")):
                data = str(data)
                space_after_line = "  " * index
                if len(lines)-1 > index:
                    lines[index+1] += "  " + data
                    if top:
                        lines[index+1] += space_after_line
                else:
                    if top:
                        lines.append(data + space_after_line)
                    else:
                        lines.append(data)
                for line_number in range(1, len(lines) - 1):
                    if len(lines[line_number + 1]) > len(lines[line_number]):
                        lines[line_number] += " " * (len(lines[line_number + 1]) - len(lines[line_number]))

        lines[0] = " " * int((len(max(lines, key=len)) - len(str(self.data))) / 2) + lines[0]
        return '\n'.join(lines)

    def hasChildren(self) -> bool:
        return bool(self.children)

    def __getitem__(self, pos: Union[int, slice]):
        return self.children[pos]
    
root = Node("Languages Good For")
root.insert("Serverside Web Development")
root.insert("Clientside Web Development")
root.insert("For Speed")
root.insert("Game Development")
root[0].insert("Python")
root[0].insert("NodeJS")
root[0].insert("Ruby")
root[0].insert("PHP")
root[1].insert("CSS + HTML + Javascript")
root[1].insert("Typescript")
root[1].insert("SASS")
root[2].insert("C")
root[2].insert("C++")
root[2].insert("Java")
root[2].insert("C#")
root[3].insert("C#")
root[3].insert("C++")
root[0][0].insert("Flask")
root[0][0].insert("Django")
root[0][1].insert("Express")
root[0][2].insert("Ruby on Rails")
root[0][0][0].insert(1.1)
root[0][0][0].insert(2.0)
root[0][0][0][1].insert("2.0.1")
root[0][0][0][1].insert("2.0.0")
print(root)
