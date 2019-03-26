#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

"""Remove duplicates from a linked list

Solution 1: Using Hash Table: time and space complexity O(N).
Solution 2: Using 'runner' pointer: time and space complexity O(N^2) and constant.
"""

class ListNode(object):
    def __init__(self, value):
        self.value = value
        self.next = None 

def remove_dups_ht(head):
    node = head
    prev = None

    hashmap = {}
    while(node):
        if (hashmap.get(node.value)):

            # remove this node
            prev.next = node.next
        else:
            prev = node
            hashmap[node.value] = 1

        node = node.next

    # Print
    print_list(head)

    return head

def remove_dups_rnr(head):
    node = head

    while(node):
        runner = node.next

        while(runner):
            if (runner.value == node.value):
                prev.next = runner.next
            else:
                prev = runner

            runner = runner.next
        node = node.next

    print_list(head)

    return head


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

    # Print
    print_list(head)

    return head.next




values = [4, 10, 4, 2, 10, 10, 3, 5, 2, 10]

# Solution 1
head = init_list(values)
remove_dups_ht(head)

# Solution 2
head = init_list(values)
remove_dups_rnr(head)



