class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    def enqueue(self, item):
        if self.is_full():
            print("Queue is full")
        else:
            if self.front == -1:
                self.front = 0
            self.rear = (self.rear + 1) % self.capacity
            self.queue[self.rear] = item

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            if self.front == self.rear:
                self.front = self.rear = -1
            else:
                self.front = (self.front + 1) % self.capacity
            return self.queue[self.front]

    def peek(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            return self.queue[self.front]

    def display(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            for i in range(self.front, (self.rear + 1) % self.capacity):
                print(self.queue[i], end=" ")
            print()