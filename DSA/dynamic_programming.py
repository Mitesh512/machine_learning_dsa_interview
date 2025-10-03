"""
When to Use Memoization
Ask:
Are there overlapping subproblems?
Is the problem recursive with repeated calls for the same parameters?
Can the result of a subproblem be reused later?
Easy DP Problems (with Memoization)
| Problem                     | Type | Link                                                                    |
| --------------------------- | ---- | ----------------------------------------------------------------------- |
| 1. Fibonacci Number         | 1D   | [Leetcode 509](https://leetcode.com/problems/fibonacci-number/)         |
| 2. Climbing Stairs          | 1D   | [Leetcode 70](https://leetcode.com/problems/climbing-stairs/)           |
| 3. House Robber             | 1D   | [Leetcode 198](https://leetcode.com/problems/house-robber/)             |
| 4. Min Cost Climbing Stairs | 1D   | [Leetcode 746](https://leetcode.com/problems/min-cost-climbing-stairs/) |
| 5. Tribonacci Number        | 1D   | [Leetcode 1137](https://leetcode.com/problems/n-th-tribonacci-number/)  |
| 6. Decode Ways              | 1D   | [Leetcode 91](https://leetcode.com/problems/decode-ways/)               |

Medium:
| Problem                          | Type | Link                                                                       |
| -------------------------------- | ---- | -------------------------------------------------------------------------- |
| 1. Coin Change                   | 1D   | [Leetcode 322](https://leetcode.com/problems/coin-change/)                 |
| 2. Partition Equal Subset Sum    | 2D   | [Leetcode 416](https://leetcode.com/problems/partition-equal-subset-sum/)  |
| 3. Target Sum                    | 2D   | [Leetcode 494](https://leetcode.com/problems/target-sum/)                  |
| 4. Word Break                    | 1D   | [Leetcode 139](https://leetcode.com/problems/word-break/)                  |
| 5. Unique Paths II               | 2D   | [Leetcode 63](https://leetcode.com/problems/unique-paths-ii/)              |
| 6. Longest Palindromic Substring | 2D   | [Leetcode 5](https://leetcode.com/problems/longest-palindromic-substring/) |

Hard Problems
| Problem                        | Type | Link                                                                      |
| ------------------------------ | ---- | ------------------------------------------------------------------------- |
| 1. Regular Expression Matching | 2D   | [Leetcode 10](https://leetcode.com/problems/regular-expression-matching/) |
| 2. Edit Distance               | 2D   | [Leetcode 72](https://leetcode.com/problems/edit-distance/)               |
| 3. Interleaving String         | 3D   | [Leetcode 97](https://leetcode.com/problems/interleaving-string/)         |
| 4. Wildcard Matching           | 2D   | [Leetcode 44](https://leetcode.com/problems/wildcard-matching/)           |
| 5. Palindrome Partitioning II  | 2D   | [Leetcode 132](https://leetcode.com/problems/palindrome-partitioning-ii/) |
| 6. Scramble String             | 3D   | [Leetcode 87](https://leetcode.com/problems/scramble-string/)             |
"""


"""
Reward Points Redemption"
Context:
You're working on a rewards redemption feature for Google Pay. 
Users earn reward points every day. A user can redeem points from any day, 
but if they redeem on a given day, they must skip the next day 
(redemption is not allowed on consecutive days to prevent abuse).

Problem:
Given a list of integers representing the reward points earned each day, 
return the maximum number of points a user can redeem under the no-consecutive-day constraint.

Input: [3, 2, 5, 10, 7]
Output: 15

### 🔹 Constraints:
 1 ≤ len(reward_points) ≤ 10⁵
 0 ≤ reward_points[i] ≤ 10⁴
"""
from typing import List
def max_reward_points(reward_points: List[int]) -> int:
    """
    Since I can not take consecutive cases.
    If I take reward i, next option available to take is i+2
    or I dont't take i and take i+1
    from both the cases I want to get max value that I can get to which I will store in a memo
    this is a top down approach.
    """
    # TC O(n), SC O(n)
    n = len(reward_points)
    memo = {}
    
    def rec(ind):
        if ind >= n:
            return 0
        if ind in memo:
            return memo[ind]
        # take max of (curr num + (i+2) & i+1)
        ans = max(reward_points[ind]+ rec(ind+2), rec(ind+1))
        memo[ind] = ans
        return memo[ind]
    
    ans = rec(0)
    return ans
# print(max_reward_points([3, 2, 5, 10, 7, 2, 3, 4, 5, 6, 7, 7]))


def max_reward_points_bottom_up(reward_points: List[int]) -> int:
    """
    TC O(n)
    SC O(1)
    """
    n = len(reward_points)
    if n==0:
        return 0
    if n<=2:
        return max(reward_points)
    
    iplus2 = reward_points[-1]
    iplus1 = reward_points[-2]
    max_rewards = max(iplus1,iplus2)
    
    for i in range(n-3,-1,-1):
        max_rewards = max(reward_points[i] + iplus2, iplus1)
        iplus2 = iplus1
        iplus1 = max_rewards
    return max_rewards

# print(max_reward_points_bottom_up([3, 2, 5, 10, 7, 2, 3, 4, 5, 6, 7, 7]))


"""
You're designing a feature for a Google Fit application where a user climbs stairs. 
Each stair has a cost of effort associated with stepping on it. 
The user can start from step 0 or step 1, and can take either one or two steps at a time. 
You want to find the minimum total cost to reach just beyond the last stair.
You are given an integer array cost where cost[i] is the cost of i-th step.
Once you pay the cost, you can either climb one or two steps.
You can start from step 0 or 1.
Return the minimum cost to reach the top of the floor (one step past the last index).

🧪 Example 1:
Input:
cost = [10, 15, 20]
Output: 15
Explanation:

Start at step 1 (cost 15), then go directly to the top.

🧪 Example 2:
Input:
cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
"""


def minCostClimbingStairs(cost: List[int]) -> int:
    """
    This Looks same problem like the house robber but with variation.
    you pay the cost and you move either 1 or 2, the thing is you have to pay the price of current stair in both the cases
    """
    # ##### Approach 1: starting from 0th index and 1st index not very efiicient
    # n = len(cost)
    # memo={}
    # def rec(i):
    #     # base case would be if you reach to top of the stair or more
    #     if i >= n:
    #         # top floor is n-1 you are past that, 
    #         # you have reached the top aready and now you are going beyond that
    #         return 0 
    #     if i in memo:
    #         return memo[i]
    #     # my min cost can be calculated by exploring two options 
    #     # take curr cost and move 1 step or move 2 steps.
    #     ans = min(cost[i] + rec(i+1), cost[i] + rec(i+2))
    #     memo[i] = ans
    #     return memo[i]
    # ans = min(rec(0),rec(1))
    # return ans

    ####### Approach 2: Instead of starting from 0th stair lets start from top and as soon as you reach 0 or 1 you return its value

    n = len(cost)
    memo = {}
    def rec(i):
        if i <=1:
            return 0
        if i in memo:
            return memo[i]
        # Now there can be two cases to reach to top i, either you come from i-1 or you come from i -2
        ans = min(cost[i-1]+ rec(i-1), cost[i-2] + rec(i-2))
        memo[i] = ans
        return memo[i]        
    return rec(n)

    #######Appraoch 3 : Tabulation
    # So I Know I can either start from 0 or 1 my cost will start after that
    # n = len(cost)
    # prev2 = cost[0]
    # prev1 = cost[1]

    # for i in range(2,n+1):
    #     if i ==n:
    #         curr_cost = 0
    #     else:
    #         curr_cost = cost[i]
    #     # to current step i you will either come from prev1 step prev2 step
    #     min_cost = min(curr_cost + prev1, curr_cost+prev2)
    #     prev2= prev1
    #     prev1= min_cost
    
    # return min_cost
# print(minCostClimbingStairs([1,2,3,3,4]))
    



"""
You're working on a health analytics system for tracking long-term health improvement.
A user's improvement score on the n-th day is defined using historical trends over the previous three days:
The score on day n is the sum of scores from:
Day n - 1
Day n - 2
Day n - 3

For simplicity, the first few days are initialized with:
Day 0 → 0
Day 1 → 1
Day 2 → 1

You're tasked with writing an efficient program to compute the score on day n.

Input: n = 4

Day 0 → 0  
Day 1 → 1  
Day 2 → 1  
Day 3 → 0 + 1 + 1 = 2  
Day 4 → 1 + 1 + 2 = 4 ✅

Output: 4

"""

def tribonacci(n: int) -> int:
    """
    It same like fibonacci number 
    TC O(n), SC O(n)
    """
    # memo = {}
    # def rec(i):
    #     if i in memo:
    #         return memo[i]
    #     if i == 0:
    #         return 0
    #     if i == 1 or i == 2:
    #         return 1
    #     ans =  rec(i-1) + rec(i-2) + rec(i-3)
    #     memo[i] = ans
    #     return memo[i]
    # return rec(n)
    
    ### Tabulation approach
    # TC O(n), SC O(1)
    if n == 0: return 0
    if n == 1 or n == 2: return 1
    
    prev3 = 1
    prev2 = 1
    prev1 = 0
    for i in range(3,n+1):
        ans = prev3 + prev2 + prev1
        prev3,prev2,prev1 = prev2,prev1,ans
    return ans

# print(tribonacci(16248))
# print(len(str(tribonacci(16248))))
# print(tribonacci(37))
# print(len(str(tribonacci(37))))

"""
Google-Style Scenario
You're building an internal SMS parser at Google, 
which must interpret digit strings into meaningful letter sequences 
(e.g., "1" → "A", ..., "26" → "Z"). You're given a string of digits sent by a service. 
You must return the total number of valid ways to decode the message.
Constraints
1 <= s.length <= 100
s contains only digits and may start with '0'

Input: "12"
Output: 2
Explanation: "12" can be decoded as "AB" (1 2) or "L" (12)

Input: "226"
Output: 3
Explanation: "2 2 6" → "BBF", "22 6" → "VF", "2 26" → "BZ"
"""


def decode_ways(s):
    # s= "112310621"
    # memo: {8: 1, 7: 2, 6: 2, 4: 2, 3: 2, 2: 4, 1: 6, 0: 10}
    n = len(s)
    memo = {}
    def rec(i,s,memo):
        if i == n:
            # I have reached to end so I have foudn a way 
            return 1
        # alphabets are designed to be between 1 and 26 so 0 is invalid only 10, 20 are valid
        if s[i] == "0":
            return 0
        if i in memo:
            return memo[i]
        # you can always check way with single digit
        ways = rec(i+1,s,memo)
        # check for 2 digits
        if i < n-1 and 10 <= int(s[i:i+2]) <=26:
            ways += rec(i+2,s,memo)
        memo[i] = ways
        return memo[i]

    ans =  rec(0,s,memo)
    print(memo)
    return ans

    

print(decode_ways("112310621"))
s= "112310621"
# memo: {8: 1, 7: 2, 6: 2, 4: 2, 3: 2, 2: 4, 1: 6, 0: 10}


"""
You are working on the payments team at Google Pay.
Users can pay their bills using gift cards of fixed denominations (e.g., ₹1, ₹2, ₹5).
Given a bill amount, your service must determine the minimum number of gift cards required to exactly pay that amount.
If it's not possible to pay the exact amount using any combination of the available denominations, return -1.
coins = [1, 2, 5]
amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

coins = [2]
amount = 3
Output: -1
Explanation: You can't make 3 using only 2-rupee coins.

coins = [1]
amount = 0
Output: 0
Explanation: No coins are needed.

"""

def get_coin_change(coins, amount):
    """
    I have coins supply that is unlimited and I can chose any nymber of coins
    I need to get to that amount, I need to return the minimum number of coins required to do so.
    I can do a recursive solution at each step check with possible coins to get to that value
    
    so I have a target that I need to reach to so I my base case will be 
    I mean I will reduce the target as soon as i pick the coin
    if amount == 0
    """
    # memo = {}
    # def rec(target,memo):
    #     if target in memo:
    #         return memo[target]
    #     if target == 0:
    #         # I have found a possible solution
    #         return 0
    #     if target < 0:
    #         return float("inf")
    #     # what possible cases I have
    #     min_coins = float("inf")
    #     for coin in coins:
    #         coint_count = 1 + rec(target - coin,memo)
    #         min_coins = min(min_coins, coint_count)
    #     memo[target] = min_coins
    #     return memo[target]
    # min_coins = rec(amount,memo)
    # return -1 if min_coins == float("inf") else min_coins
    
    
    memo = {}
    def rec(i, target):
        if target == 0:
            return 0
        if target < 0 or i == len(coins):
            return float("inf")        
        if (i, target) in memo:
            return memo[(i, target)]

        # Case 1: Take current coin[i], stay on same index (unlimited supply)
        take = 1 + rec(i, target - coins[i])
        # Case 2: Skip current coin[i], move to next index
        skip = rec(i + 1, target)
        memo[(i, target)] = min(take, skip)
        return memo[(i, target)]

    result = rec(0, amount)
    return -1 if result == float("inf") else result

    
    
# print(get_coin_change([1,2,5],11))
# print(get_coin_change([186,419,83,408], 6249))


# 33 + 2 -->  23
# 22 + 1 + 1 --> 12 
# 56 --> 24
# 24 + 1 + 83 --> 10



"""
KnapSack 0/1 problem:
Mamximize profit for given capacity and weight constraint
capacity = 4, 
profit[] = [1, 2, 3]
weight[] = [4, 5, 1]
Output: 3
Explanation: There are two items which have weight less than or equal to 4. 
If we select the item with weight 4, the possible profit is 1. 
And if we select the item with weight 1, the possible profit is 3. 
So the maximum possible profit is 3. Note that we cannot put both the items with weight 4 and 1 together as the capacity of the bag is 4.

Input: capacity = 3, profit[] = [1, 2, 3], weight[] = [4, 5, 6]
Ouput = 0

How we can solve this is lets check for all possible combinations
start from 0th bag or nth bag
"""

def kanpsack_0_1(capacity,weight, profit):
    ### Approach 1 try out all paths
    # def rec(ind,curr_capacity,weight,profit):
    #     if ind == n:
    #         # you have exhausted all the paths
    #         return 0 
    #     # Either you pick the current bag given the capacity or you go to next one
    #     # pick
    #     pick = 0
    #     # I can only pick weight[ind] if I have capacity to have it
    #     if curr_capacity >= weight[ind]:
    #         # accumulate the profit
    #         pick = profit[ind] + rec(ind + 1,curr_capacity - weight[ind] ,weight,profit)
    #     # don't pick current bag and explore other bags, without earning any profit or reducing your capacity
    #     not_pick = rec(ind + 1,curr_capacity ,weight,profit)
    #     return max(pick,not_pick)
    
    # n = len(weight)
    # max_profit = rec(0,capacity,weight,profit)
    # return max_profit
    
    
    ##### Appraoch 2 I know there are two variables , ind, capacity Let's memoize it
    n = len(weight)
    memo ={} # in tuple way (ind,capacity)
    def memo_rec(ind,curr_capacity, weight,profit,memo):
        # check memo first
        if (ind,curr_capacity) in memo:
            return memo[(ind,curr_capacity)]
        # base cases
        if ind == n:
            return 0
        
        # pick case
        pick = 0
        if curr_capacity >= weight[ind]:
            pick = profit[ind] + memo_rec(ind+1, curr_capacity-weight[ind],weight,profit,memo)
            
        not_pick = memo_rec(ind+1,curr_capacity, weight, profit,memo)
    
        memo[(ind,curr_capacity)] = max(pick,not_pick)
        return memo[(ind,curr_capacity)]
    
    max_profit = memo_rec(0,capacity,weight,profit,memo)
    return max_profit
    

# print(kanpsack_0_1(4,[4,5,1], [1,2,3]))
# print(kanpsack_0_1(0,[4,5,1], [1,2,3]))

"""
Unbounded Knapsack Problem:
Given a knapsack weight, say capacity and a set of n items with certain value val[i] and weight wt[i], 
The task is to fill the knapsack in such a way that we can get the maximum profit. 
This is different from the classical Knapsack problem,
here we are allowed to use an unlimited number of instances of an item.

Input: capacity = 100, profit= [1, 30], wt = [1, 50]
Output: 100 
Explanation: There are many ways to fill knapsack. 
1) 2 instances of 50 unit weight item. 
2) 100 instances of 1 unit weight item. 
3) 1 instance of 50 unit weight item and 50 instances of 1 unit weight items. 
We get maximum value with option 2.  
"""

def unbounded_kanpsack(capacity,weight,profit):
    ## Approach 1 where I will iterate for each case 
    # n = len(weight)
    # def rec(curr_capacity,weight,profit):
    #     # base case
    #     if curr_capacity == 0:
    #         # you have consumed all your capacity
    #         return 0
    #     # try out all ways 
    #     max_profit = 0
    #     for i in range(n):
    #         # check if I have capacity then only I can go and epxlore
    #         if curr_capacity >= weight[i]:
    #             curr_profit = profit[i]+ rec(curr_capacity-weight[i], weight,profit)
    #             max_profit = max(max_profit,curr_profit)
    #     return max_profit
    # max_profit = rec(capacity,weight,profit)
    # return max_profit
    
    # Approach 2 where index is part of function and apply memoization is easy
    # n = len(weight)
    # def rec(ind,n,curr_capacity,weight,profit):
    #     if ind ==n:
    #         return 0
    #     take = 0
    #     if curr_capacity >= weight[ind]:
    #         # as we are allowed to take it again so no need to increase ind
    #         # we will again explore the ind but reduce our capacity
    #         take = profit[ind] + rec(ind,n,curr_capacity-weight[ind],weight,profit)
    #     not_take = rec(ind+1,n,curr_capacity, weight,profit)
    #     return max(take,not_take)
    # max_profit = rec(0,n,capacity,weight,profit)
    # return max_profit
    
    ### Better Appraoch using memoization
    # variables are curr_capacity and i
    memo = {} # (capacity,ind)
    n = len(weight)
    def rec(ind,n,memo,curr_capacity,weight,profit):
        if (curr_capacity,ind) in memo:
            return memo[(curr_capacity,ind)]
        # base case
        if ind == n:
            return 0
        take = 0
        if curr_capacity >= weight[ind]:
            take = profit[ind]+ rec(ind,n,memo,curr_capacity-weight[ind],weight,profit)
        
        not_take = rec(ind+1,n,memo,curr_capacity,weight,profit)
        max_profit = max(take,not_take)
        memo[(curr_capacity,ind)] = max_profit
        return memo[(curr_capacity,ind)]
    max_profit = rec(0,n,memo,capacity,weight,profit)
    return max_profit

# print(unbounded_kanpsack(4,[4,5,1], [1,2,3]))
# print(unbounded_kanpsack(100,[1,50], [1,30]))
# print(unbounded_kanpsack(8,[1,3,4,5],[10,40,50,70] ))


"""
Given an array arr[] containing the weight of 'n' distinct items, 
and two knapsacks that can withstand capactiy1 and capacity2 weights, 
the task is to find the sum of the largest subset of the array 'arr', 
that can be fit in the two knapsacks. It's not allowed to break any items in two, 
i.e. an item should be put in one of the bags as a whole.

Examples: 
Input: arr[] = [8, 3, 2], capacity1 = 10, capacity2 = 3 
Output: 13 
Explanation: The first and third items are placed in the first knapsack, 
while the second item is placed in the second knapsack. 
This results in a total weight of 13.

Input: arr[] = [8, 5, 3] capacity1 = 10, capacity2 = 3 
Output: 11 
Explanation: The first item is placed in the first knapsack, 
and the third item is placed in the second knapsack. 
This results in a total weight of 11. 
"""              

def double_knapsack(capacity1,capacity2,weight):
    n = len(weight)
    memo = {} # ind,c1,c2
    def rec(i,curr_cap1,curr_cap2,weight,memo):
        if (i,curr_cap1,curr_cap2) in memo:
            return memo[(i,curr_cap1,curr_cap2)]
        
        if i == n:
            return 0
        
        # Now either you take using capacity 1 or capacity 2
        take_c1 = 0
        # check with capacity 1
        if curr_cap1 >= weight[i]:
            take_c1 = weight[i] + rec(i+1,curr_cap1 - weight[i], curr_cap2, weight,memo)
        
        take_c2 = 0
        if curr_cap2 >= weight[i]:
            take_c2 =  weight[i] + rec(i+1,curr_cap1, curr_cap2 - weight[i], weight,memo)
        
        # explore other weights
        not_take = rec(i+1,curr_cap1,curr_cap2,weight,memo)
        max_wt = max(take_c1,take_c2, not_take)
        memo[(i,curr_cap1,curr_cap2)] = max_wt
        return max_wt
    
    max_wt = rec(0,capacity1, capacity2, weight,memo)
    return max_wt
    
# print(double_knapsack(10,3,[8, 3, 2]))
# print(double_knapsack(10,3,[8, 5, 3]))
        


### Fractional Knapsack

"""
Given two arrays, val[] and wt[], representing the values and weights of items, 
and an integer capacity representing the maximum weight a knapsack can hold, 
the task is to determine the maximum total value that can be achieved by 
putting items in the knapsack. You are allowed to break items into fractions if necessary.

Note: Return the maximum value as a double, rounded to 6 decimal places.

Input: val[] = [60, 100, 120], wt[] = [10, 20, 30], capacity = 50
Output: 240 
Explanation: By taking items of weight 10 and 20 kg and 2/3 fraction of 30 kg. 
Hence total price will be 60+100+(2/3)(120) = 240

Input:  val[] = [500], wt[] = [30], capacity = 10
Output: 166.667
"""


def fractional_kanpsack(capacity, weight, profit):
    n = len(weight)
    profit_weight_ratio = [(profit[i]/weight[i],i) for i in range(n)]
    profit_weight_ratio = sorted(profit_weight_ratio, reverse=True)
    
    max_profit = 0
    for profit_ratio,i in profit_weight_ratio:
        if capacity >= weight[i]:
            max_profit += profit_ratio * weight[i]
            capacity -= weight[i]
        else:
            max_profit += profit_ratio * capacity
            break
        
    return round(max_profit,6)
            
# print(fractional_kanpsack(50, [20,10, 30], [100,60, 120]))
# print(fractional_kanpsack(10, [30], [500]))
    
"""
You're working on an internal billing system at Google where users 
can be credited with virtual coins of certain denominations. 
You want to count how many unique combinations of coins can be used 
to reach a certain amount.

Unlike the previous problem, you don't care about the minimum number of coins, 
only about the total number of distinct ways the coins can be combined to reach the target.
Input: coins = [1, 2, 5], amount = 5
Output: 4

Explanation:
There are 4 combinations:
  5 = 5
  5 = 2 + 2 + 1
  5 = 2 + 1 + 1 + 1
  5 = 1 + 1 + 1 + 1 + 1
"""

def get_coin_combination(coins, amount):
    memo = {}
    def rec(i, curr_amount):
        if curr_amount == 0:
            return 1
        if curr_amount < 0 or i == len(coins):
            return 0
        if (i, curr_amount) in memo:
            return memo[(i, curr_amount)]
        
        # Option 1: take coin[i]
        take = rec(i, curr_amount - coins[i])
        
        # Option 2: skip coin[i]
        skip = rec(i + 1, curr_amount)

        memo[(i, curr_amount)] = take + skip
        return memo[(i, curr_amount)]
    return rec(0,amount)
    

# print(get_coin_combination([1,2,5],5))


"""
Regular Expression Matching
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Example 1:
Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
"""

def match_without_kleenestar(s, p):
    """
    In case we don't have kleene (*)
    We just need to match pattern with the string
    
    definition of pattern is that it can create the string.
    that means whole of the pattern should be used to create the whole of the string.
    if pattern is bigger than it won't be able to create the string at any cost until we have some wild card that can does it
    
    so idea is simple check for each element of s[i] and p[j]
    if they match return True otherwise return False
    
    base case would be 
    if i has been reached and j has been reach to end at the same time that means we have found 
    """
    ns = len(s)
    np = len(p)
    def rec(i,j,ns,np,s,p):
        # base case: both strings fully matched
        if i == ns and j == np:
            return True
        # mismatch in lengths
        if i == ns or j == np:
            return False
        # current character matches (or . wildcard)
        if s[i] == p[j] or p[j] == ".":
            return rec(i + 1, j + 1,ns,np,s,p)
        else: # if we don't use else then also it can work
            # characters do not match
            return False
    return rec(0,0,ns,np,s,p)
# print(match_without_kleenestar("baca", "..aca"))         # False
# print(match_without_kleenestar("ab", ".."))         # True
# print(match_without_kleenestar("mississippi", "mis.is..p..")) 


def match_expression(s,p):
    ns = len(s)
    np = len(p)
    
    def rec(i,j,ns,np,s,p,memo):
        if (i,j) in memo:
            return memo[(i,j)]
        # base case pattern has matched to string fully
        if i == ns and j==np:
            return True
        # it means my i in s is still not complete but j is already done
        if j == np:
            return False 
        
        # Difference cases
        # both match either by character or "."
        match = False
        if i < ns and ((s[i] == p[j]) or (p[j] == ".")):
            match = True
            
        # Handle the wild card "*"
        if j+1 < np and p[j+1] == "*":
            # two options
            # 1. Skip the 'char*' (zero occurrence) consider zero occurace
            # 2. If current matches, use one char from s (stay at p[j])
            # there can be two casesa
                # either you keep using *, increase i keep j same or skip currletter, * and move to j+2 , i remains same
                # you can continue iterating only till you find match
                
            take = False
            if match:
                # increase i and keep j same as you will keep iterating
                take  = rec(i+1,j,ns,np,s,p,memo)
            # you will just skip the wild card to explore other path
            not_take = rec(i,j+2,ns,np,s,p,memo)

            # anyone of above can you get me pattern match?
            memo[(i,j)] = take or not_take
            return memo[(i,j)]
        
        else:
            if match:
                match = rec(i+1,j+1,ns,np,s,p,memo)
            memo[(i,j)] = match
            return memo[(i,j)]
    
    memo = {}
    expression_found = rec(0,0,ns,np,s,p,memo)
    return expression_found

# print(match_expression("aa", "a"))          # False
# print(match_expression("aa", "a*"))         # True
# print(match_expression("ab", ".*"))         # True
# print(match_expression("mississippi", "mis*is*p*."))  # False
# print(match_expression("abcaaaaaaabaabc", ".*ab.a.*c"))  # True


            
        
"""
You're designing a calculator search interface for Google Sheets.
A user enters a string of digits like "123" and a target number like 6.
Your task is to insert operators (+, -, *) between digits to form valid expressions that evaluate to the target.

Given a string num and an integer target, return all expressions that evaluate to the target.
You may add +, -, or * between digits.
Digits must be used in order.
No leading zeros (i.e., "05" is invalid).
Only valid expressions.
"""


def generate_expression(string_num, target):
    
    """
    This has 3 operations
    -
    +
    *
    So for each case there will be 3 operations I can perform
    
    To create the experession I need to carry 
    expression: []
    expression_value: 0
    previous_number (why?): in case of multiplication I need to apply substraction of prevous one 
        1+2*3 is actually 7
        but if we go recursively
        1+2 value is 3 and 3*3 is 9 which is wrong
        so we can apply this logic in multiplication case 
        current num is 3 prev is 2  expression_val is 3
        expression_val - prev val = 3 - 2 = 1
        prev_val * curr_val = 2 * 3
        so overall 
        expression_val - prev val + prev_val * curr_val
        
        in this multiplication case prev value after this operation will be prev_val * curr_val
    
    results: []
    
    I need to check for leading zero case also
    05 should not be considered to handle that when we are iterating in loop at that time 
    we can put a check
    
    Time Complexity:

    At every step along the way, we consider exactly 4 different choices or 4 different recursive paths. The base case is when the value of index reaches N i.e. the length of the nums array. 
    Hence, our complexity would be O(4^N).
    For the base case we use .join() operation in Python and that takes O(N) time. 
    Here N represents the length of our expression. 
    In the worst case, each digit would be an operand and we would have N digits and N-1 operators. 
    So O(N). This is for one expression. In the worst case, we can have O(4^N)valid expressions.
    Overall time complexity = O(N. 4^N)
    
    
    Space Complexity
    So, the space occupied by the intermediate list would be O(N) since in the worst case the expression would be built out of all the digits as operands.
Additionally, the space used up by the recursion stack would also be O(N) since the size of recursion stack is determined by the value of index and it goes from 0 all the way to N.
We don't consider the space occupied by the answers array since that is a part of the question's requirement and we can't reduce that in any way
    
    """
    
    n = len(string_num)
    def rec(curr_ind,n, stirng_num,target, prev_val,exp, exp_val, result ):
        if curr_ind == n:
            if exp_val == target:
                result.append("".join(exp))
            return result

        # Now differnce cases
        # from my current index I can use curr nums
        # given a str 123, I have option to select my curent num as 
        # 1, 12, 123 so I have to iterate it
        
        for i in range(curr_ind,n):
            curr_str = string_num[curr_ind:i+1]
            curr_num = int(curr_str)
            #### Now I have choices if there is no previous number that means it is coming
            # for the first time
            if curr_ind == 0:
                # use the curr_num
                result = rec(i+1,n, stirng_num,target, curr_num,exp + [curr_str], curr_num, result)
            else:
                # Now lets say I have some expression already so I can apply operations on previous value
                # Add opetation
                result = rec(i+1,n, stirng_num,target, curr_num,exp + ["+"]+ [curr_str], exp_val + curr_num, result)
                # substract operation
                result = rec(i+1,n, stirng_num,target, -curr_num ,exp+ ["-"]+ [curr_str], exp_val - curr_num, result )
                # multiplication operation
                # prev_val for next operation is prev_val * curr_num
                # this makes sense because 1 + 2*3 *5
                result = rec(i+1,n, stirng_num,target, prev_val * curr_num,exp+ ["*"]+ [curr_str], exp_val-prev_val + prev_val * curr_num, result )
               
            # to handle the case of leading zeros
            # if 21054 was a sting 
            # we will iterate for 
            # 2 and all its recursive cases 21, 210, 2105,21054
            # 1 for all its recursive cases 1, 10 , 105, 1054
            # 0 not for all its recursive cases 
            # send for first case 0: 2 + 1 + 0 + 5 + 4 (its a valid case) 
            # but for next 5 we wil not carry 5 beacuse it will make num as 05 which is invalid
            # so perform opeation with single 0 but check at the end if it zero break the loop 05 is not a number to carry
            if curr_num == 0:
                break
        return result
    
    result = rec(0,n, string_num,target, 0,[], 0, [])
    
    print(result)
    return result
 
# generate_expression("13345",20)


"""
Palindrome Partitioning:

You're designing a text segmentation tool for an internal Google product. 
For optimal compression, you want to partition a string such that every 
substring is a palindrome. But, since segmentation is costly, 
you need the minimum number of cuts to partition the string this way.

Given a string s, partition it into substrings such that every substring is a palindrome.
Return the minimum number of cuts needed for a palindrome partitioning of s.

Input:
A string s of length n (1 ≤ n ≤ 2000)

Output:
Integer representing minimum number of cuts.
Input: s = "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be done with 1 cut.

Input: s = "a"
Output: 0
Explanation: Already a palindrome.

Input: s = "abcbm"
Output: 2
Explanation: "a | bcb | m"



"""

def palindrome_partition(s):
    """
    ### Approach 1 Brute Force Approach
    trying all prefixes and recursing only on the suffix 
    TC : O(n x 2^n x log(n)) iterate over n , rec 2^n, palindrom check log(n)
    SC : O(n)
    
    """
    def is_palindrome(s):
        if len(s)==1:
            return True
        l=0
        r=len(s)-1
        while l<r:
            if s[l] != s[r]:
                return False
            l +=1
            r -=1
        return True
    
    
    def rec(start,n,memo):
        """
        Idea is to check string only when till current point you have a palindrom
        s = aab
        iterate over the string check string till i if its palindrom you partition from that point
        and rest of string, so basically your left part is already a palindrome
        here is a dry run
        at start =0 i can iterate with three cases a,aa,aab    
            a yes go and check ab
            aa yes go and check b
            aab no don't go
            
        s = abcbm
        at start 0 we have options: a,ab,abc,abcb, abcbm
        a yes go and check on bcbm (part_cnt = 1), start =1
        no for ab , abc,abcb, abcbm
        
        now bcbm start 1 again options b, bc, bcb, bcbm
        b yes go and check cbm, start = 2, part_cnt =2
        bc no 
        bcb yes got and check m, start = 4 and part_cnt = 2
        bcbm no
        
        there are two options
        cbm start = 2--->  options c,cb,cbm
        c yes go ahead for bm, start =3 part_cnt = 3
        cb,cbm no
        
        m start =4, part_cnt =2 options: m
        m yes go ahead and check "" start =5, part_cnt = 3
        """
        
        if start == n:
            # we have reached to end return -1 this end partition 
            # is empty only
            return -1
        min_part = float("inf")
        for end in range(start,n):
            # check 
            if is_palindrome(s[start:end+1]):
                part = 1+ rec(end+1, n,memo)
                min_part = min(min_part,part)
        
        return min_part

    memo = {}
    return rec(0,len(s),memo)
    
    # def rec(substr):
    #     """
    #     TC : O(n x 2^n x log(n)) iterate over n , rec 2^n, palindrom check log(n)
    #     SC : O(n)
    #     """
    #     # base case
    #     if len(substr)==1 or is_palindrome(substr):
    #         return 0
    #     # Try out all possible cases
    #     # what partition can I do
    #     # aab 
    #     # 1 ---> a | ab,  2:--> aa|b
    #     # a|a|b   1+1 (two partitions)
    #     # aa|b  1+ 0 (1 partiion)
    #     min_part = float("inf")
    #     for i in range(1,len(substr)):
    #         left_substr = substr[:i]
    #         right_substr = substr[i:]
    #         part = 1 + rec(left_substr) + rec(right_substr)
    #         min_part = min(part,min_part)
    #     return min_part 
    # return rec(s)  

# print(palindrome_partition("aab"))
# print(palindrome_partition("aabc"))
# print(palindrome_partition("a"))
# print(palindrome_partition("abcbm"))

"""
Google-style Framing:
You're designing a text pre-processor at Google Docs. 
Given a continuous string typed without spaces, you need to decide whether 
the string could have been formed by concatenating valid dictionary words.

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: True

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: True

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: False
"""

def wordbreak(s,word_dict):
    n = len(s)
    memo = {}
    word_dict = set(word_dict)
    
    def rec(start,n,s,word_dict,memo):
        if start in memo:
            return memo[start]
        # Base case
        if s[start:n] in word_dict:
            return True

        if start == n:
            return False
        
        ans = False
        for end in range(start,n):
            curr_str = s[start:end+1]
            if curr_str in word_dict:
                explore_path = rec(end+1,n,s,word_dict,memo)
                if explore_path:
                    ans = True
                    break
        
        memo[start] = ans
        return ans

    return rec(0,n,s,word_dict,memo)
    
# print(wordbreak("leetcode",["leet","code"]))
# print(wordbreak("applepenapple",["apple","pen"]))
# print(wordbreak("pineapplespenapplespine",["pineapple","apples","pen","pine"]))
# print(wordbreak("catsandog",["cats","dog","sand","and","cat"]))

"""
You're working on optimizing storage in a text processing system. 
To compress text efficiently, you want to identify the longest palindromic subsequence in a given string — 
a sequence that reads the same backward and forward, not necessarily contiguous.

📘 Problem Statement:
Given a string s, return the length of the longest palindromic subsequence in s.

Constraints:
1 ≤ s.length ≤ 1000

s contains only lowercase English letters.
Input: s = "bbbab"
Output: 4
Explanation: One possible LPS is "bbbb"
Input: s = "cbbd"
Output: 2
Explanation: One possible LPS is "bb"


"""

def longest_palindrome_subseq(s):
    n = len(s)
    memo ={}
    
    def rec(i,j,s,memo):
        if (i,j) in memo:
            return memo[(i,j)]
        
        # base case 
        if i > j:
            return 0
        if i==j:
            return 1

        
        if s[i] == s[j]:
            pal_len = 2 + rec(i+1,j-1,s,memo)
        else:
            pal_len = max(rec(i+1,j,s,memo), rec(i,j-1,s,memo))
        
        memo[(i,j)] = pal_len
        return memo[(i,j)]
    
    longest_paln = rec(0,n-1,s,memo)
    return longest_paln
            
        
# print(longest_palindrome_subseq("asdaetefdeabcbaedfieds"))      

"""
Find longest palindrome itself
Time: O(n³) — because for each (i, j), we may call is_palindrome(i, j) which is O(n), and we do it for O(n²) states.

Space: O(n²) for memoization + recursion stack
"""

def longest_palindromic_substring(s):
    n = len(s)
    memo = {}

    def is_palindrome(i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    def rec(i, j):
        if i > j:
            return ""
        if (i, j) in memo:
            return memo[(i, j)]

        if is_palindrome(i, j):
            memo[(i, j)] = s[i:j+1]
            return memo[(i, j)]

        left = rec(i+1, j)
        right = rec(i, j-1)

        memo[(i, j)] = left if len(left) >= len(right) else right
        return memo[(i, j)]

    return rec(0, n-1)



"""
Longest commong subsequence:
You're working on the Gmail autosync engine. To improve sync efficiency, 
you want to identify common patterns between a cached local copy and the new server version of an email’s content.

This is not about exact matching—you're allowed to skip some characters.
Your goal is to compute the length of the longest common pattern (subsequence) between two versions of the email content.

This will help you determine the minimum number of operations needed to sync.
# print(get_lcs("abcde", "ace"))  
# print(get_lcs("aggtab", "gxtxayb"))  
# print(get_lcs("abcfde","abbclsdfde"))
"""

def get_lcs(s1,s2):
    
    """
    Longest commong subsequence:
    TC = O(mxn)
    SC = O(mxn)
    """
    n = len(s1)
    m = len(s2)
    memo = {}
    
    def rec(i,j,n,m,s1,s2,memo):
        if (i,j) in memo:
            return memo[(i,j)]
        # base case
        if i==n or j==m:
            return 0
        
        # check i of s1 with j of s2
        if s1[i] == s2[j]:
            # increase both and you increase length by 1
            lcs = 1+ rec(i+1,j+1,n,m,s1,s2,memo)
        else:
            # so there are two option I can match with
            # either increase index for word 1 for word 2
            pick1 = rec(i+1,j,n,m,s1,s2,memo)
            pick2 = rec(i,j+1,n,m,s1,s2,memo)
            # I need to find longest common subsequence
            lcs = max(pick1, pick2)
            
        memo[(i,j)] = lcs
        return lcs
    
    return rec(0,0,n,m,s1,s2,memo)
            
# print(get_lcs("abcde", "ace"))  
# print(get_lcs("aggtab", "gxtxayb"))  
# print(get_lcs("abcfde","abbclsdfde"))


def get_lcs_string(s1, s2):
    # Longest commong subsequence
    n = len(s1)
    m = len(s2)
    memo = {}
    
    def rec(i, j,n,m,s1,s2,memo):
        if (i, j) in memo:
            return memo[(i, j)]
        
        # base case
        if i == n or j == m:
            return ""
        
        if s1[i] == s2[j]:
            memo[(i, j)] = s1[i] + rec(i + 1, j + 1,n,m,s1,s2,memo)
        else:
            pick1 = rec(i + 1, j,n,m,s1,s2,memo)
            pick2 = rec(i, j + 1,n,m,s1,s2,memo)
            if len(pick1)> len(pick2):
                memo[(i,j)] = pick1
            else:
                memo[(i, j)] = pick2
        
        return memo[(i, j)]

    return rec(0, 0,n,m,s1,s2,memo)

# print(get_lcs_string("abcde", "ace"))  # Output: "ace"
# print(get_lcs_string("aggtab", "gxtxayb"))  # Output: "gtab"
# print(get_lcs_string("abcfde","abbclsdfde")) # Output: "abcfde"


"""
You're working on Google Docs' real-time collaborative editor.
When a user types or edits a document, Google wants to suggest how similar the edited version is to the original document.
You're tasked with building a tool that tells how many operations (insertions, deletions, or replacements) are needed to convert one string (original) into another (edited).

This helps with:
Smart autocorrect
Diff and merge tools
Plagiarism or version comparison
Search query refinement


Given two strings word1 and word2, return the minimum number of operations required to convert word1 into word2.
Allowed operations:
    Insert a character
    Delete a character
    Replace a character
    
word1 = "intention"
word2 = "execution"
Output = 5

Explanation:
intention → inention (delete 't')  
          → enention (replace 'i' with 'e')  
          → exention (replace 'n' with 'x')  
          → exection (replace 'n' with 'c')  
          → execution (insert 'u')

"""


def edit_distance(word1,word2):
    """
    What I need to do is 
    convert word1 into word2
    
    word1 = "abc"
    word2 = "abcd"
    
    word1 = "intention"
    word2 = "execution"
    
    I can try to solve it recursively because I have multiple options and I want to find the min operations to get it done.
    I can start iterating both the words: i,j
    
    ### Possible options
    if both letters are same, there is no need to perform any operation. and move both i,j by 1--> i+1, j+1
    
    else:
        ### perform operations on word1
        either I can delete, insert or replace
        delete from word1: i will incrase i+1 and j remain same with operation +1
        insert in word1: so we will be inserting the chr same as word2's j ind so I can increase j+1, i remain same operation +1
        replace: both i,j will increase as upon replacing both will match i+1, j+1 and operation +1
        
        get min of all 3 operations.
    
    ## what will be my base case?
    if both i and j reach to n, that basically means both word have been matched at same time:
    return 0
    
    if any of i or j reaches n then 
        either i has'nt reached word1 has extra characters that needs to be deleted
        or j hasn't reached so we will have to insert the chr in word1.
        
        in both cases whatever length is remained that many operations has be performed so we can just return extra len
    
    we can do memoization in case of overlapping subproblems
    Time: O(n x m)

    Space Complexity:
    Memoization table stores up to n x m entries → O(n x m)

    Call stack in the worst case goes as deep as n + m → O(n + m)

    Space: O(n x m)
    """
    n = len(word1)
    m = len(word2)
    memo = {}
    
    def rec(i,j,n,m,word1,word2,memo):
        if (i,j) in memo:
            return memo[(i,j)]
    
        ## base cases
        if i==n and j==m:
            return 0
    
        if i==n:
            # word1 is over return remaining len of word 2
            return m-j
        
        if j==m:
            # word 2 is over return remaining len of word 1
            return n-i

        if word1[i]==word2[j]:
            # no operation is performed
            operations = rec(i+1,j+1,n,m,word1,word2,memo)
        else:
            # delete form word1, i+1
            delete_op = rec(i+1,j,n,m,word1,word2,memo)
            
            # insert in word1
            insert_op = rec(i,j+1,n,m,word1,word2,memo)
            
            # replace in word1
            replace_op = rec(i+1,j+1,n,m,word1,word2,memo)
            
            operations = 1 + min(delete_op,insert_op,replace_op)
        memo[(i,j)] = operations
        return memo[(i,j)]
    
    return rec(0,0,n,m,word1,word2,memo)
        
# print(edit_distance("abc","abcd"))
# print(edit_distance("intention","execution"))
    