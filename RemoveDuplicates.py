#!/usr/local/bin/python3.7

"""Remove Duplicates from Sorted Array

Given a sorted array nums, remove the duplicates in-place such 
that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this 
by modifying the input array in-place with O(1) extra memory.

Example 1:
Given nums = [1,1,2],
Your function should return length = 2, with the first two 
elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the returned length.
"""

from typing import List

def removeDuplicates(nums: List[int]) -> int:
    if not nums:
        return 0

    tail = 0

    for i in range(1, len(nums)):
        if nums[i] != nums[tail]:
            tail += 1
            nums[tail] = nums[i]

    return tail + 1
     

examples = [
    {
        "input" : [1, 1, 2, 3],
        "output": [1, 2, 3],
        "return": 3,
    },
    {
        "input" : [1, 1, 2, 2, 2, 3, 4],
        "output": [1, 2, 3, 4],
        "return": 4,
    },
    {
        "input" : [1, 2, 3, 4],
        "output": [1, 2, 3, 4],
        "return": 4,
    },
    {
        "input" : [0, 0, 1, 1, 1, 2, 2, 3, 3, 4],
        "output": [0, 1, 2, 3, 4],
        "return": 5,
    },
]

for e in examples:
    print('---\nInput: {}, Output: {}'.format(e['input'], e['output']))

    length = removeDuplicates(e['input'])

    print('Actual Output: {}, Lenght: {}'.format(e['input'], length))