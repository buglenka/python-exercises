#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Reverse Integer (https://leetcode.com/problems/reverse-integer/description/)

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321

Example 2:

Input: -123
Output: -321

Example 3:

Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store integers 
within the 32-bit signed integer range: [−2^31,  2^31 − 1]. 
For the purpose of this problem, assume that your function returns 0 when 
the reversed integer overflows.
"""

def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    if (x == 0) or (x < -2**31) or (x > 2**31): 
        return 0
        
    divisor = 10
    sign = x < 0;
        
    if (sign):
        x = -x
        
    rems = []
    while(x != 0):
        digit = int(x % divisor)
        x = int(x /divisor)
            
        rems.append(digit)
        
    result = rems.pop()
    i = 0
    while(len(rems) != 0):
        i += 1
        result += rems.pop() * (divisor**i)
            
    if (result > 2**31): 
        return 0
            
    if (sign):
        return -result
    else:
        return result


print(reverse(-123))
