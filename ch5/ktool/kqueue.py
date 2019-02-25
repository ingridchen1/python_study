class kqueue():

    def __init__(self):
        self.queue = []

    def push(self, data):
        return self.queue.append(data)

    def pop(self):
        del self.queue[0]

    def size(self):
        return len(self.queue)

    def front(self):
        return self.queue[0]

    def back(self):
        return self.queue[-1]

