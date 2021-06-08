from typing import Union, Any


class Node:
    def __init__(self, data: Any):
        self.data: Any = data
        self.children: list = []

    def insert(self, data: Any):
        self.children.append(Node(data))

    def __str__(self, top: bool = True) -> str:
        output_str = str(self.data)
        if self.children:
            output_str += "\n"
            first = True
            for index, child in enumerate(self.children):
                child_str = child.__str__(False)
                if "\n" in child_str:
                    if top:
                        child_str = '\n│   '.join(child_str.split("\n"))
                    else:
                        child_str = '\n    '.join(child_str.split("\n"))
                if not first:
                    output_str += f"\n└── {child_str}" \
                        if index == len(self.children) - 1 \
                        else f"\n├── {child_str}"
                else:
                    output_str += f"└── {child_str}" \
                        if index == len(self.children) - 1 \
                        else f"├── {child_str}"
                    first = False

        return output_str

    def hasChildren(self) -> bool:
        return bool(self.children)

    def __getitem__(self, pos: Union[int, slice]):
        return self.children[pos]
