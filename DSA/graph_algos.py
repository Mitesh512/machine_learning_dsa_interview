from typing import List, Tuple
from collections import defaultdict, deque
import heapq
# The first problem is to find the shortest path in a graph using Dijkstra's algorithm.
def get_graph(edges):
    graph = defaultdict(list)
    for u,v,w in edges:
        graph[u].append((v,w))
        graph[v].append((u,w))
    return graph
        
"""
1. Dijkstra's Algorithm (BFS with Priority Queue (Min Heap))
Single-source shortest path in weighted graphs (no negative edges)

✅ Use Case:
Find the shortest time/cost to reach all nodes from a source.

🧠 Time: O(E log V) with Min Heap (Priority Queue)


# grpah --> u: [(v,wt)], Edges: [(u,v,wt)]
{   0:[(1,5), (2,3)],
    1:[(0,5), (2,2), (3,1)],
    2:[(0,3), (1,2), (3,5)],
    3:[(1,1), (2,5)],
}

Source = 0 

0 : 0 
1 : inf
2 : inf
3 : inf

"""
def dijkstra(graph,start_node):
    distances = {node:float("inf") for node in graph.keys()}
    distances[start_node] = 0 
    visited = set()
    min_heap = [(0,start_node)] # dist, node
    while min_heap:
        dist, node = heapq.heappop(min_heap)  
        if node in visited:
            continue
        visited.add(node)
        for nbr,nbr_dist in graph[node]:
            if dist + nbr_dist < distances[nbr]:
                distances[nbr] = dist + nbr_dist
                heapq.heappush(min_heap,(distances[nbr], nbr))
    return distances

"""
2: Minimum Spanning Tree (MST) : Kruskal's Algorithm
Connect all nodes with minimum total cost, no cycles

✅ Use Case:
Network cabling, city connections, clustering

🧠 Time: O(E log E) (sort edges + Union-Find)
"""

class DisjointSet:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.size = [1 for _ in range(n)]
    
    def find(self,x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self,u,v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return False # no uinon is needed they belong to same component
        
        if self.size[pu] >= self.size[pv]:
            self.parent[pv] = pu
            self.size[pu] += self.size[pv]
        else:
            self.parent[pu] = pv
            self.size[pv] += self.size[pu]
        return True
    
    
def kruskal_min_spanning_tree(n,edges):
    ds = DisjointSet(n)
    min_spanning_tree_cost = 0 
    edges.sort(key= lambda x:x[2])
    
    for u,v,w in edges:
        if ds.union(u,v):
            min_spanning_tree_cost += w
            
    return min_spanning_tree_cost
    
    
"""
3. Bellman Ford:
The Bellman-Ford algorithm is a graph search algorithm that 
finds the shortest path from a single source vertex to all other vertices.
in a weighted graph, even if the graph has negative weight edges. 
It works by relaxing the edges iteratively to find the shortest path.

Handles negative weights; detects negative cycles
✅ Use Case:
Currency arbitrage, dynamic prices, route planning with penalties

🧠 Time: O(V * E)
Graph: Edges = V -1

""" 
def bellman_ford(n,edges,start):
    distances = [float("inf") for i in range(n)]
    distances[start] = 0
    #  Relax all edges (V - 1) times 5 vertices, Edges 15 
    for step in range(n-1):
        for u,v,w in edges:
            if distances[u] + w < distances[v]:
                distances[v] = distances[u] + w

    ## check for negative cycle
    for u,v,w in edges:
        # print("distances[u] + w , distances[v]",distances[u] + w , distances[v])
        if distances[u] + w < distances[v]:
            return "Negative Cycle in detected"
    return distances


"""
4. Floyd-Warshall Algorithm
All-pairs shortest path (handles negative weights, no negative cycles)

✅ Use Case:
Precomputing shortest paths between all pairs

Navigation systems, transitive closure

🧠 Time: O(V^3)
"""

def floyd_warshall(graph):
    """
    graph: 2D matrix graph[i][j] = weight or inf
    returns: distance matrix
    """
    n = len(graph)
    dist = [[graph[i][j] for j in range(n)] for i in range(n)]
    for k in range(n):  # intermediate
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist

# Example
INF = float('inf')
graph = [
    [0, 3, INF, 5],
    [2, 0, INF, 4],
    [INF, 1, 0, INF],
    [INF, INF, 2, 0]
]
for row in floyd_warshall(graph):
    print(row)


### Bipartite Graph
class Solution:
    def get_graph(self,n,edges):
        graph = {i:[] for i in range(n+1)}
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        return graph


    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        """
        TC O(V+E), SC: O(V)
        BFS is more intutive

        What is a Bipartite Graph?
            A graph is bipartite if:
            You can split its nodes into two sets, say U and V
            Such that no two nodes in the same set are connected
            Another way to say it: you can color the graph using only 2 colors such that no two adjacent nodes share the same color.

        Intution:

            Think of a bipartite graph as a "no triangle between 3 friends" network.
            If one node is red, all its neighbors must be blue, and their neighbors must be red again, and so on.
            If you ever find two adjacent nodes with the same color, the graph is not bipartite.
            
            0 - 1
            |   |
            3 - 2 is a Bipartite

            0 - 1
             \ /
              2  ← triangle → not bipartite


        Applications:
            Graph Coloring
            Team Assignment (e.g. can we divide people into two rival teams?)
            Checking if a graph has odd-length cycles (bipartite graphs cannot)
            Matching problems (e.g., in bipartite matching or flow networks)
        """
        #### BFS Approach
        graph = self.get_graph(n,dislikes)
        color = [-1 for _ in range(n+1)] # -1: unvisited, 0 and 1 are two colors
        # BFS approach
        for start in range(n):
            if color[start] == -1:
                q = deque([start])
                # assign the color to the start node you can use any
                # 0 or 1
                color[start] = 1
                while q:
                    node = q.popleft()
                    for nbr in graph[node]:
                        if color[nbr] == -1:
                            # assign color
                            color[nbr] = 1 - color[node]
                            q.append(nbr)
                        elif color[nbr] == color[node]:
                            # oo oh! this is same color as previous node
                            return False # not possible to divide
        return True

if __name__=="__main__":
    # Example of edges with weights assigned to it
    # edges = [
    #     (0, 1, 1),
    #     (0, 2, 4),
    #     (1, 2, 2),
    #     (1, 3, 5),
    #     (2, 3, 1)
    #     ]
    # graph = get_graph(edges)
    # start_node = 0
    
#     graph = {
#     'A': [('B', 1), ('C', 4)],
#     'B': [('C', 1)],
#     'C': []
# }
#     start_node = "A"
    
    # shortest_paths = dijkstra(graph, start_node)
    # print(shortest_paths)
    # print("Shortest paths from node", start_node)
    # for node, distance in shortest_paths.items():
    #     print(f"Distance to {node}: {distance}")
    
    ### Min spanning Tree
    #  u,v,wt
    # edges = [
    #         ( 0, 1, 1),
    #         ( 0, 2, 4),
    #         ( 1, 2, 3),
    #         ( 1, 3, 2),
    #         ( 2, 3, 5)]
    # n = 4
    # print(kruskal_min_spanning_tree(n,edges))

    ### Bellman Ford Example
    
    edges = [
    (0, 1, -5),
    (1, 2, -2),
    (0, 2, -10)]
    print(bellman_ford(3, edges, 0)) 
    
    edges = [
    (0, 1, -5),
    (1, 2, -2),
    (2, 0, -10)]
    print(bellman_ford(3, edges, 0)) 
    
    edges = [
    (0, 1, 1),
    (1, 2, -1),
    (2, 0, -1)
        ]
    print(bellman_ford(3, edges, 0))




