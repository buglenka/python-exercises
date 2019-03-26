#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

"""Merge K sorted lists

Solution 1: merge each 2 linked lists. 
Solution 2: Using a priority queue. 
"""

from collections import deque
from Queue import PriorityQueue

class ListNode(object):
    def __init__(self, value):
        self.value = value
        self.next = None

def _merge_2_lists(list_1, list_2):       
    head = prev = ListNode(0)

    while list_1 and list_2:
        if (list_1.value < list_2.value):
            prev.next = list_1                
                
            prev = list_1
            list_1 = list_1.next
        else:
            prev.next = list_2
                
            prev = list_2
            list_2 = list_2.next
            
    if not list_1:
        prev.next = list_2

    if not list_2:
        prev.next = list_1                
            
    return head.next
    
def merge_k_lists_by_2(lists):
    """
    :type lists: List[ListNode]
    :rtype: ListNode
    """
    lists_count = len(lists)
        
    if (lists_count < 1): return None
    if (lists_count < 2): return lists.pop()
        
    queue = deque(lists)

    while (lists_count > 1):
        queue.append(_merge_2_lists(queue.popleft(), queue.popleft()))
            
        lists_count = len(queue)

    head = queue.popleft()

    # Print
    print_list(head)
        
    return head

def merge_k_lists_by_pq(lists):
    head = prev = ListNode(0)
    q = PriorityQueue()    

    # Put all values to queue
    for l in lists:
        node = l

        while(node):
            q.put(node.value)

            node = node.next

    # Build a final list
    while not q.empty():
        prev.next = ListNode(q.get())
        prev = prev.next

    head = head.next

    # Print
    print_list(head)
    
    return head
        
def print_list(head):
    values = []
    while(head is not None):
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



values = [[1, 3, 4, 6, 7, 8, 8], [2, 5, 9, 9, 56], [2, 2, 6, 7]]

lists = []
for block in values:
    lists.append(init_list(block))

# Solution 1
merge_k_lists_by_2(lists)


lists = []
for block in values:
    lists.append(init_list(block))

# Solution 2
merge_k_lists_by_pq(lists)
