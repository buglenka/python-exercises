#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Return Kth to last

Implement an algorithm to find the kth to last element of a singly linked list.

Solution 1: Deque with max len.
Solution 2: Two pointers with distance = k (Sliding window).
"""

from collections import deque

class ListNode(object):
    def __init__(self, value):
        self.value = value
        self.next = None 

def print_list(head):
    values = []
    while(head):
        values.append(str(head.value))
        head = head.next

    print("->".join(values))

def init_list(values):
    head = None
    node = None

    head = node = ListNode(0)

    for value in values:
        node.next = ListNode(value)
        node = node.next

    head = head.next

    # Print
    print_list(head)

    return head

def tail_by_rnr(head, k):
    if (not head or k < 1): return head

    # Set runner to start position
    start = end = head
    while(end and k > 0):
        k -= 1
        end = end.next
        
    if (k > 0): # List contains elements count < k
        return head

    # Move sliding window to tail
    while(end):
        start = start.next
        end = end.next

    # Print
    print_list(start)

    return start

def tail_by_pq(head, k):
    if (not head or k < 1): return head

    d = deque(maxlen = k)

    # Fill the k size buffer
    items_count = 0
    while(head):
        items_count += 1

        d.append(head) 
        head = head.next

    # Build a list
    head = prev = ListNode(0)

    if (items_count < k):
        k = items_count

    while(k > 0):
        prev.next = d.popleft()
        prev = prev.next
        k -= 1
        
    head = head.next

    print_list(head)

    return head


values = [4, 10, 4, 2, -1, 10, 4, 6, 1]

# Solution 1
head = init_list(values)
head = tail_by_pq(head, 3)

# Solution 2
head = init_list(values)
head = tail_by_rnr(head, 3)

