#!/usr/local/bin/python3.7

"""Pairs of Songs With Total Durations Divisible by 60

Pairs of Songs With Total Durations Divisible by 60

In a list of songs, the i-th song has a duration of time[i] seconds. 

Return the number of pairs of songs for which their total duration in 
seconds is divisible by 60.  Formally, we want the number of indices 
i < j with (time[i] + time[j]) % 60 == 0.

Example 1:

Input: [30,20,150,100,40]
Output: 3
Explanation: Three pairs have a total duration divisible by 60:
(time[0] = 30, time[2] = 150): total duration 180
(time[1] = 20, time[3] = 100): total duration 120
(time[1] = 20, time[4] = 40): total duration 60
Example 2:

Input: [60,60,60]
Output: 3
Explanation: All three pairs have a total duration of 120, which is divisible by 60.

Note:

1 <= time.length <= 60000
1 <= time[i] <= 500
"""
from typing import List

DIVISOR = 60

def numPairsDivisibleBy60_1(time: List[int]) -> int:
    pairs = set()

    for i in range(len(time)):
        for j in range(i+1, len(time)):
            if ((time[i] + time[j]) % DIVISOR == 0):
                p = (i, j)
                if p not in pairs:
                    pairs.add(p)
                    
    return len(pairs)

def numPairsDivisibleBy60_2(time: List[int]) -> int:
    pairs = dict()

    count = 0

    for i, t in enumerate(time):
        comp_rem = (DIVISOR - (t % DIVISOR)) % DIVISOR
        if comp_rem in pairs:
            count += len(pairs[comp_rem])

        rem = t % DIVISOR

        if rem in pairs:
            pairs[rem].append(i)
        else:
            pairs[rem] = [i]

    return count

times_1 = [30,20,150,100,40]
times_2 = [60,60,60]

pairsCount_1 = numPairsDivisibleBy60_1(times_2)
pairsCount_2 = numPairsDivisibleBy60_2(times_2)

print('{} {}'.format(pairsCount_1, pairsCount_2))