from typing import List, Tuple
"""
Problem:
 1: Friend Circles
🧠 Google-style framing:
Imagine you're designing a social graph for a small internal tool at Google.
Each employee can be “friends” with other employees.
Friendship is bidirectional and transitive — meaning if A is friends with B and B is friends with C, then A is friends with C.

You're given a 2D matrix M of size n x n where M[i][j] = 1 means employee i and j are friends.

Return the number of friend circles (i.e., distinct groups of connected employees).
🔧 Constraints:
1 <= n <= 200
M[i][j] == 1 means friendship, M[i][j] == M[j][i]
Every employee is friends with themselves: M[i][i] == 1

Solution:
This looks like finding number of islands, I can use DFS to find all distinct groups
start traversing the matring from top left to bottom right
if I find 1 , I will first increase the count of friend circle, and apply dfs
since it is connected in 4 directions to avoid going to cases which I have seen earlier I 
can have a visited set. 

"""

class friend_disjoint_set:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.size = [1 for i in range(n)]
        
    def find(self,x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        
        return self.parent[x]

    def union(self,u,v):
        pu = self.find(u)
        pv = self.find(v)
        
        if pu == pv:
            return # there is no need to merge
        
        if self.size[pu] >= self.size[pv]:
            self.parent[pv] = pu
            self.size[pu] += self.size[pv]
        else:
            self.parent[pu] = pv
            self.size[pv] += self.size[pu]

        return

def find_friend_circle(friend_grid):
    
    n = len(friend_grid)
    
    ds = friend_disjoint_set(n)
    
    for i in range(n):
        for j in range(i+1,n):
            if friend_grid[i][j]==1:
                ds.union(i,j)
    
    friend_circles = 0
    
    for i in range(n):
        if ds.find(i) == i:
            friend_circles +=1
    
    return friend_circles
    


# friend_grid = [[1,0,1,0], [0,1,0,0],[1,0,1,1],[1,0,0,1]]
# print(find_friend_circle(friend_grid))       

"""
Problem 2: Number of Islands (Disjoint Set Approach)
🧠 Google-style framing:
You're working on a geographic mapping system at Google. 
A satellite sends back a grid of land (1) and water (0) readings. 
You want to analyze how many distinct landmasses (islands) exist. 
Two land cells are considered part of the same island if they are connected horizontally or vertically (not diagonally).

💡 Problem Statement:
You are given a 2D grid grid of '1's (land) and '0's (water).
Return the number of islands.

Each cell in the grid is connected 4-directionally (up, down, left, right).
Islands are surrounded by water and are formed by connecting adjacent lands.

🔧 Constraints:
1 <= m, n <= 300

grid[i][j] is '0' or '1'

🧪 Example:
python
Copy
Edit
Input:
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

Output: 3
"""




class island_disjoint_set:
    def __init__(self,grid_size):
        self.parent = [i for i in range(grid_size)]
        self.size = [1 for i in range(grid_size)]
    
    def find(self,x):
        if self.parent[x] !=x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    
    def union(self,u,v):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return False# islands are already connected
    
        if self.size[pu] >= self.size[pv]:
            self.parent[pv] = pu
            self.size[pu] += self.size[pv]
        
        else:
            self.parent[pu] = pv
            self.size[pv] += self.size[pu]
        
        return True

def get_1d_node(r,c,n):
    return r*n + c

    
def is_in_grid(nr,nc,n,m):
    return 0<=nr<m and 0<=nc<n

def get_number_of_islands(grid):
    m = len(grid) # rows
    n = len(grid[0]) # cols
    
    ds = island_disjoint_set(m*n)
    # I 
    directions = [[0,1],[1,0],[0,-1],[-1,0]]
    
    # Now I need to connect all nodes
    for r in range(m):
        for c in range(n):
            node_u= get_1d_node(r,c,n)
            if grid[r][c] == "1":
                for dr,dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if is_in_grid(nr,nc,n,m) and grid[nr][nc] == "1":
                        node_v = get_1d_node(nr,nc,n)
                        ds.union(node_u, node_v)


    # Once Union is done lets check how many islands have been creted
    number_of_islands = 0
    for r in range(m):
        for c in range(n): 
            if grid[r][c]=="1":
                node_u = get_1d_node(r,c,n)
                if ds.find(node_u) == node_u:
                    number_of_islands += 1
    return number_of_islands                
                
    
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

# print(get_number_of_islands(grid))

# Output: 3

            
"""Problem 3: Accounts Merge
🧠 Google-style framing:
Imagine you're building a system for Google Contacts where users can save email addresses across multiple accounts. If two accounts share even a single common email, they should be merged into one.
You're given a list of accounts. Each account is a list where:
The first element is the user's name.
The remaining elements are email addresses.

Merge accounts that belong to the same person (i.e., if they share at least one email), and return the merged accounts in the same format:   
[
 ["John", "johnsmith@mail.com", "john00@mail.com"],
 ["John", "johnnybravo@mail.com"],
 ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
 ["Mary", "mary@mail.com"]
]

[
 ["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],
 ["John", "johnnybravo@mail.com"],
 ["Mary", "mary@mail.com"]
]

Approach:
We know a list that starts with name and its emails
the name can appear multiple times
you can merge lists where name is common and at least one email from the list

can these names be different for same email, like john, John , Johnny? No names will be standard only

Since we need to find matching email and merge it or connect it, this can be solved using disjoint sets

We can do something like convert list to indices because i need to connect the list so I need the count.
so create like 
disjoin_set(len(accounts))
since names will be standard I can assign the name as like indices, so that I can merge on basis of indices.

0: ["johnsmith@mail.com", "john00@mail.com"],
1: [ "johnnybravo@mail.com"],
2: ["johnsmith@mail.com", "john_newyork@mail.com"],
3: ["mary@mail.com"]

{"johnsmith@mail.com":0,
"john00@mail.com":0,
 "johnnybravo@mail.com":1,
 "johnsmith@mail.com":2
}

this becomes like adjacency list
0 is connected to ["johnsmith@mail.com", "john00@mail.com"],
2 is connected to ["johnsmith@mail.com", "john_newyork@mail.com"] 


I will iterate for each account and if I find any email which is common I will connect them
So Basically I need to connect email to accounts 


"""

class DisjointSetAccountMerge:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.size = [1 for i in range(n)]
    
    def find(self,x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    
    def union(self,u,v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return False # two accounts are already connected
    
        if self.size[pu] >= self.size[pv]:
            self.parent[pv] = pu
            self.size[pu] += self.size[pv]
        else:
            self.parent[pu] = pv
            self.size[pv] += self.size[pu]
        return True

def merge_accounts(accounts):
    n = len(accounts)
    ds = DisjointSetAccountMerge(n)
    
    email_accounts_dict = {}
    for i in range(n):
        for eml in accounts[i][1:]:
            if eml in email_accounts_dict: 
                # this basically means I have seen this email earlier
                # this means "ind" of this seen email and current "i" are connected lets connect them
                ds.union(email_accounts_dict[eml], i)
            email_accounts_dict[eml] = i
    
    # once I have gone through all emails my accounts merge information is available in disjoint set
    # lets use this information by travelling to all indexes (nodes/names) and find their ultimate parent
    # and append the all emails into the list
    merged_accounts = {}
    for eml,acc_idx in email_accounts_dict.items():
        parent_i = ds.find(acc_idx)
        if parent_i not in merged_accounts:
            merged_accounts[parent_i] = set()
        merged_accounts[parent_i].add(eml)
    
    # once we have merged accounts lets convert them to output format
    result = []
    for accnt, emls in merged_accounts.items():
        name = accounts[accnt][0]
        account_list = [name] + sorted(emls)
        result.append(account_list)
        
    return result


accounts = [
 ["John", "johnsmith@mail.com", "john00@mail.com"],
 ["John", "johnnybravo@mail.com"],
 ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
 ["Mary", "mary@mail.com"]
]


# print(merge_accounts(accounts))
    
    
"""
Google Scenario Framing:
You're working on a network reliability system for Google's internal infrastructure. The system represents a collection of n microservices.
Some microservices communicate directly with each other, and this communication is bidirectional.

Your task is to write a utility that, given a list of n microservices and a set of communication links between them, 
determines how many isolated groups of microservices exist.
In other words, how many disconnected subnetworks or connected components are present in the system?

Input:
n (number of microservices): int

edges (list of bidirectional links): List[List[int]]

Input:
n = 5
edges = [[0, 1], [1, 2], [3, 4]]

Output:
2

"""

class DisjoinSetNetworkSystem:
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
            return # already connected there is no need to check

        if self.size[pu] >= self.size[pv]:
            self.parent[pv] = pu
            self.size[pu] += self.size[pv]
            
        else:
            self.parent[pu] = pv
            self.size[pv] += self.size[pu]
        return
        
        
def get_connected_networks(n,edges):
    ds = DisjoinSetNetworkSystem(n)
    
    for u,v in edges:
        ds.union(u,v)
    
    connected_networks = 0
    for i in range(n):
        if ds.find(i)==i:
            connected_networks += 1
    return connected_networks
    
n = 8
edges = [[0, 1], [1, 2], [3, 4],[4,5],[6,7]]     
        
# print(get_connected_networks(n,edges)) 

"""

You're building a social network backend. 
Each user can send a friend request to another. Once two users become friends, their circles (connected components) merge.

But there's a twist.

🚫 Some users must not be in the same friend circle. These are called enemy pairs.
🧩 Problem Statement
You are given:

n users labeled 0 to n - 1

A list of friend requests friend_requests, where each request is a pair [u, v]
A list of enemy pairs restrictions, where each restriction is a pair [x, y] — meaning x and y cannot be in the same friend circle
You must:

Process each friend request in order
Return an array of booleans: for each request, return True if the request can be accepted, or 
False if it violates a restriction (either directly or through the union)
Example:

n = 5
friend_requests = [[0,1], [1,2], [2,3], [0,4]]
restrictions = [[0,3], [2,4]]
Output: [True, True, False, False]
"""

class DisjointSetFrndConnRest:
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
            return False # nodes are connected
        
        if self.size[pu] >= self.size[pv]:
            self.parent[pv] = pu
            self.size[pu] += self.size[pv]
        
        else:
            self.parent[pu] = pv
            self.size[pv] += self.size[pu]
        return True

def friend_request_with_restriction(n,friend_requests,restriction):
    ds = DisjointSetFrndConnRest(n)
    result = []
    
    for u, v in friend_requests:
        pu = ds.find(u)
        pv = ds.find(v)
        
        # Check if accepting this request would violate any restrictions
        valid = True
        for a, b in restrictions:
            pa = ds.find(a)
            pb = ds.find(b)
            # If u and v are merged, check if any restricted pair would end up in the same set
            if (pu == pa and pv == pb) or (pu == pb and pv == pa):
                valid = False
                break
        
        if valid:
            ds.union(u, v)  # Accept the friend request
            result.append(True)
        else:
            result.append(False)

    return result

n = 5
friend_requests = [[0,1],[1,2],[2,3],[0,4]]
restrictions = [[0,3],[2,4]]

print(friend_request_with_restriction(n, friend_requests, restrictions))
# [True, True, False, False]
# Output: [True, True, False, False]


"""
Problem: Earliest Moment When Everyone Becomes Friends
📘 Scenario:
You're working on a social platform where users send friend requests over time. 
Each friend request connects two users. Your task is to determine the earliest timestamp at which all users are connected — meaning 
everyone is either directly or indirectly friends with everyone else.

🧾 Problem Statement:
You are given:
An integer n — total number of people labeled 0 to n-1.
A list logs, where each entry is [timestamp, user_a, user_b].
Each log represents a friendship request made at timestamp, connecting user_a and user_b.
Goal: Return the earliest timestamp at which all the n users become connected.
If it's never possible, return -1.
"""

class DisjointSetEarliestTimestampFriends:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.size = [1 for _ in range(n)]
        self.components = n
    
    def find(self,x):
        if self.parent[x]!=x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self,u,v):
        pu = self.find(u)
        pv = self.find(v)
        
        if pu == pv:
            return False # componets are already connected
    
        if self.size[pu] >= self.size[pv]:
            self.parent[pv] = pu
            self.size[pu] += self.size[pv]
        else:
            self.parent[pu] = pv
            self.size[pv] += self.size[pu]
        
        # if we are mergin two comoponets basicaly we are reduing the count of 
        # individual components
        self.components -= 1
        return True
    
    
def earliest_time_for_friends(logs,n):
    ds = DisjointSetEarliestTimestampFriends(n)
    logs.sort(key=lambda x:x[0])
    
    for time_stamp, u,v in logs:
        if ds.union(u,v):
            if ds.components == 1:
                return time_stamp
    return -1
            

logs = [
    [20190101, 0, 1],
    [20190104, 3, 4],
    [20190107, 2, 3],
    [20190211, 1, 3],
    [20190224, 2, 4]
]
n = 5

print(earliest_time_for_friends(logs, n)) 


"""
Number of islands II:
You are given an empty 2D binary grid grid of size m x n. The grid represents a map where 0's represent water and 1's represent land. 
Initially, all the cells of grid are water cells (i.e., all the cells are 0's).
We may perform an add land operation which turns the water at position into a land. 
You are given an array positions where positions[i] = [ri, ci] is the position (ri, ci) at which we should operate the ith operation.
Return an array of integers answer where answer[i] is the number of islands after turning the cell (ri, ci) into a land.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
Input: m = 3, n = 3, positions = [[0,0],[0,1],[1,2],[2,1]]
Output: [1,1,2,3]
Explanation:
Initially, the 2d grid is filled with water.
- Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land. We have 1 island.
- Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land. We still have 1 island.
- Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land. We have 2 islands.
- Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land. We have 3 islands.
Example 2:

Input: m = 1, n = 1, positions = [[0,0]]
Output: [1]


"""
class disjoint_set:
    def __init__(self,grid_size):
        self.parent = [i for i in range(grid_size)]
        self.size = [1 for _ in range(grid_size)]

    def find(   self,x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self,u,v):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return False #  belong to same island no need to increase the islands

        if self.size[pu] >= self.size[pv]:
            self.parent[pv] = pu
            self.size[pu] += self.size[pv]
        else:
            self.parent[pu] = pv
            self.size[pv] += self.size[pu]
        
        return True # merging completed # successfully merged → one less island

class Solution:

    def get_1d_node(self,r,c,n):
        return r*n +c
    
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        grid= [[0 for _ in range(n)] for _ in range(m)]
        ds = disjoint_set(m*n)
        count = 0
        number_of_islands = []
        directions = [[0,1],[1,0],[0,-1],[-1,0]]

        for r,c in positions:
            if grid[r][c]==1:
                number_of_islands.append(count)
                continue
            else:
                grid[r][c] = 1
            
            count += 1
            node_u = self.get_1d_node(r,c,n)

            for dr, dc in directions:
                nr = dr + r
                nc = dc + c
                if 0<=nr<m and 0<=nc<n and grid[nr][nc]==1:
                    node_v = self.get_1d_node(nr,nc,n)
                    merged = ds.union(node_u,node_v)

                    if merged: # merging was done 
                        count -= 1
            
            number_of_islands.append(count)
        return number_of_islands



"""
Next Google-Type Problem: Evaluate Division
🧠 (Leetcode 399)
📌 Why Google likes this:
Graph traversal with mapping.
Reasoning over transitive relations (like currency conversion, units, knowledge graphs).
Often used to test DFS/BFS, hash maps, and data modeling skills.

You are given an array of variable pairs equations and an array of real numbers values,
where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.
You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.
Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.
Note: The variables that do not occur in the list of equations are undefined, so the answer cannot be determined for them.

Example 1:
Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]

Explanation: 
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? 
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
note: x is undefined => -1.0
"""
from collections import defaultdict, deque

def evaluate_division(equations,values,queries):
    graph = defaultdict(list)
    
    for ind,(u,v) in enumerate(equations):
        graph[u].append((v,values[ind]))
        graph[v].append((u,1/values[ind]))
    
    
    def bfs(num,den):
        q = deque([(num,1)])
        visited = set()
        visited.add(num)
        
        while q:
            node,eval = q.popleft()
            if node == den:
                return eval
            for nbr,val in graph[node]:
                if nbr not in visited:
                    visited.add(nbr)
                    q.append((nbr, eval*val))
        return -1
    
    def dfs(node,target,visited,acc_product):
        if node == target:
            return acc_product
        visited.add(node)
        for nbr, nbr_val in graph[node]:
            if nbr not in visited:
                result = dfs(nbr,target,visited,acc_product*nbr_val)
                if result != -1:
                    return result
        return -1
    
    evaluations = []
    for num,den in queries:
        if num not in graph or den not in graph:
            evaluations.append(-1)
            continue
            
        # ans = bfs(num,den)
        
        ## DFS
        visited = set()
        ans = dfs(num,den,visited,1)
        
        evaluations.append(ans)
    
    return evaluations

# Input:
equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]

# Output:
# [6.0,0.5,-1.0,1.0,-1.0]

print(evaluate_division(equations,values,queries))

