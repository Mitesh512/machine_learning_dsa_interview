
def sum_of_n(n):
    # TC O(n), SC O(n)
    if n == 1:
        return 1
    return n + sum_of_n(n-1)

# print(sum_of_n(5))
# 4 + 3 +2 +1

def fibbonacci(n):
    # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34,
    # TC O(2^N), SC: O(n)
    if n ==0:
        return 0
    if n == 1:
        return 1
    return fibbonacci(n-1) + fibbonacci(n-2)

# print(fibbonacci(4))

def count_down(n):
    # TC O(n) , SC: O(n)
    if n == 0:
        return 
    print(n)
    count_down(n-1)

# print(count_down(5))


def count_up(n):
     # TC O(n) , SC: O(n)
    if n==0:
        return
    count_up(n-1)
    print(n)

# print(count_up(5))


def print_evens(n):
    # TC O(n) , SC: O(n)
    if n == 0:
        return 
    if n % 2 ==0:
        print(n)
    print_evens(n-1)

        
# print(print_evens(6))


def print_first_n_evens(n):
     # TC O(n) , SC: O(n)
    if n == 0:
        return

    print_first_n_evens(n-1)
    print(2*n)
    
# print_first_n_evens(5)


def reverse_string(s):
    # TC O(n) , SC: O(n)
    n = len(s) -1
    
    def rec(s,i):
        if i==0:
            return s[i]
        return s[i] + rec(s,i-1) 
    
    reverse_str = rec(s,n)
    print(reverse_str)


# reverse_string("asdfg")



def is_sorted(arr):
    # TC O(n) , SC: O(n)
    # increasing order
    if len(arr) == 1:
        return True
    n = len(arr)
    
    def rec(i):
        if i == n-1:
            return True

        if arr[i]<= arr[i+1]:
            return rec(i+1)
        else:
            return False
            
    return rec(0)

# print(is_sorted([1,2,2,3,4,5]))
    
    

def is_palindrome(s):
    # TC O(n) , SC: O(n)
    l = 0
    r= len(s)-1
    def rec(l,r):
        if l >r:
            return True
        if s[l] == s[r]:
            return rec(l+1,r-1)
        else:
            return False
    return rec(l,r)

# print(is_palindrome("racecar"))
# print(is_palindrome("hello"))


def find_first_index(arr,target):
    # TC O(n) , SC: O(n)
    n = len(arr)
    
    def rec(i,target):
        if i == n:
            return -1
        if arr[i] == target:
            return i
        else:
            return rec(i+1,target)
    
    return  rec(0,target)

# print(find_first_index([1,4,5,4,5],5))
# print(find_first_index([1,4,3,4,5],6))


def find_all_indices(arr,target):
    # TC O(n) , SC: O(n)
    n = len(arr)
    def rec(i):
        # base case
        if i == n:
            return []
        ans = rec(i+1)
        if arr[i] == target:
            return [i] + ans
        else:
            return ans
    ans = rec(0)
    return ans


# print(find_all_indices([1,2,3,2,3,4,2,2],2))



def find_all_indices_reversed(arr,target):
    # TC O(n) , SC: O(n)
    n = len(arr)
    def rec(i):
        # base case
        if i == n:
            return []
        ans = rec(i+1)
        if arr[i] == target:
            return ans + [i]
        else: return ans
    ans = rec(0)
    return ans

# print(find_all_indices_reversed([1,2,3,2,3,4,2,2],2))
    
    
def generate_all_subset(arr):
    
    """
    Input: [1,2,3]
    Output: [[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]]
    # TC O(2^n) , SC: O(2^n)
    """
    n = len(arr)
    power_set = []
    def rec(i,res):
        # base case
        if i == n:
            power_set.append(res[:])
            return
        # take case
        res.append(arr[i])
        rec(i+1, res) # [1]
        res.pop() 
        # not take 
        rec(i+1,res) # []
        
    rec(0,[])
    return power_set
        
# print(generate_all_subset([1,2,3]))
        
        
        
def generate_permutaions(arr):
    # TC O(n!) , SC: O(n!)
    """
    permutations of an array are all possible arrangements of the elements in the array.
    For example, the permutations of [1,2,3] are:
    permutations of [1,2,3] = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    Pseudo code:
    1. Start with an empty path and available array as the input array.
    2. If the path length equals the input array length, add the path to the result.
    3. Iterate through the available array and for each element, 
        make a recursive call with the updated path and available array.
    """
    n = len(arr)
    permutations = []
    def rec(path,available_arr):
        if len(path) ==n:
            permutations.append(path.copy())
            return
        for i in range(len(available_arr)):
            rec(path+ [available_arr[i]],available_arr[:i] + available_arr[i+1:])
        
    rec([],arr)
    return permutations
        
    
# print(generate_permutaions([1,2,3]))

def generate_permuttions_with_r(arr,r):
    # TC O(n!/(n-r)!) , SC: O(n!/(n-r)!)
    n = len(arr)
    permutations = []
    def rec(path,available_arr,r):
        if len(path) == r:
            permutations.append(path.copy())
            return
        for i in range(len(available_arr)):
            rec(path+ [available_arr[i]],available_arr[:i] + available_arr[i+1:],r)
        
    rec([],arr,r)
    return permutations

# print(generate_permuttions_with_r([1,2,3],3))

def sum_of_all_subsets(arr):
    # TC O(2^n) , SC: O(2^n)
    res = []
    n = len(arr)
    def rec(i,curr_sum):
        if i == n:
            res.append(curr_sum)
            return
        rec(i+1,curr_sum)
        rec(i+1,arr[i]+ curr_sum)
    rec(0,0 )
    return res
        
# print(sum_of_all_subsets([1,2,3]))


def generate_subsets_without_duplicate(arr):
    # TC O(2^n) , SC: O(2^n)'
    # arr.sort()
    # n = len(arr)
    # subsets = set()
    
    # def rec(i,subset):
    #     if i == n:
    #         subsets.add(tuple(subset))
    #         return
    #     rec(i+1,subset)
    #     rec(i+1,subset+ [arr[i]] )
    
    # rec(0,[])
    # return [list(subset) for subset in subsets]
    arr.sort()
    res = []
    def backtrack(start, path):
        # print(f"At index {start}, path = {path}")
        res.append(path.copy())
        for i in range(start, len(arr)):
            # Skip duplicates
            if i > start and arr[i] == arr[i - 1]:
                # print(f"  Skipping {arr[i]} = {arr[i-1]} due to duplication")
                continue
            path.append(arr[i])
            # print(f"  --> Recursing with path: {path}")
            backtrack(i + 1, path)
            path.pop()
            # print(f"  <-- Backtracked to path: {path}")

    backtrack(0, [])
    return res
# print(generate_subsets_without_duplicate([1,2,2]))
    
"""
Recursive Thinking
🔍 Scenario (Google-style framing):
You're working on a team building an analytics dashboard that processes customer engagement data.
One of the features is to calculate the total number of likes a campaign received over N days.

However, due to system constraints, the team wants to simulate this using recursive data access,
where each days likes are pulled individually and added recursively (i.e., no loops allowed).
Given an integer n, return the sum of the first n natural numbers using recursion.
n >= 0
Assume n fits in a 32-bit integer.
No use of loops or built-in summation functions.
Input: n = 5  
Output: 15   # 1 + 2 + 3 + 4 + 5
"""
def get_likes(n):
    def rec(ind):
        if ind > n:
            return 0
        return ind + rec(ind+1)
    return rec(1)
    
"""
Follow-Up to Previous Problem (with Example)
“Suppose now your analytics dashboard tracks multiple campaigns, each running for n_i days (where n_i is different for each campaign). 
You're given a list of integers representing the days per campaign.

Write a recursive solution to compute the total likes across all campaigns, assuming each campaign receives 1 + 2 + ... + n_i likes.
campaign_days = [3, 2, 4]
This means output:

Campaign 1: sum of 1 to 3 = 6
Campaign 2: sum of 1 to 2 = 3
Campaign 3: sum of 1 to 4 = 10
output 19  # 6 + 3 + 10
"""

def get_total_campaign_likes(campaign_days):
    # TC O(n!) , SC: O(n!)
    n = len(campaign_days)
    def rec(ind):
        if ind >= n:
            return 0
        return get_likes(campaign_days[ind]) + rec(ind+1)
    return rec(0)

# print(get_total_campaign_likes([3, 2, 4,5]))


"""
Recursion Problem #2 (Google Style)
🏢 Scenario:
Your team at Google Photos is building a tagging engine that needs to create all
possible tag combinations from a list of user-selected keywords. However, 
due to performance constraints, each combination must preserve the original order of 
keywords and not skip any characters in between.
You're asked to implement a function that returns all subsets (a.k.a. subsequences) of a given list, 
including the empty subset.
Input: ['beach', 'sunset']
Output: [
  [],
  ['beach'],
  ['sunset'],
  ['beach', 'sunset']
]
Input: ['cat', 'dog', 'fish']

Output:
[
 [],
 ['cat'],
 ['dog'],
 ['cat', 'dog'],
 ['fish'],
 ['cat', 'fish'],
 ['dog', 'fish'],
 ['cat', 'dog', 'fish']
]
"""


def get_all_possible_tags(keywords):
    # TC O(2^n) , SC: O(2^n)
    all_possible_tags = []
    n= len(keywords)
    def rec(ind,curr_tags):
        if ind == n:
            all_possible_tags.append(curr_tags[:])
            return
        # Now to get subsequence in order there are two possible cases
        # not take the current one
        rec(ind+1,curr_tags)
        # take the current 
        curr_tags.append(keywords[ind])
        rec(ind+1,curr_tags)
        curr_tags.pop()
    rec(0,[])
    return all_possible_tags

# print(get_all_possible_tags(['cat', 'dog', 'fish']))
    
    
"""
What if we now only wanted subsets that contain at least 2 keywords?
"""   
def get_all_possible_tags_with_atleast_k_tags(keywords,k):
    # TC O(2^n) , SC: O(2^n)
    n= len(keywords)
    def rec(ind,curr_tags,all_possible_tags):
        if ind == n:
            if len(curr_tags) >=k:
                all_possible_tags.append(curr_tags)
            return
        # Now to get subsequence in order there are two possible cases
        # not take the current one
        rec(ind+1,curr_tags,all_possible_tags)
        # take the current 
        rec(ind+1,curr_tags+[keywords[ind]],all_possible_tags)
    all_possible_tags = []
    rec(0,[],all_possible_tags)
    return all_possible_tags
print(get_all_possible_tags_with_atleast_k_tags(['cat', 'dog', 'fish'],2))


"""
Scenario:
You're building a search engine tag suggester. Each keyword group can be picked only once, 
and you need to generate all possible tag orders from a list of keywords.

❓ Problem:
Given a list of unique keywords, generate all possible orderings of tags (i.e., permutations).

Function Signature:
def get_all_tag_orders(keywords: List[str]) -> List[List[str]]:
['ml', 'ai', 'cv']


"""

def get_all_possible_permutations(tags):
    # TC O(n!) , SC: O(n!)
    """
    recursive way:
    time complexity n* n! (Correct but costly due to copying)
        n! permutations (number of paths)
        Each path takes O(n) to build via list copying (curr_tags + [x])
        
    what are we doing here?
    given arr: a b c
    select any element you are left with rest element to select from
    
        
                c  --> abc
        bc--> b  
       a        b  --> acb
                c
        
               c   --> bac
              a
        ac-->  a   --> bca
abc -->b      c
        
               b   --> cab
              a
        ab-->  a   --> cba
       c      b
    """
    n = len(tags)
    all_possible_permutations = []
    def rec(curr_tags ,available_tags):
        if len(curr_tags)==n:
            all_possible_permutations.append(curr_tags.copy())
            return
        # Now for permutation I can select any element from index to start with and 
        # I can possibly create all permutations
        for i in range(len(available_tags)):
            rec(curr_tags + [available_tags[i]], available_tags[:i]+ available_tags[i+1:])
        
    rec([],tags)
    return all_possible_permutations

        

# print(get_all_possible_permutations(['ml', 'ai', 'cv']))
