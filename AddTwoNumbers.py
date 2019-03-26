#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

"""Add two numbers

You are given two non-empty linked lists representing two non-negative 
integers. The digits are stored in reverse order and each of their nodes 
contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except 
the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        sumList = ListNode()

        carry = 0

        while(True):

            if ()

            lvalue = l1.value
            rvalue = l2.value

            l1.value = l1.next
            l2.value = l2.next

            sumDigit = lvalue + rvalue + carry

            if (sumDigit > 9):
                carry = 1
            else:
                carry = 0

            sumList.value = sumDigit
        
