#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Sort list"

Sort a linked list in O(n log n) time using constant space complexity.

Example 1:
Input: 4->2->1->3
Output: 1->2->3->4

Example 2:
Input: -1->5->3->4->0
Output: -1->0->3->4->5
"""

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

def sort(head):
    if (not head): return None

    # One element in a list
    if (not head.next): return head

    # Two elements in a list, make right order
    if (not head.next.next):
        if (head.value > head.next.value):
            buff = head
            head = head.next
            head.next = buff
            head.next.next = None
        return head
    
    # Do not sort, just split
    slow = fast = prev = head

    while(slow):
        if not fast or not fast.next: # the end of list
            middle = slow
            prev.next = None

            right = sort(middle)
            left = sort(head)

            break
        else:
            prev = slow
            slow = slow.next
            fast = fast.next.next

    # Merge lists
    head = _merge_2_lists(left, right)

    return head


values = [4, 10, 4, 2, -1, 10, 4, 6, 1]

head = init_list(values)
head = sort(head)

print_list(head)
