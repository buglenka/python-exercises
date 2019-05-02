#!/usr/local/bin/python3.7

"""Trapping Rain Water

Given n non-negative integers representing an elevation 
map where the width of each bar is 1, compute how much 
water it is able to trap after raining.

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""

from typing import List

def trap(height: List[int]) -> int:
    """Using dynamic programming
    3 Steps:
        - Find max height upto the point from the left
        - Find max height upto the point from the right
        - Choose the minimum of 2 heights and substract initial height
    """
    if not height:
        return 0

    l = len(height)
    
    max_right = [0] * l
    max_left = [0] * l
    
    max_right[0] = height[0]
    
    for i in range(1, len(height)):
        max_right[i] = max(height[i], max_right[i - 1])
        
    max_left[len(height) - 1] = height[len(height) - 1]
    
    for i in range(len(height) - 2, -1, -1):
        max_left[i] = max(height[i], max_left[i + 1])
        
    res = 0
    
    for i in range(l):
        res += min(max_right[i], max_left[i]) - height[i]    
    
    return res

hs = [0,1,0,2,1,0,1,3,2,1,2,1]

print(trap(hs))