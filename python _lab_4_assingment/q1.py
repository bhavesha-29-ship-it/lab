class Stack:
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        if self.items == []:
            print("Empty")
        else:
            return self.items.pop()

    def peek(self):
        if self.items == []:
            print("Empty")
        else:
            return self.items[-1]

    def size(self):
        return len(self.items)


s = Stack()
s.push(10)
s.push(20)
s.push(30)

print(s.peek())
print(s.pop())
print(s.size())