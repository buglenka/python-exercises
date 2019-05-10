#!/usr/local/bin/python3.7

"""Is Graph Bipartite?

Given an undirected graph, return true if and only if it is bipartite.

Recall that a graph is bipartite if we can split it's set of nodes 
into two independent subsets A and B such that every edge in the graph 
has one node in A and another node in B.

The graph is given in the following form: graph[i] is a list of indexes j 
for which the edge between nodes i and j exists.  Each node is an integer 
between 0 and graph.length - 1.  There are no self edges or parallel edges: 
graph[i] does not contain i, and it doesn't contain any element twice.

Example 1:
Input: [[1,3], [0,2], [1,3], [0,2]]
Output: true
Explanation: 
The graph looks like this:
0----1
|    |
|    |
3----2
We can divide the vertices into two groups: {0, 2} and {1, 3}.
Example 2:
Input: [[1,2,3], [0,2], [0,1,3], [0,2]]
Output: false
Explanation: 
The graph looks like this:
0----1
| \  |
|  \ |
3----2
We cannot find a way to divide the set of nodes into two independent 
subsets.
 

Note:

graph will have length in range [1, 100].
graph[i] will contain integers in range [0, graph.length - 1].
graph[i] will not contain i or duplicate values.
The graph is undirected: if any element j is in graph[i], then i will 
be in graph[j].
"""
from typing import List

def isBipartite(graph: List[List[int]]) -> bool:
    if len(graph) < 2:
        return True
    
    UNDEF = 2

    # Let's mark all vertexes with flags '0' or '1' (two groups)
    marked = [UNDEF] * len(graph)

    v = 0; q = []
    for i in range(len(graph)):
        if marked[i] != UNDEF:
            continue

        q.append(i); marked[i] = 0
        
        while(len(q) > 0):
            v = q.pop()
            group = marked[v] ^ 1 # opposite group

            for v_next in graph[v]:
                if (marked[v_next] == UNDEF):
                    marked[v_next] = group
                    q.append(v_next)

                elif (marked[v_next] != group):
                    return False

    return True

a = [[1,3], [0,2], [1,3], [0,2]]
print(isBipartite(a))

a = [[2,4],[2,3,4],[0,1],[1],[0,1],[7],[9],[5],[],[6],[12,14],[],[10],[],[10],[19],[18],[],[16],[15],[23],[23],[],[20,21],[],[],[27],[26],[],[],[34],[33,34],[],[31],[30,31],[38,39],[37,38,39],[36],[35,36],[35,36],[43],[],[],[40],[],[49],[47,48,49],[46,48,49],[46,47,49],[45,46,47,48]]
print(isBipartite(a))

a = [[1,2,3], [0,2], [0,1,3], [0,2]]
print(isBipartite(a))
        






