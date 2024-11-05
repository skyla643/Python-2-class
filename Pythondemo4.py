from collections import deque

class DequeQueue:
    def __init__(self):
        self.items = deque()  # initialize an empty deque

    def enqueue(self, item):
        self.items.append(item)  # add item to the end of the deque

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")  # raise error if queue is empty
        return self.items.popleft()  # remove and return the item from the front of the deque

    def is_empty(self):
        return len(self.items) == 0  # returns True if deque is empty

    def size(self):
        return len(self.items)  # returns the number of items in the deque


# Example test cases:
queue = DequeQueue()
print("Is the queue empty?", queue.is_empty())  # Output: True

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
print("Queue size:", queue.size())  # Output: 3

print("Dequeued item:", queue.dequeue())  # Output: 10
print("Queue size after dequeue:", queue.size())  # Output: 2
print("Is the queue empty?", queue.is_empty())  # Output: False
