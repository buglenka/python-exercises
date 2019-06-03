#!/usr/local/bin/python3.7

class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.left = None
        self.right = None

class InOrder:
    def traversal(self, node: Node) -> None:
        if node == None: return

        self.traversal(node.left)
        print(node.value)
        self.traversal(node.right)

class PreOrder:
    def traversal(self, node: Node) -> None:
        if node == None: return

        print(node.value)
        self.traversal(node.right)
        self.traversal(node.left)

class PostOrder:
    def traversal(self, node: Node) -> None:
        def do(node: Node) -> None:
            if node == None: return

            do(node.right)
            do(node.left)
            print(node.value)

            node.right = self.prev
            node.left = None
            self.prev = node
 
        self.prev = None

        do(node)

#    1
#  2   5
# 3 4 6 7

root = Node(1)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.left = Node(6)
root.right.right = Node(7)

# In-order traversal
print('In-order Traversal:')
InOrder().traversal(root)

# Pre-order traversal
print('Pre-order Traversal:')
PreOrder().traversal(root)

# Post-order traversal
print('Post-order Traversal:')
PostOrder().traversal(root)

