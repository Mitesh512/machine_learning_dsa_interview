class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
"""
Some Quick Notes:
BFS is better for shortest path unweighted graphs.
DFS is better for components, cycles detection, etc.
"""

# BFS 
from collections import deque
def bfs_traversal(root):
    traversal = []
    if root is None:
        return traversal
    
    q = deque([root])
    
    while len(q):
        node = q.popleft()
        traversal.append(node.val)
        
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    
    return traversal


## Recursive Technique
def dfs_traversal(root):
    if root is None:
        return []
    pre_order = []# root, left, right
    in_order = []
    post_order = []
    
    def pre_dfs(node,traversal):
        if node:
            traversal.append(node.val)
            pre_dfs(node.left,traversal)
            pre_dfs(node.right,traversal)
        return traversal
    
    def in_dfs(node,traversal):
        if node:
            in_dfs(node.left,traversal)
            traversal.append(node.val)
            in_dfs(node.right,traversal)
        return traversal
    
    def post_dfs(node,traversal):
        if node:
            post_dfs(node.left,traversal)
            post_dfs(node.right,traversal)
            traversal.append(node.val)
        return traversal
    
    pre_order = pre_dfs(root,pre_order)
    in_order = in_dfs(root,in_order)
    post_order = post_dfs(root,post_order)
    
    return pre_order,in_order, post_order            


## Iterative Technique
def itertaive_dfs(root):
    if root is None:
        return []
    ## preorder iterative dfs root left right
    # root --> left --> right
    pre_traversal = []
    node = root
    pre_stack = [node]
    
    while pre_stack:
        node = pre_stack.pop()
        pre_traversal.append(node.val)
        # first go to right and put it in stack, because we want to access left first so it should
        # be on top
        if node.right:
            pre_stack.append(node.right)
        # put left in the end because we want it on top
        if node.left:
            pre_stack.append(node.left)
        
    ## inorder iterative dfs left , root, right
    inorder_traversal = []
    inorder_stack = []
    node = root
    while node or inorder_stack:
        while node:
            inorder_stack.append(node)
            node = node.left
        node = inorder_stack.pop()
        inorder_traversal.append(node.val)
        if node.right:
            node = node.right
    
    ## post order iterative traversal left right root
    ## This is a bit tricky fist we will traverse it in reverse order
    # so the reverse order will be root right left (slightly different from preorder)
    node = root
    post_traversal = []
    post_stack = [node]
    while post_stack:
        node = post_stack.pop()
        post_traversal.append(node.val)
        # root right left
        # we alredy have taken root, now remaining are right and left
        # what we need is right first and then left
        # so in stack lets put left first and then right (so last will be right, Last in first Out)
        if node.left:
            post_stack.append(node.left)
        if node.right:
            post_stack.append(node.right)
    post_traversal = post_traversal[::-1]
    return pre_traversal,inorder_traversal,post_traversal
        
"""
Problems on path:
| Concept                          | Definition                                                                          |
| -------------------------------- | ----------------------------------------------------------------------------------- |
| **Height of a node**             | Number of edges on the longest path from the node **down to a leaf**.               |
| **Depth of a node**              | Number of edges from the **root to the node**.                                      |
| **Distance between two nodes**   | Number of edges in the shortest path connecting the two nodes.                      |
| **Diameter of a tree**           | Longest path (in terms of number of edges) **between any two nodes** in the tree.   |
| **Max path sum**                 | Path that yields the **maximum sum** of node values. Can start and end at any node. |
| **Root-to-leaf path sum**        | Path from root to any leaf that sums to a **target** value.                         |
| **All root-to-leaf paths**       | All valid paths from root to leaves (used for decision tracking, backtracking).     |
| **Lowest Common Ancestor (LCA)** | The **lowest** node in the tree that has both nodes as descendants.                 |
"""

from collections import deque
def height_of_bt(root):
    """
    Can you walk me through the algorithm line-by-line, maybe with a quick example?
    What would be the edge case when the tree has only one node or is empty?
    What if the tree is very deep but has very few nodes per level — does BFS still help us in terms of space?
        - in DFS also we would still have to iterate to each node, only thing is that there is no q so that can be optimized
    Would you consider DFS (recursive) as an alternative here? Why or why not?
        - Yes I should consider DFS recursive way , where I will iterate and as I go down I increment and then while backtracking substract it
        - keep a variable to store max depth
    please help me write the dfs solution, I think TC will be O(n) in both cases only space will be optimized in dfs, but it will also have a recursive stack.
    let me know what do you think.
    DFS is often preferred when you're dealing with tree depth/height questions due to simpler code and no need for a queue
    """
    if root is None: # edge case
        return -1
    q= deque([root])
    height = -1
    while q:
        height += 1 # 1 node edge case addressed
        for _ in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    return height
    
def height_of_bt_dfs(root):
    if root is None:
        return -1
    left_height = height_of_bt_dfs(root.left)
    right_height = height_of_bt_dfs(root.right)
    return 1 + max(left_height, right_height)


## Depth of a Node:

def depth_of_a_node(root,target_node):
    """
    Depth of a node: Number of edges from the **root to the node
    """
    ### DFS solution
    # def find_depth(root,target,depth=0):
    #     if root == target:
    #         return depth
    #     if root is None:
    #         return -1
    #     # check in left
    #     left = find_depth(root.left,target,depth + 1)
    #     if left != -1:
    #         return left
    #     # check in right:
    #     right = find_depth(root.right,target,depth+1)
    #     if right != -1:
    #         return right
    # return find_depth(root,target_node,0)

    ### BFS Solution
    if root is None:
        return -1
    
    q = deque([root, 0]) # keep node and depth in the queue
    
    while q:
        node,depth = q.popleft()
        if node == target_node: # in case you have value node.val = target_val
            return depth 
        if node.left:
            q.append([node.left,depth+1])
        if node.right:
            q.append([node.right,depth+1])
    
    return -1 # not found


### Distannce between two nodes:
# Distance between two nodes: Number of edges in the shortest path connecting the two nodes
def distnace_between_two_nodes(root,node1,node2):
    """
    Assuming there will always exist two nodes in tree,if not please confirm
    Find the Lowest Common Ancestor (LCA) of the two nodes.
    Find the depth of each node from that LCA.
    Add both distances.
    """
    def get_lca(root,p,q):
        # TC O(n), SC: O(n)
        if root is None or root==p or root==q:
            return root
        left = get_lca(root.left,p,q)
        right = get_lca(root.right,p,q)
        
        if left and right:
            return root
        if left:
            return left
        else:
            return right
    
    def find_depth(root,target,depth):
        # TC O(n), SC: O(h)
        # ### DFS approach
        # if root is None:
        #     return -1
        # if root.val == target:
        #     return depth
        # left = find_depth(root.left,target,depth+1)
        # if left != -1:
        #     return left
        
        # right = find_depth(root.right,target,depth+1)
        # if right != -1:
        #     return right
        # return -1

        ### BFS approach
        if root.val ==target:
            return 0
        q = deque([root,0])
        
        while q:
            node,depth = q.popleft()
            if node.val == target:
                return depth
            if node.left:
                q.append([node.left,depth+1])
            if node.right:
                q.append([node.right,depth+1])
        return -1
            
    lca_node = get_lca(root,node1,node2)
    depth_node1 = find_depth(lca_node,node1.val,0)
    depth_node2 = find_depth(lca_node,node2.val,0)
    return depth_node1 + depth_node2
    
    
#Max path sum: Path that yields the **maximum sum** of node values. Can start and end at any node.    
def get_max_path_sum(root):
    """
    Time: O(n) — every node visited once.
    Space O(h) - height of tree due to recursion stack.
    """
    def get_max_sum(root,max_sum):
        if root is None:
            return 0, max_sum
        left,max_sum = get_max_sum(root.left,max_sum)
        right,max_sum = get_max_sum(root.right,max_sum)
        # left and right can be negative as well, i don't want my root to include -ve value path
        left = max(left,0)
        right = max(right,0)
        curr_path_sum = root.val + left + right
        max_sum = max(max_sum, curr_path_sum)
        return root.val + max(left,right) , max_sum

    _,max_sum =  get_max_sum(root,max_sum= float("-inf"))
    return max_sum

### In case we need to pring the max_sum path as well
def get_max_path_with_path(root):
    def helper(node):
        if not node:
            # gain, path, max_sum, max_path
            return 0, [], float('-inf'), []

        left_gain, left_path, left_max_sum, left_max_path = helper(node.left)
        right_gain, right_path, right_max_sum, right_max_path = helper(node.right)

        # Max contribution if this node is part of a path going upwards
        gain_through_node = node.val + max(0, left_gain, right_gain)
        path_through_node = [node.val] + (left_path if left_gain > right_gain else right_path if max(left_gain, right_gain) > 0 else [])

        # Max path that passes through this node (can go left + root + right)
        total_path_sum = node.val + max(0, left_gain) + max(0, right_gain)
        total_path_nodes = (left_path if left_gain > 0 else []) + [node.val] + (right_path if right_gain > 0 else [])

        # Now, compare all possible max path sums:
        max_sum = max(left_max_sum, right_max_sum, total_path_sum)
        max_path = total_path_nodes
        if max_sum == left_max_sum:
            max_path = left_max_path
        elif max_sum == right_max_sum:
            max_path = right_max_path

        return gain_through_node, path_through_node, max_sum, max_path
    _, _, max_sum, max_path = helper(root)
    return max_sum, max_path

### Diameter of Binary tree

def diameterOfBinaryTree( root):
    """

    We basically need to go the the depth 
    use any dfs traversal like inorder, preorder, postorder
    
    have two variable path and max_path
    while backtracking reduce the path len
    """
    max_path_len = 0
    def dfs(root,path_len):
        if root is None:
            return 0
        right = dfs(root.right, path_len)
        left = dfs(root.left, path_len)
        path_len = left + right
        max_path_len = max(max_path_len, path_len)
        return max(left, right) + 1
    path_len = 0
    dfs(root, path_len)
    
    return max_path_len


"""
BST Validation
Check if a given binary tree is a valid Binary Search Tree (BST).

A BST must satisfy:
    - All nodes in the left subtree < root
    - All nodes in the right subtree > root
    - This must hold for every node recursively
"""

def is_valid_bst(root):
    """
    Time: O(n) — visit each node once
    Space: O(h) — height of the tree (recursion stack)
    """
    if root is None:
        return True

    max_val = float("inf")
    min_val = float("-inf")
    
    def is_valid(root,min_val,max_val):
        if root is None:
            return True
        # what we want to for a tree to be valid min_val < root.val < max_val
        if min_val > root.val or root.val > max_val:
            return False
        
        left = is_valid(root.left,min_val,root.val)
        right = is_valid(root.right, root.val, max_val)
        
        return left and right
    
    return is_valid(root,min_val,max_val)
    
"""
2. Insertion into a BST
Insert a value into the BST, maintaining BST properties
"""

def insert_node_in_bst(root,val):
    """
    We can insert the node always at the leaf node.
    because no matter what the value is we will be able to find its position 
    at any of the leaf node
    Best/Average: O(log n) for balanced BST
    Worst: O(n) for skewed BST
    """
    if root is None:
        return TreeNode(val)
    
    if val < root.val:
        root.left = insert_node_in_bst(root.left,val)
    else:
        root.right = insert_node_in_bst(root.right,val)
    return root
        
        
### Deletion in BST:
# Delete a value from BST and preserve its properties.

def delete_node_from_bst(root,val):
    """
    3 Deletion Cases:
    Leaf node — remove it directly.
    1 child — replace the node with its child.
    2 children — replace with inorder successor (smallest value in right subtree) or inorder predecessor.
    """
    def get_min_val_from_tree(right_tree):
        while right_tree.left:
            right_tree = right_tree.left
            min_val = right_tree.val
        return min_val
            
    
    
    if root is None:
        return None
    
    # first we need to find the node to delete it
    # check the node in left if val is less then root
    if val < root.val:
        # we are just shortening our serach space now there is no need to go to right
        root.left = delete_node_from_bst(root.left,val)
    elif val > root.val:
        root.right = delete_node_from_bst(root.right,val)
    else:
        # We have found the Node, now there can be 3 cases:
        # there is nothing in left
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        
        # Now there is a node with two childer we can find the right min and update tree
        # right_min_val = get_min_val_from_tree(root.right)
        # right_min_node = TreeNode(right_min_val)
        # right_min_node.left = root.left
        # right_min_node.right = root.right
        # delete_node_from_bst(right_min_node,val)
        # return right_min_node
        min_val = get_min_val_from_tree(root.right)
        root.val = min_val
        root.right = delete_node_from_bst(root.right, min_val)
        
### Delete nodes and create a Forest
class Solution:
    # post order traversal
    def delNodes(self, root, to_delete):
        to_delete_set = set(to_delete)
        forest = []
        def dfs(root):
            if root is None:
                return None
            root.left = dfs(root.left)
            root.right = dfs(root.right)

            if root.val in to_delete_set:
                # if leaft node there is no need add any thing to forext
                if root.left is None and root.right is None:
                    return None
                
                if root.left:
                    forest.append(root.left)
                if root.right:
                    forest.append(root.right)
                return None
            return root
        root = dfs(root)
        if root is not None:
            forest.append(root)
        return forest
        
#### All nodes at distance K


from collections import defaultdict, deque
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # we can create a graph from Tree
        graph = defaultdict(list)

        def create_graph(root):
            if root is None:
                return
            
            if root.left:
                graph[root.val].append(root.left.val)
                graph[root.left.val].append(root.val)
                create_graph(root.left)
            if root.right:
                graph[root.val].append(root.right.val)
                graph[root.right.val].append(root.val)
                create_graph(root.right)
        
        create_graph(root)

        q = deque([target.val])
        visited = set([target.val])
        level = 0
        ans = []
        while q:
            if level == k:
                break
            for _ in range(len(q)):
                node = q.popleft()
                for nbr in graph[node]:
                    if nbr not in visited:
                        q.append((nbr))
                        visited.add(nbr)
            level += 1
        
        while q:
            node= q.popleft()
            ans.append(node)
        
        return ans
            
            
# k-th smallest/largest in BST?
        

### Construct Tree form PreOrder and Inorder


    
    