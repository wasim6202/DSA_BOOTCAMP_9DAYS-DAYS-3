class Deque:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def add_front(self, item):
        self.items.insert(0, item)

    def add_rear(self, item):
        self.items.append(item)

    def remove_front(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Deque is empty")

    def remove_rear(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Deque is empty")

    def peek_front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Deque is empty")

    def peek_rear(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Deque is empty")

    def size(self):
        return len(self.items)

    def display(self):
        print("Deque:", self.items)

# Test the Deque
if __name__ == "__main__":
    deque = Deque()

    # Add elements to front and rear
    deque.add_front(1)
    deque.add_rear(2)
    deque.add_front(3)
    deque.add_rear(4)

    deque.display()  # Deque: [3, 1, 2, 4]

    # Remove from front and rear
    print("Removed from front:", deque.remove_front())
    print("Removed from rear:", deque.remove_rear())

    deque.display()  # Deque: [1, 2]

    # Peek at front and rear
    print("Front element:", deque.peek_front())
    print("Rear element:", deque.peek_rear())

    # Check size
    print("Size of deque:", deque.size())

    # Remove remaining elements
    print("Removed from front:", deque.remove_front())
    print("Removed from rear:", deque.remove_rear())

    # Check if empty
    print("Is deque empty?", deque.is_empty())

    # Try to remove from empty deque
    try:
        deque.remove_front()
    except IndexError as e:
        print("Error:", str(e))