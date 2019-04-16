#!/usr/local/bin/python3.7

"""Rotate Array

Given an array, rotate the array to the right by k steps, 
                                    where k is non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
Note:

Try to come up as many solutions as you can, there are at 
least 3 different ways to solve this problem.

Could you do it in-place with O(1) extra space?
"""

from collections import deque
from typing import Deque, List


examples = [
    {'input': [1,2,3,4,5,6,7], 'k': 3, 'output': [5,6,7,1,2,3,4]},
    {'input': [-1,-100,3,99], 'k': 2, 'output': [3,99,-1,-100]},
]

for e in examples:
    print('Input: [{}], Output: [{}]'
            .format(', '.join(map(str, e['input'])), 
                    ', '.join(map(str, e['output']))))

    # Solution 1: Deque or FIFO Queue
    d = deque()
    for v in e['input']:
        d.append(v)

    d.rotate(e['k'])
    print('Solution 1: {}'.format(', '.join(map(str, d))))

    # Solution 2: 
    nums = e['input']; k = e['k']
    n = len(nums)
    k = k % n
    nums[:] = nums[n-k:] + nums[:n-k]

    print('Solution 2: {}'.format(', '.join(map(str, nums))))