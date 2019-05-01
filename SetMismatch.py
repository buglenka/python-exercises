#!/usr/local/bin/Python3.7

"""Set Mismatch

The set S originally contains numbers from 1 to n. 
But unfortunately, due to the data error, one of the numbers 
in the set got duplicated to another number in the set, which 
results in repetition of one number and loss of another number.

Given an array nums representing the data status of this set 
after the error. Your task is to firstly find the number occurs 
twice and then find the number that is missing. Return them in the form of an array.

Example 1:
Input: nums = [1,2,2,4]
Output: [2,3]
Note:
The given array size will in the range [2, 10000].
The given array's numbers won't have any order.
"""

from typing import List

def findErrorNums(nums: List[int]) -> List[int]:
    if len(nums) < 2:
        return []

    nums.sort()
    dupl = 0; missed = 0

    prev = nums[0]
    for i in range(1, len(nums)):
        curr = nums[i]

        if (curr - prev) != 1:
            if curr == prev:
                dupl = curr

                if i == 1:
                    missed = dupl - 1
            else:
                missed = prev + 1

        prev = curr

        if (dupl != 0 and missed != 0):
            break

    if (missed == 0) and (len(nums) == 2):
        missed = 3 - dupl

    if (missed == 0):
        if nums[0] == 1:
            missed = nums[-1] + 1
        else:
            missed = 1

    return [dupl, missed]
            
nums = [1,3,3]

print(findErrorNums(nums))
        
            
        