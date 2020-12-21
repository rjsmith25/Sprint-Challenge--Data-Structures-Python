class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = []
        self.track_queue = 0
    def append(self, item):
        if len(self.queue) == self.capacity:
            self.queue.pop(self.track_queue % self.capacity)
            self.queue.insert(self.track_queue % self.capacity, item)
            self.track_queue += 1
        else:
            self.queue.append(item)

    def get(self):
        return self.queue
