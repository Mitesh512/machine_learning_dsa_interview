from typing import List, Tuple
"""
What Is Backtracking?
Backtracking is a refined form of recursion where you:
Make a choice → Explore → Undo the choice → Try next option

It's perfect for solving problems where:
    You need to explore all combinations/paths.
    There are constraints, and you prune invalid paths early.
    Examples include: permutations, combinations, N-Queens, Sudoku, Word Search.
    
    
def backtrack(state, choices):
    if goal_reached(state):
        save_solution(state)
        return

    for choice in choices:
        if is_valid(choice, state):
            make_choice(state, choice)
            backtrack(state, choices)
            undo_choice(state, choice)  # <--- backtrack
            
Let's Translate to an Example
Let's revisit your permutation example and apply in-place backtracking logic.
"""

"""
Google Interview Scenario
You're working on an internal tagging engine at Google that assigns different combinations of expertise tags 
(like "ml", "ai", "cv") to user profiles for recommendation systems.
To test all configurations, your task is to generate all unique orderings of the tags provided.
You are not allowed to use additional memory like slicing or creating new arrays in each recursive call.
Implement this using in-place backtracking.
"""

def get_all_permutations(nums):
    # TC: O(n* n!), SC: O(n* n!)
    """
    Permutations (Backtracking Approach)
    We try all numbers at each position by swapping elements in place, 
    and we undo the swap (backtrack) after exploring.
    """
    all_permutations = []
    n = len(nums)
    def backtrack(start):
        if start==n:
            all_permutations.append(nums.copy())
            return
        for i in range(start,n):
            nums[start], nums[i] = nums[i], nums[start]  # Make choice
            backtrack(start + 1)
            nums[start], nums[i] = nums[i], nums[start]  # Undo choice
    backtrack(0)
    return all_permutations

# print(get_all_permutations([1,2,3]))

"""
Scenario:

Imagine tags could repeat (e.g., ['ai', 'ai', 'ml']).
You now need to generate only unique permutations (no duplicates in output).

This is the classic "permutations with duplicates" variant. 
"""

# def get_unique_permutation(arr):
    # n = len(arr)
    # all_permutations = set()
    
    # def backtrack(start):
    #     if start == n:
    #         all_permutations.add(tuple(arr.copy()))
    #         return 

    #     for i in range(start,n):
    #         # select the ith element as the start and get the permutation
    #         arr[start],arr[i] = arr[i],arr[start]
    #         backtrack(start+1)
    #         # after performing the operation put it back
    #         arr[start],arr[i] = arr[i],arr[start]
    
    # backtrack(0)
    # return [list(permut) for permut in all_permutations]

def get_unique_permutation(arr):
    arr.sort()
    n = len(arr)
    all_permutations = []
    def backtrack(start):
        if start == n:
            all_permutations.append(arr.copy())
            return 
        for i in range(start,n):
            if i!= start and arr[i]==arr[start]:
                continue
            # select the ith element as the start and get the permutation
            arr[start],arr[i] = arr[i],arr[start]
            backtrack(start+1)
            # after performing the operation put it back
            arr[start],arr[i] = arr[i],arr[start]
    backtrack(0)
    return  all_permutations

# print(get_unique_permutation([1,2,3,2]))

            
"""
Scenario-Based Question 
📌 Problem:
Your product team wants to auto-generate bundles of features to offer in different product tiers (e.g. free, pro, enterprise).
You're given a list of feature tags. You need to return all unique combinations of features of exactly k size to help them build bundles.
Input: tags = ['ai', 'ml', 'cv', 'nlp'], k = 2  
Output: [
  ['ai', 'ml'], ['ai', 'cv'], ['ai', 'nlp'],
  ['ml', 'cv'], ['ml', 'nlp'],
  ['cv', 'nlp']]
  
Now in this case to me order doesn't matter and I just need two cases
['ai', 'ml', 'cv', 'nlp']
at each step I have an option either to select or not

"""
def get_all_combinations_of_size_k(tags,k):
    n = len(tags)
    all_combination_of_size_k =[]
    def backtrack(ind,comb):
        if len(comb)==k:
            all_combination_of_size_k.append(comb.copy())
            return
        if ind ==n:
            return
        # take 
        comb.append(tags[ind])
        backtrack(ind+1,comb)
        
        comb.pop()
        # not take
        backtrack(ind+1,comb)
    backtrack(0,[])
    return all_combination_of_size_k

# print(get_all_combinations_of_size_k(['ai', 'ml', 'cv', 'nlp'],2))
            
            
        
    

"""
Google Interview Scenario:
"You're working on a feature that helps users allocate resources. 
Given a list of task weights, you need to find whether 
it's possible to select a subset of tasks such that their total weight exactly 
equals a given capacity."

📥 Input:
tasks = [3, 4, 5, 2]

target_sum = 9

📤 Output:
True (because 4 + 5 = 9, or 3 + 4 + 2 = 9)
"""

def allocate_resources_for_given_exact_capacity(tasks,target_sum):
    """
    Assuming no negative values in tasks
    Recursive solution has TC O(2^n)
    SC stack==> SC O(2^n)
    
    Memoized solution has TC O(n* target_sum)
    SC O(n*target_sum)
    """
    n = len(tasks)
    
    def is_allocation_possible(ind, curr_sum):
        if curr_sum == target_sum:
            return True
        if ind==n:
            return False
        
        # take case
        take = is_allocation_possible(ind+1, curr_sum + tasks[ind])
        # not take case
        not_take = is_allocation_possible(ind+1, curr_sum)
        return take or not_take
    ans =  is_allocation_possible(0, 0)

    return ans

print(allocate_resources_for_given_exact_capacity([3, 4, 5, 2],9))

"""

Google Cloud Resource Allocation
You're working as a systems engineer on Google Cloud Platform. 
A client has a daily resource budget (in units of compute time). 
They provide you with a list of tasks, each task consuming a fixed amount of compute units.

Your task is to determine if it's possible to allocate some subset of these tasks such 
that the total compute usage exactly matches the client's budget.

If yes, return one such subset of tasks that meets the exact requirement. 
If not, return an empty list or None.

📘 Problem Statement (Formalized)
Given a list of tasks, where each task is represented by its compute cost (a positive integer), 
and a target_budget (positive integer), 
return any one subset of tasks that sum exactly to the target.

If no such subset exists, return None.
tasks = [3, 4, 5, 2]
target_budget = 9
[4, 5] or [3, 2, 4] or any other valid combination that sums to 9.

tasks = [2, 5, 7]
target_budget = 4
Output: None 
"""

def find_a_subset_sum_equals_target(tasks,target):
    """
    I need to find a subset whose sum is target
    
    for each task I will have two options
    [3, 4, 5, 2]
    
    take the taks or not take it
    """
    
    n = len(tasks)
    ans = []
    
    def backtrack(ind,target,subset):
        if len(ans) > 0:
            return
        if target ==0:
            ans.append(subset.copy())
            return
            
        if ind ==n:
            return
        if target < 0:
            return
        # take
        backtrack(ind+1,target - tasks[ind],subset + [tasks[ind]])
        # not take
        backtrack(ind+1,target,subset)
    
    backtrack(0,target, [])
    return ans

print(find_a_subset_sum_equals_target([3, 4, 5,0, 2],9))

    
    
        

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        What are the possibilities of putting a queen
        in a row I can put only one but it can be at any column
        once I have chosen 1 column it will become unavailable in next row,
        I have to check same in case of diagonals as well

        for diagonal top left to bottom right (r-c) remains constant
        for diagonal bottom left to top right (r+c) remains constant
        """

        columns = set()
        diag_tl_br = set() # (r-c) is constant
        diag_bl_tr = set() # (r+c) is constant
        board = [["." for _ in range(n)] for _ in range(n)]

        result = []

        def backtrack(row):
            # nonlocal result
            if row == n:
                # base case we have found a solution
                possible_queen_position = ["".join(board[i])  for i in range(n) ]
                result.append(possible_queen_position)
                return
            # in the given row I will have n options (columns ) to put my queen in
            for col in range(n):
                if (col not in columns) and ((row-col) not in diag_tl_br) and ((row+col) not in diag_bl_tr) :
                    columns.add(col)
                    diag_tl_br.add(row-col)
                    diag_bl_tr.add(row+col)
                    board[row][col] = "Q"
                    
                    backtrack(row+1)

                    columns.remove(col)
                    diag_tl_br.remove(row-col)
                    diag_bl_tr.remove(row+col)
                    board[row][col] = "."
        
        backtrack(0)

        return result





        