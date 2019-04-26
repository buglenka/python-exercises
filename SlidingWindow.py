#!/usr/local/bin/python3.7

"""Sliding Window Median

Median is the middle value in an ordered integer list. 
If the size of the list is even, there is no middle value. So the median 
is the mean of the two middle value.

Examples: 
[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Given an array nums, there is a sliding window of size k which is moving 
from the very left of the array to the very right. You can only see the k 
numbers in the window. Each time the sliding window moves right by one position. 
Your job is to output the median array for each window in the original array.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Median
---------------               -----
[1  3  -1] -3  5  3  6  7       1
 1 [3  -1  -3] 5  3  6  7       -1
 1  3 [-1  -3  5] 3  6  7       -1
 1  3  -1 [-3  5  3] 6  7       3
 1  3  -1  -3 [5  3  6] 7       5
 1  3  -1  -3  5 [3  6  7]      6
Therefore, return the median sliding window as [1,-1,-1,3,5,6].

Note: 
You may assume k is always valid, ie: k is always smaller than input array's size 
for non-empty array.
"""

from typing import List
from bisect import *

def medianSlidingWindow_1(nums: List[int], k: int) -> List[float]:
    result = []
    window = []

    for i, v in enumerate(nums[0:k-1]):
        window.append((i, v))
    
    window.sort(key = lambda x: x[1])

    i = 0
    while(i <= len(nums) - k):
        j = i + k
        next_num = nums[j-1]

        # Insert a next value in a sorted array
        inserted = False
        for idx, v in enumerate(window):
            curr_num = v[1]
            if (next_num < curr_num):
                inserted = True
                window.insert(idx, (j-1, next_num))
                break

        if not inserted:
            window.append((j-1, next_num))

        middle = k//2
            
        if (k % 2 > 0): # odd
            _, v = window[middle]

            result.append(float(v))
        else:
            # k is even
            left_v = window[middle-1][1]
            right_v = window[middle][1]
            result.append((left_v + right_v) / 2.0)
        
        window.remove((i, nums[i]))

        i += 1
        
    return result


def medianSlidingWindow_2(nums: List[int], k: int) -> List[float]:
    win, res=nums[:k],[]
    win.sort()
    odd = k % 2
    
    for i, num in enumerate(nums[k:],k):
        if odd:
            res.append(win[(k-1)//2]*1.0)
        else:
            res.append((win[k//2]+win[(k//2)-1])/2.0)

        win.pop(bisect(win,nums[i-k])-1)
        insort(win,nums[i])
    if odd:
        res.append(win[(k-1)//2]*1.0)
    else:
        res.append((win[k//2]+win[(k//2)-1])/2.0)
    return res

nums = [7,0,3,9,9,9,1,7,2,3]
# nums = [1,2]
k = 6

print(medianSlidingWindow_1(nums,k))