class Node:
    def __init__(self, data):
        self.data = data  # store the node's value
        self.left = None  # left child
        self.right = None  # right child

class BinarySearchTree:
    def __init__(self):
        self.root = None  # initialize an empty tree

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, current, data):
        if data < current.data:
            if current.left is None:
                current.left = Node(data)
            else:
                self._insert_recursive(current.left, data)
        elif data > current.data:
            if current.right is None:
                current.right = Node(data)
            else:
                self._insert_recursive(current.right, data)
        # If data is equal, it’s not inserted since BST doesn’t allow duplicates

    def search(self, data):
        return self._search_recursive(self.root, data)

    def _search_recursive(self, current, data):
        if current is None:
            return False  # base case: data not found
        if data == current.data:
            return True  # data found
        elif data < current.data:
            return self._search_recursive(current.left, data)
        else:
            return self._search_recursive(current.right, data)

# Example usage and test cases:
bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(3)
bst.insert(7)

print("Searching for 7:", bst.search(7))  # Output: True
print("Searching for 20:", bst.search(20))  # Output: False
