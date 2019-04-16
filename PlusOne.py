#!/usr/local/bin/python3.7

"""Plus One
Given a non-empty array of digits representing a non-negative 
integer, plus one to the integer.

The digits are stored such that the most significant digit is 
at the head of the list, and each element in the array contain 
a single digit.

You may assume the integer does not contain any leading zero, 
except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
"""

from typing import List

def plusOne(digits: List[int]) -> List[int]:
    l = len(digits)
    
    for i in range(l-1, -1, -1):     
        if digits[i] == 9:
            digits[i] = 0
        else:
            digits[i] += 1
            return digits
    
    digits[0] = 1
    digits.append(0)
    
    return digits


d = [8,9,9]

b = plusOne(d)

print('{}'.format(', '.join(map(str, b))))