#!/usr/local/bin/python3.7

""" Climbing a Stair 

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. 
In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""

from typing import List

def climbStairs(n: int) -> int:
    if (n == 1):
        return 1

    dp = [0]*(n + 1)
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]

def climbStairs123(n: int) -> int:
    """Recursion
    """
    def steps(n: int) -> int:
        if (n == 0):
            return 1
        elif (n < 0):
            return 0

        c = steps(n-1)
        c += steps(n-2)
        c += steps(n-3)

        return c

    return steps(n)

def climbStairs123dp(n: int) -> int:
    """Dynamic Programming:

    Bottom-Up Solution
    """
    dp = [0]*(n)
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n):        
        dp[i] = sum(dp[i-3:i])

    return sum(dp[n-3:n])

def climbStairs123memo(n: int) -> int:
    """Dynamic Programming:

    Top-Down Solution
    """
    def steps(N: int, memo: List[int]) -> int:
        if (N == n):
            return 1
        elif (N > n):
            return 0
        elif (memo[N] == -1):
            memo[N] = steps(N+1, memo) + \
                        steps(N+2, memo) + \
                            steps(N+3, memo)

        return memo[N]

    memo = [-1]*n

    return steps(0, memo)

n = 4

print(climbStairs123memo(n))