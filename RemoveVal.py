#!/usr/local/bin/python3.7

"""Remove val from Linked List

Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def removeElements(head: ListNode, val: int) -> ListNode:
    while(head):
        if (head.val != val):
            break
            
        head = head.next
            
    newHead = head
    
    while(head):
        if (head.next == None):
            break
            
        if (head.next.val == val):
            head.next = head.next.next
        else:
            head = head.next
        
    return newHead

[1,2,2,1]
2

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(2)
head.next.next.next = ListNode(1)

val = 2

removeElements(head, val)
            
            
        