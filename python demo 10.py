class Node:
    def __init__(self, data):
        self.data = data  # store the node's value
        self.left = None  # left child
        self.right = None  # right child

class BinaryTree:
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
        else:
            if current.right is None:
                current.right = Node(data)
            else:
                self._insert_recursive(current.right, data)

    def in_order_traversal(self, node, result=[]):
        if node:
            self.in_order_traversal(node.left, result)
            result.append(node.data)
            self.in_order_traversal(node.right, result)
        return result

    def pre_order_traversal(self, node, result=[]):
        if node:
            result.append(node.data)
            self.pre_order_traversal(node.left, result)
            self.pre_order_traversal(node.right, result)
        return result

    def post_order_traversal(self, node, result=[]):
        if node:
            self.post_order_traversal(node.left, result)
            self.post_order_traversal(node.right, result)
            result.append(node.data)
        return result

# Example usage and test cases:
tree = BinaryTree()
tree.insert(10)
tree.insert(5)
tree.insert(15)
tree.insert(3)
tree.insert(7)

print("In-order traversal:", tree.in_order_traversal(tree.root))     # Output: [3, 5, 7, 10, 15]
print("Pre-order traversal:", tree.pre_order_traversal(tree.root))   # Output: [10, 5, 3, 7, 15]
print("Post-order traversal:", tree.post_order_traversal(tree.root)) # Output: [3, 7, 5, 15, 10]
