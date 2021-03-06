#!/usr/local/bin/python3.7

"""First Unique Character in a String

Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
"""

from collections import Counter

def firstUniqChar(s: str) -> int:
    c = Counter(s)

    for i, x in enumerate(s):
        if c[x] == 1:
            return i

    return -1

s = "aadadaadc"

print(firstUniqChar(s))


    