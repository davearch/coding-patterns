# topological sort
# O(V+E) time
# O(V+E) space

# Given a directed graph, find the topological sorting of its vertices.
# ex. vertices=4, edges=[[3,2],[3,0],[2,0],[2,1]]
# output:
# [3,2,0,1]
# [3,2,1,0]

# output = [3,2,1,0]
# queue = []
from collections import deque, defaultdict
from typing import List

class Node:
    def __init__(self):
        self.indegrees = 0
        self.children = []

def topologicalSort(vertices: int, edges: List[List[int]]) -> List[int]:
    output = []
    if vertices <= 0:
        return output

    # instantiate adj list (graph)
    graph = defaultdict(Node)
    for edge in edges:
        parent = edge[0]
        child = edge[1]
        graph[parent].children.append(child)
        graph[child].indegrees += 1

    sources = deque()
    for node in graph:
        if not graph[node].indegrees:
            sources.append(node)

    while sources:
        current = sources.popleft()
        for child in graph[current].children:
            graph[child].indegrees -= 1
            if not graph[child].indegrees:
                sources.append(child)
        output.append(current)

    if len(output) != vertices:
        return []

    return output
