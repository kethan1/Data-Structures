class StackOverflow(BaseException):
    pass

class Stack:
    def __init__(self, limit):
        self.stck = []
        self.limit = limit

    def Push(self, data):
        if isinstance(self.limit, int):
            if self.limit < len(self.stck)+1:
                raise StackOverflow
            self.stck.append(data)
        else:
            self.stck.append(data)

    def Pop(self):
        last_element = self.stck[-1]
        self.stck = self.stck[:-1]
        return last_element

    def Top(self):
        return self.stck[-1]

    def Size(self):
        return len(self.stck)

    def isEmptyStack(self):
        return not(bool(self.stck))

    def isFullStack(self):
        if isinstance(self.limit, int):
            if self.limit == len(self.stck)+1:
                return True
        return False

    def __len__(self):
        return self.Size()
