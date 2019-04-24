#!/usr/bin/python3
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

import math

def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    if (abs(x) < 10):
        return x

    n = abs(x)

    digits = []
    tens_power = int(math.log(n, 10))

    for i in range(tens_power, -1, -1):
        p = 10**i
        div = n // p
        n = n % p

    digits.append(div)

    n = 0
    for i in range(tens_power+1):
        n += digits[i] * 10**i

    if x < 0:
        n = -n

    if (n < -2147483648 or n > 2147483647):
        return 0

    return n


print(reverse(-123))
