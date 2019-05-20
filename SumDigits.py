#!/usr/local/bin/python3.7

"""Add Digits

Given a non-negative integer num, repeatedly add all its digits 
until the result has only one digit.

Example:

Input: 38
Output: 2 
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
             Since 2 has only one digit, return it.
Follow up:
Could you do it without any loop/recursion in O(1) runtime?

"""

def addDigits(num: int) -> int:
    while(num > 9):
        num = sum(map(int, str(num)))

    return num


num = 1234

print(addDigits(num))




