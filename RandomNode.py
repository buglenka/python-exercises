#!/usr/local/bin/python3.7

"""Random Node

Given a singly linked list, return a random node's value from the 
linked list. Each node must have the same probability of being chosen.

Follow up:
What if the linked list is extremely large and its length is unknown 
to you? Could you solve this efficiently without using extra space?

Example:

// Init a singly linked list [1,2,3].
ListNode head = new ListNode(1);
head.next = new ListNode(2);
head.next.next = new ListNode(3);
Solution solution = new Solution(head);

// getRandom() should return either 1, 2, or 3 randomly. Each element 
// should have equal probability of returning.
solution.getRandom();
"""
import random

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution1:
    """Known length of LinkedList
    """

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.nodes = []

        while(head):
            self.nodes.append(head)
            head = head.next

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """

        return random.choice(self.nodes).val

class Solution2:
    """Unknown dynamically changed length of LinkedList
    
    Solution based on Reservoir sampling.
    """
    
    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        R = self.head; k = 1
        node = self.head.next
        i = 1

        while(node):
            j = random.randint(1, i+1)
            if j <= k:
                R = node

            node = node.next
            i += 1

        return R.val

# Init a singly linked list [1,2,3].
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
solution1 = Solution1(head)
solution2 = Solution2(head)

# getRandom() should return either 1, 2, or 3 randomly. Each element 
# should have equal probability of returning.
print(solution1.getRandom())
print(solution2.getRandom()) 
