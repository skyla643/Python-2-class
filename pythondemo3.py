class Queue:
    def __init__(self):
        self.items = []  # initialize an empty list to store queue items

    def enqueue(self, item):
        self.items.append(item)  # add item to the end of the list

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")  # raise an error if queue is empty
        return self.items.pop(0)  # remove and return the item at the front of the queue

    def is_empty(self):
        return len(self.items) == 0  # returns True if the queue is empty

    def size(self):
        return len(self.items)  # returns the number of items in the queue


# Example test cases:
queue = Queue()
print("Is the queue empty?", queue.is_empty())  # Output: True

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print("Queue size:", queue.size())  # Output: 3

print("Dequeued item:", queue.dequeue())  # Output: 1
print("Queue size after dequeue:", queue.size())  # Output: 2
print("Is the queue empty?", queue.is_empty())  # Output: False
