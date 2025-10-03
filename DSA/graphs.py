"""
Graph Traversal: (Adj List, Adj Matrix)
    DFS
    BFS


Shortest Path (Edge weight):
    - Dijkstra's Algorithm (Positive weights) TC: E logs(V) ---> shortest path between a source to all nodes (destination node) with  positive edge weights
    - Bellman-Ford (Negative Weightts): TC: ExV ---> shortest path between a source to all nodes (destination node) destination node with even with negative weights,  (Negative Cycle Identification)
    - Floyd Warshall: TC (V^3): shortest path from all nodes to all nodes

# ---- Done with above
Minimum Spanning Tree: It will have V-1 Edges. ( to connect to V points we just need V-1 Edges)
    - Prim's Algorithm
    - Kruskal's Algorithm (Disjopint Set Data Structure)

Topological Sort: (Directed Graphs, depndency matters)
    - Indegree

Bipartitie Graph: (Not possible for odd cycles)
    - To separate graph into two entities.
    
"""

from collections import deque
def dfs_adj_list(n,adj_list):
    """
    you are given nodes n and an adj_list {1:[1,2]}
    consider 0 based node indexing.
    It is given that the graph can have components as well as connected, you need to traverse the whole array
    perform dfs and pring elements or you can put the traversal in an array
    
    adj_list = {
        0:[1,2,3],
        1:[0,3],
        2:[0,4],
        3:[1,0,5],
        4:[2,5],
        5:[4,3], 
    }
    visited = set() --> {0,1,3,5,4,2}
    traversal = []-->[0,1,3,5,4,2]    
    TC : (V+E)
    """
    visited = set()
    traversal = []
    
    def dfs(node,visited, traversal):
        visited.add(node)
        traversal.append(node)
        for nbr in adj_list[node]:
            if nbr not in visited:
                visited,traversal = dfs(nbr,visited, traversal)
        return visited, traversal   
    
    for i in range(n):
        if i not in visited:
            visited, traversal = dfs(i,visited, traversal)
    return traversal

adj_list = {
        0:[1,2,3],
        1:[0,3],
        2:[0,4],
        3:[1,0,5],
        4:[2,5],
        5:[4,3], 
    }
# print(dfs_adj_list(6,adj_list))

def bfs_adj_list(n,adj_list):
    """
    you are given nodes n and an adj_list {1:[1,2]}
    consider 0 based node indexing.
    It is given that the graph can have components as well as connected, you need to traverse the whole array
    perform bfs and pring elements or you can put the traversal in an array
    TC : (V+E)
    adj_list = {
        0:[1,2,3],
        1:[0,3],
        2:[0,4],
        3:[1,0,5],
        4:[2,5],
        5:[4,3], 
    }
    visited = set() --> {0,1,2,3,4,5}
    traversal = []-->[0,1,2,3,4,5]
    q = 0,1,2,3,4,5 []
    """
    
    traversal = []
    visited = set()
    for i in range(n):
        if i not in visited:
            q = deque([i])
            visited.add(i)
            while q:
                node = q.popleft()
                traversal.append(node)
                for nbr in adj_list[node]:
                    if nbr not in visited:
                        visited.add(nbr)
                        q.append(nbr)
    return traversal
                        
                
# print(bfs_adj_list(6,adj_list))


def dfs_adj_matrix(matrix):
    """
    Perform dfs on adjecency matrix (NxN), consider 0 based indexing for the nodes, size of the matrix will be n
    n is equal to number of nodes in the graph
    return traversal
    the graph can have components
    Here is an example of the matrix
    matrix =[
         0  1  2  3  4  5
    0   [0, 1, 1, 1, 0, 0],
    1   [1, 0, 0, 1, 0, 0],
    2   [1, 0, 0, 0, 1, 0],
    3   [1, 1, 0, 0, 0, 1],
    4   [0, 0, 1, 0, 0, 1],
    5   [0, 0, 0, 1, 1, 0]
    ]
    visited = {} --> {0,1,3,5,4,2}
    traversal = [] --> [0,1,3,5,4,2]
    dfs call--> 0, 1, 3, 5,4,2
    """
    visited = set()
    traversal = []
    def dfs(node,visited,traversal):
        visited.add(node)
        traversal.append(node)
        for j in range(len(matrix)):# range(6)--> 0,1,2,3,4,5
            if matrix[node][j] ==1 and j not in visited:
                visited, traversal = dfs(j,visited,traversal)
        return visited, traversal
    # we need to traverse to each node
    for i in range(len(matrix)): # range(6)--> 0,1,2,3,4,5
        if i not in visited:
            visited, traversal = dfs(i,visited,traversal)
    
    return traversal
        
    
    

matrix =[
        [0, 1, 1, 1, 0, 0],
        [1, 0, 0, 1, 0, 0],
        [1, 0, 0, 0, 1, 0],
        [1, 1, 0, 0, 0, 1],
        [0, 0, 1, 0, 0, 1],
        [0, 0, 0, 1, 1, 0]
    ]


# print(dfs_adj_matrix(matrix))



def bfs_adj_matrix(matrix):
    """ Perform bfs on adjecency matrix, consider 0 based indexing for the nodes, size of the matrix will be n
    n is equal to number of nodes in the graph
    return traversal
    the graph can have components
    
    Here is an example of the matrix
    matrix =[
         0  1  2  3  4  5
    0   [0, 1, 1, 1, 0, 0],
    1   [1, 0, 0, 1, 0, 0],
    2   [1, 0, 0, 0, 1, 0],
    3   [1, 1, 0, 0, 0, 1],
    4   [0, 0, 1, 0, 0, 1],
    5   [0, 0, 0, 1, 1, 0]
    ]
    visited = {} --> {0,1,2,3,4,5}
    traversal = [] --> [0,1,2,3,4,5]
    q = 0,1,2,3,4,5  <-- []
    """
    n = len(matrix) # 6
    visited = set()
    traversal = []
    for i in range(n): # 0,1,2,3,4,5
        if i not in visited:
            q = deque([i])
            visited.add(i)
            while q:
                node = q.popleft()
                traversal.append(node)
                for j in range(n): # 0,1,2,3,4,5
                    if matrix[node][j]==1 and j not in visited:
                        visited.add(j)
                        q.append(j)
    return traversal
                        
                
        
# print(bfs_adj_matrix(matrix))









from collections import deque, defaultdict

# Approach 1: Graph input as Edge List
def build_graph_from_edges(edges):
    # graph = {} 
    # for u ,v in edges:
    #     if u in graph.keys():
    #         graph[u].append(v)
    #     else:
    #         graph[u] = [v]
    #     if v in graph.keys():
    #         graph[v].apend(u)
    #     else:
    #         graph[v] = [u]
    # return graph
    
    """

    Edges: [[0,1], [0,2], [0,3], [1,3], [2,4], [3,5], [4,5], [9,10]] 
    
    6, 7, 8 are just nodes
    
    graph= {
        0:[1,2,3],
        1:[0,3],
        2:[0,4],
        3:[1,0,5],
        4:[2,5],
        5:[4,3],
        6:[],
        7:[],
        8:[],
        9:[10],
        10:[9]
    }
    
    """
    
    
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)  # Assuming undirected graph
    return graph


def build_adjacency_graph_from_edges(edges):
    # get vertices first:
    V = 0
    for u,v in edges:
        V = max(V, u, v)
    
    # if graph is strating from zero we will add 1 to V
    V = V+1
    matrix_graph = [[0 for _ in range(V)] for _ in range(V)]
    
    for u,v in edges:
        matrix_graph[u][v] = 1
        matrix_graph[v][u] = 1
    return matrix_graph


# Approach 2: Graph input as Adjacency Matrix
def build_graph_from_matrix(matrix):
    graph = defaultdict(list)
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:  # Edge exists
                graph[i].append(j)
                # below line is not required as it will be convered directly
                # graph[j].append(i)
    return graph


# BFS for adjecency list Traversal
def bfs(adj_list, start):
    visited = set([start])
    queue = deque([start])
    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for neighbor in adj_list[node]:
            if neighbor not in visited:
                visited.add(neighbor)  # mark as visited when enqueuing
                queue.append(neighbor)


# DFS Traversal for adjacency list (Recursive)
def dfs(adj_list,node,visited):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for nbr in adj_list[node]:
            dfs(adj_list,nbr,visited)



from collections import deque

def bfs_matrix(adj_matrix, start):
    n = len(adj_matrix)
    visited = set()
    queue = deque([start])
    visited.add(start)
    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for neighbor in range(n):
            if adj_matrix[node][neighbor] == 1 and neighbor not in visited:
                visited.add(node)
                queue.append(neighbor)


        

def dfs_adj_matrix(matrix):
    """
    There is a difference from number of islands problem.
    Here in adjacency matrix it represents how one node is connected
    to other node
    
    M = [
  [0, 1, 0],  # Node 0 is connected to Node 1
  [1, 0, 1],  # Node 1 is connected to Nodes 0 and 2
  [0, 1, 0]   # Node 2 is connected to Node 1
    ]
    if we see it ideally 0,1 and 2 are connected. there is only 1 component
    
    In case of number of island problem this will give us 4 different islands
    
    In this case understand it like a adjacency list only
    Now perform DFS
    
    # Adjacency Matrix  (nxn) # nodes = n 
#0 1 2
[0,1,0], 0
[1,0,1], 1
[0,1,0], 2

output = 1

# Provinces
# # Number of nodes: n = 3
[[1,1,0],
 [1,1,0],
 [0,0,1]]
Output: 2

[[1,0,0],
 [0,1,0],
 [0,0,1]]
Output: 3

# Islands # Number of nodes: mxn ---> 4x5 = 20
["1","1","1","1","0"],
["1","1","0","1","0"],
["1","1","0","0","0"],
["0","0","0","0","0"]
Output: 1

# Number of nodes: mxn ---> 4x5 = 20
["1","1","0","0","0"],
["1","1","0","0","0"],
["0","0","1","0","0"],
["0","0","0","1","1"]
Output: 3

    """
    n = len(matrix)
    visited = [0 for _ in range(n)]
    count = 0
    
    def dfs(node):
        if visited[node] == 0:
            visited[node] = 1
            # I will check nbrs or friends of node to find to which it is connected
            # this basically means I will be traversing the node(th) row the adjacency matrix
            # if lets say zeroth node has visited 1 and 2 
            for j in range(n):
                if matrix[node][j] == 1 and visited[j]==0:
                    dfs(j)
                    
    for i in range(n):
        if visited[i] == 0:
            count +=1
            dfs(i)
            
    return count
    
    
                    

              
class Disjointset:
    def __init__(self,n):
        # initialzise each element as its own parent
        self.parent = list(range(n+1))
        self.rank = [0 for _ in range(n+1)]
        self.size = [1 for _ in range(n+1)]
        print(self.rank)
        print(self.size)
        
    
    def find(self,x):
        if self.parent[x] == x:
            # ultimate parent points to himself
            return x
        # find the ultimate parent until you find the it
        return self.find(self.parent[x])
      
    def union_by_rank(self,x,y):
        # Union by Rank
        px = self.find(x)
        py = self.find(y)
        
        if px == py:
            # there is no need to perfom union the ultimate parent is same
            return 
        
        # Attach smaller rank to larger rank tree or graph
        print(x,y,px,py,self.rank)
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            # if both are of equal rank merge them
            # either way is fine but whoever you are making parent increase its rank
            self.parent[py] = px
            self.rank[px] += 1
    
    def union_by_size(self,x,y):
        px = self.find(x)
        py = self.find(y)
        
        if px==py:
            return 

        if self.size[px] < self.size[py]:
            self.parent[px] = py
            self.size[py] += self.size[px]
        else:
            self.parent[py] = px
            self.size[px] += self.size[py]
            
            
    
    def connected(self,x,y):
        return self.find(x) == self.find(y)

        
def DAG(number_of_nodes, edges):
    """
    This is code for Directed Acyclic Graph
    """
    graph = defaultdict(list)
    indegree = [0] * number_of_nodes

    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1

    # Topological Sort using Kahn's Algorithm
    queue = deque([i for i in range(number_of_nodes) if indegree[i] == 0])
    topological_order = []

    while queue:
        node = queue.popleft()
        topological_order.append(node)

        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return topological_order if len(topological_order) == number_of_nodes else []
    
        
    





if __name__ == "__main__":
    pass
    
    # ds = Disjointset(5)
    # ds.union_by_rank(0,1)
    # ds.union_by_rank(2,3)
    # print(ds.connected(0,1))
    # print(ds.connected(0,2))
    # ds.union_by_rank(1,2)
    # print(ds.connected(0,3))
    
    # ------------------ TEST CASE 1: EDGE LIST -------------------
    # # print("Graph Input: Edge List")
    # edges = [[0, 1], [0, 2], [1, 3], [2, 4],[0,3],[4,5],[3,5]]
    
    # adj_list = {
    #     0:[1,2,3],
    #     1:[0,3],
    #     2:[0,4],
    #     3: [1,0,5],
    #     4:[2,5],
    #     5:[4,3], 
    # }
    # matrix =[
    #     [0, 1, 1, 1, 0, 0],
    #     [1, 0, 0, 1, 0, 0],
    #     [1, 0, 0, 0, 1, 0],
    #     [1, 1, 0, 0, 0, 1],
    #     [0, 0, 1, 0, 0, 1],
    #     [0, 0, 0, 1, 1, 0]
    # ]
    
    # graph1 = build_graph_from_edges(edges)

    # print("BFS Traversal:")
    # bfs(graph1, 0)

    # print("\nDFS Traversal:")
    # visited = set()
    # dfs(graph1, 0, visited)

    # print("\n\n------------------")

    # # # ------------------ TEST CASE 2: ADJACENCY MATRIX -------------------
    # print("\nGraph Input: Adjacency Matrix")
    # matrix = [
    #     [1, 1, 1, 0, 0],
    #     [1, 1, 1, 1, 0],
    #     [1, 0, 1, 0, 1],
    #     [0, 1, 1, 1, 1],
    #     [0, 0, 1, 0, 1]
    # ]
    # adj_2 = build_graph_from_matrix(matrix)

    # print("BFS Traversal:")
    # bfs(adj_2, 0)

    # print("\nDFS Traversal:")
    # visited = set()
    # dfs(adj_2, 0, visited)
    
    # bfs_traversal = bfs_matrix(matrix, (0,0))
    # print("This is my Matrix BFS traversal",bfs_traversal)

    # dfs_traversal = dfs_matrix(matrix,(0,0))
    # print("This is DFS traversal: ", dfs_traversal)
