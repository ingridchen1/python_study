class kstack():

    def __init__(self):
        self.stack = []

    def push(self, data):
        return self.stack.append(data)

    def pop(self):
        del self.stack[-1]

    def size(self):
        return len(self.stack)

    def top(self):
        return self.stack[-1]

