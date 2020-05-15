class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = []
        self.position = 0

    def append(self, item):
        if len(self.buffer) >= self.capacity:
            if self.position >= self.capacity:
                self.position = 0
            self.buffer[self.position] = item
            self.position += 1
        else:
            self.buffer.append(item)
            self.position += 1

    def get(self):
        return self.buffer