#!/usr/local/bin/python3.7

"""Valid Palindrome

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
"""

import string

def isPalindrome(s: str) -> bool:
    alphabet = string.ascii_lowercase + string.digits

    alphanumeric_s = list(filter(lambda x: x in alphabet, s.lower()))

    if len(alphanumeric_s) < 2:
        return True
    
    tail_len = len(alphanumeric_s) // 2
    
    left = alphanumeric_s[:tail_len]
    right = alphanumeric_s[-tail_len:]
    
    return left == right[::-1]


s = "race a car"

print(isPalindrome(s))