class Node:
    def __init__(self,data):
        self.data = data
        self.children = []
    
    def insert(self, data):
        self.children.append(Node(data))


    def __str__(self, top=True):
        lines = []
        lines.append(str(self.data))
        for child in self.children:
            children_str = child.__str__(top=False).split("\n")
            # if top:
            #     print(children_str)
            for index, data in enumerate(children_str):
                space_after_line = "   "
                space_after_line = space_after_line * index
                try:
                    if top:
                        lines[index+1] += "   " + str(data) + "   "
                    else:
                        lines[index+1] += "    " + str(data)
                except:
                    if top:
                        lines.append(str(data) + space_after_line)
                    else:
                        lines.append(str(data))
                for line_number in range(1, len(lines)-1):
                    if len(lines[line_number+1]) > len(lines[line_number]):
                        lines[line_number] += " " * ((len(lines[line_number+1])-len(lines[line_number])))

        lines[0] = " " * int((len(max(lines, key=len)) - len(self.data))/2) + lines[0]
        return '\n'.join(lines)

    def hasChildren(self):
        return bool(self.children)

    def __getitem__(self, pos: int):
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
root[0][0][0].insert("v1.1")
root[0][0][0].insert("v2.1")
print(root)
