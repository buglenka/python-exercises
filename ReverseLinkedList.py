#!/usr/local/bin/python3.7

"""Reverse linked list
"""

class Node:
    def __init__(self, value):
        self.next = None
        self.value = value

class LinkedList:
    def __init__(self):
        self.head = None

    def reverse(self):
        node = self.head
        prev = None

        while(node):
            next = node.next
            node.next = prev
            prev = node
            node = next

        self.head = prev

    def push(self, value):
        node = Node(value)

        node.next = self.head
        self.head = node

    def __str__(self):
        node = self.head
        lst = []

        while(node):
            lst.append(str(node.value))
            node = node.next
    
        return "->".join(lst)


# Initialize
lst = LinkedList()
for i in range(0,10):
    lst.push(i)

# Print initialized
print(lst)

# Reverse
lst.reverse()

# Print reversed
print(lst)