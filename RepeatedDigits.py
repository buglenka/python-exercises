#!/usr/local/bin/python3.7

"""Numbers With Repeated Digits

Given a positive integer N, return the number of positive integers 
less than or equal to N that have at least 1 repeated digit.

 

Example 1:

Input: 20
Output: 1
Explanation: The only positive number (<= 20) with at least 1 repeated 
digit is 11.
Example 2:

Input: 100
Output: 10
Explanation: The positive numbers (<= 100) with atleast 1 repeated digit 
are 11, 22, 33, 44, 55, 66, 77, 88, 99, and 100.
Example 3:

Input: 1000
Output: 262
 

Note:

1 <= N <= 10^9
"""

def numDupDigitsAtMostN(N: int) -> int:
    # Number = 234
    # [2, 3, 5]
    # Count all permutations:
    # XX, X
    # 1XX, 20X - 21X, 230 - 234  
    digits = list(map(int, str(N + 1)))
    l = len(digits)
    count = 0

    def count_permutations(n, m: int) -> int:
        return 1 if m == 0 else count_permutations(n, m - 1) * (n - m + 1)

    # 1. Count all permutations of numbers lenght < l
    for ll in range(1, l):
        count += 9 * count_permutations(9, ll - 1)

    # 2. Count all permutations with prefixes the same as N
    seen = set()
    for i, digit in enumerate(digits):
        # prefix = digits[:i] + current digit
        # current digit < digits[i]
        for x in range(1 if i == 0 else 0, digit):
            if (x in seen):
                continue

            count += count_permutations(9 - i, l - (i + 1))

        if digit in seen:
            break
            
        seen.add(digit)
    
    return N - count


N = [20, 11, 100, 1000]

for n in N:
    print(numDupDigitsAtMostN(n))
    




