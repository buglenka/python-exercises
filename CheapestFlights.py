#!/usr/local/bin/python3.7

"""Cheapest Flights Within K Stops

There are n cities connected by m flights. Each fight starts from 
city u and arrives at v with a price w.

Now given all the cities and flights, together with starting city 
src and the destination dst, your task is to find the cheapest price 
from src to dst with up to k stops. If there is no such route, output -1.

Example 1:
Input: 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 1
Output: 200
Explanation: 
The graph looks like this:

The cheapest price from city 0 to city 2 with at most 1 stop costs 200, 
as marked red in the picture.
Example 2:
Input: 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 0
Output: 500
Explanation: 
The graph looks like this:

The cheapest price from city 0 to city 2 with at most 0 stop costs 500, 
as marked blue in the picture.
Note:

The number of nodes n will be in range [1, 100], with nodes labeled 
from 0 to n - 1.
The size of flights will be in range [0, n * (n - 1) / 2].
The format of each flight will be (src, dst, price).
The price of each flight will be in the range [1, 10000].
k is in the range of [0, n - 1].
There will not be any duplicated flights or self cycles.
"""
import sys
from typing import List
import heapq

def findCheapestPrice(n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
    graph = [[] for i in range(n)]
    for s, d, w in flights:
        graph[s].append((d,w))

    heap = [(0, src, K + 1)]
    while heap:
        price, town, stops = heapq.heappop(heap)

        if town == dst:
            return price

        if stops > 0:
            for d, p in graph[town]:
                heapq.heappush(heap, (price + p, d, stops - 1))

    return -1

    
n = 10
edges = [[3,4,4],[2,5,6],[4,7,10],[9,6,5],[7,4,4],[6,2,10],[6,8,6],[7,9,4],[1,5,4],[1,0,4],[9,7,3],[7,0,5],[6,5,8],[1,7,6],[4,0,9],[5,9,1],[8,7,3],[1,2,6],[4,1,5],[5,2,4],[1,9,1],[7,8,10],[0,4,2],[7,2,8]]
src = 6
dst = 0
k = 7

print(findCheapestPrice(n, edges, src, dst, k))


            
