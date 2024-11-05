class Node:
    def __init__(self, data):
        self.data = data  # store the data in the node
        self.next = None  # initially, this node does not point to any other node


class SinglyLinkedList:
    def __init__(self):
        self.head = None  # the list starts empty, so head is None

    def append(self, data):
        new_node = Node(data)  # create a new node
        if not self.head:
            # if the list is empty, set new_node as the head
            self.head = new_node
        else:
            # otherwise, find the end of the list and add the new node
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def prepend(self, data):
        new_node = Node(data)  # create a new node
        new_node.next = self.head  # make new_node point to the current head
        self.head = new_node  # update the head to be the new node

    def print_list(self):
        current = self.head  # start from the head of the list
        while current:
            print(current.data, end=" -> ")  # print the data
            current = current.next  # move to the next node
        print("None")  # end of the list


# Example usage:
linked_list = SinglyLinkedList()
linked_list.append(10)
linked_list.append(20)
linked_list.prepend(5)
linked_list.print_list()  # Output: 5 -> 10 -> 20 -> None
