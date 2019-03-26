#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

"""Copy List With Random Pointer

A linked list is given such that each node contains an additional 
random pointer which could point to any node in the list or null.

Return a deep copy of the list.

"""


# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        
        new_head = None
        prev_new_node = None
        
        node = head
        hashmap = {}

        # 1. Copy all nodes and fill the hash table
        while(node != None):
            new_node = RandomListNode(node.label)
            new_node.next = node.next
            new_node.random = node.random
            
            if (prev_new_node == None): # first node in a new list
                new_head = new_node
            else: 
                prev_new_node.next = new_node
                
            # Map old node -> new node (copied)
            hashmap[id(node)] = new_node
            
            node = node.next
            prev_new_node = new_node
            
        node = new_head
        # 2. Fill the random pointers
        while(node != None):
            if (node.random != None):
                node.random = hashmap[id(node.random)]
            
            node = node.next
            
        return new_head
