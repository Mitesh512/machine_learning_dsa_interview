from typing import List
class Transactions:
    def __init__(self,transactions:List[int]):
        self.transactions = transactions
        self.prefix_sum = []
        self.get_prefix_sum()
    
    def get_prefix_sum(self):
        curr_sum = 0
        for i in range(len(self.transactions)):
            curr_sum += self.transactions[i]
            self.prefix_sum.append(curr_sum)
    
    def transaction_between_two_times(self,l:int,r:int) -> int:
        if l == 0:
            return self.prefix_sum[r]
        else:
            return self.prefix_sum[r] - self.prefix_sum[l-1]


# transact_obj = Transactions([100, 200, 50, 400, 150])
# [100,300,350,750,900]
# print(transact_obj.prefix_sum)
# print(transact_obj.transaction_between_two_times(1,3))  [1,3]
# print(transact_obj.transaction_between_two_times(0,4))

"""
On Google Maps, you analyze traffic data from a smart road. Each element in the list represents the number of cars that passed a sensor each day.
You need to detect if there's any “balanced split day” where:

Sum of cars from 0 to i-1 == sum of cars from i+1 to n-1

Given an array of integers nums, calculate the pivot index of this array.
The pivot index is the index where the sum of all the numbers strictly to the left of the index is 
equal to the sum of all the numbers strictly to the index's right.
If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. 
This also applies to the right edge of the array.
Return the leftmost pivot index. If no such index exists, return -1.
Example 1:

Input: nums = [1,7,3,6,5,6] --> 6
[1,8,11,17,22,28]
 0 1  2  3 4  5 

Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11
"""

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        """
        get prefix sum,
        move from left to right
        for each ind chekc pref_sum[ind-1] and pref_sum[n-1] pref_sum[ind] 
        if both are equal just send that
        """
        pref_sum = []
        curr_sum = 0
        for num in nums:
            curr_sum += num
            pref_sum.append(curr_sum)
        
        r = len(nums)-1
        for i in range(len(nums)):
            if i ==0:
                if pref_sum[r] - pref_sum[i] ==0:
                    return i
                else:
                    continue

            if pref_sum[i-1] == pref_sum[r] - pref_sum[i]:
                return i
        return -1


"""

Google-style Scenario:
You're developing a feature in Google Sheets to auto-flag rows with 
negative profit trends. Given a list of profits/losses, 
flag all days where cumulative profit so far drops below zero.

🧪 Examples:
python
Copy code
profits = [200, -500, 300, -100, -50]
Cumulative: [200, -300, 0, -100, -150]
Flagged days: Day 1, Day 3, Day 4

"""
def get_negative_profit_days(profits):
    cumulative_profit = 0
    flag_days = []
    
    for i, prft in enumerate(profits):
        cumulative_profit += prft
        if cumulative_profit <0:
            flag_days.append(i)
            
    return flag_days
    
# print(get_negative_profit_days([200, -500, 300, -100, -50]))


"""
style Scenario:
As part of a Google Search analysis tool, 
you're asked to analyze the daily increase in the number of queries. 
Find out if any subarray of consecutive days has a total increase equal to a given target.

search_counts = [2, 1, 3, 4, 1]
target = 8
Subarrays that sum to 8: [3, 4, 1], [1, 3, 4]

Return True if any subarray sum equals target.
"""

def is_any_subarry_sum_equal_k(arr,k):
    hash_pref_sum_freq = {0:1}
    curr_sum = 0
    for i,num in enumerate(arr):
        curr_sum += num
        if curr_sum - k in hash_pref_sum_freq:
            return True
        hash_pref_sum_freq[curr_sum] = i
    return False
        
# print(is_any_subarry_sum_equal_k([3,3,-15,1,2,2, 1, 3, 4, 1],-11))


"""
You're working on Google Fit. 
A user tracks daily calorie intake in an array. 
We want to find how many continuous periods exist where their calorie intake added up exactly to a goal k.
Your team wants to show how often users meet their calorie goals exactly using continuous meal streaks.

calories = [1, 2, 3]
k = 3

Subarrays that sum to 3:
- [1,2]
- [3]

Return: 2
"""

def count_subarray_sum_eqauls_k(nums, k):
    """
    Approach 1 get all sub arrays , check sum of each subarray == k, increase count
    O(n^2) solution
    
    Lets make use of prefix sum
    I need to find number of days where this k was acheived
    """
    
    pref_sum_freq_map = {0:1}
    
    count = 0
    curr_sum = 0
    for i, num in enumerate(nums):
        curr_sum += num
        if curr_sum - k in pref_sum_freq_map:
            count += pref_sum_freq_map[curr_sum - k]
        pref_sum_freq_map[curr_sum] = pref_sum_freq_map.get(curr_sum,0) + 1
    return count
        
# print(count_subarray_sum_eqauls_k([1, 2, -2,-1,2,0,3,-1,2,-1,2], 0))
print("this one")
print(count_subarray_sum_eqauls_k([1,-1,3,2,1,-2,5,-4], 5))
        
"""
You're working on YouTube Analytics. 
Your team is analyzing viewer drop-off patterns.

Each video is split into equal-length sections, 
and the list views = [+1, -1, +1, -1, ...] 
represents whether the view count increased (+1) or 
decreased (-1) compared to the previous section.

You want to identify how many sub-periods 
(i.e., continuous segments of this list) had equal number of +1s and -1s. 
This helps detect balanced engagement segments.

views = [1, -1, 1, -1]
→ Subarrays:
[1,-1], [1,-1,1,-1], [-1,1], [1,-1]

Return: 4

"""        


def count_balanced_engagement_periods(views: List[int]) -> int:
    """
    Since this views only have +1 and -1 , if at any point I find sum is 0
    I will find a segment that has equal +1 and -1.
    """
    pref_sum_freq_map = {0:1}
    count = 0
    curr_sum = 0
    for i,view in enumerate(views):
        curr_sum += view
        # curr_sum - k:  curr_sum - 0 --> curr_sum
        if curr_sum in pref_sum_freq_map:
            count += pref_sum_freq_map[curr_sum]
        pref_sum_freq_map[curr_sum] = pref_sum_freq_map.get(curr_sum,0) + 1
    return count
# print(count_balanced_engagement_periods([1, -1, 1, -1,1,-1]))


"""
Contiguous Array
Given a binary array nums, return the maximum length of a contiguous subarray 
with an equal number of 0 and 1.

Example 1:

Input: nums = [2,1]
Output: 2
Explanation: [2, 1] is the longest contiguous subarray with an equal number of 2 and 1.
Input: nums = [2,1,1,1,1,1,2,2,2]
Output: 6
Explanation: [1,1,1,0,0,0] 
"""


def findMaxLength(nums: List[int]) -> int:
    """
    TC: O(n)
    SC: O(n)
    
    I will try to make this problem same as the above one and solve it
    convert all zeros to -1
    """
    
    for i,num in enumerate(nums): #O(n)
        if num == 0:
            nums[i] = -1
    # target=0
    pref_sum_ind_map = {}
    max_arr_len = 0
    curr_sum = 0
    
    for i,num in enumerate(nums): # O(n)
        curr_sum += num
        if curr_sum == 0:
            max_arr_len = max(i+1, max_arr_len)
        # curr_sum - k:  curr_sum - 0 --> curr_sum
        if curr_sum in pref_sum_ind_map:
            max_arr_len = max(max_arr_len, i - pref_sum_ind_map[curr_sum] )
        
        if curr_sum not in pref_sum_ind_map:
            pref_sum_ind_map[curr_sum] = i
            
    return max_arr_len
        
print(findMaxLength([0,0,1,1,1,1,1,0,0,0,0,1]))
        

def findMaxLength(nums: List[int]) -> int:
    """
    TC: O(n)
    SC: O(n)
    
    I will try to make this problem same as the above one and solve it
    convert all zeros to 1
    """

    target=0
    pref_counter_freq_map = {}
    max_arr_len = 0
    curr_couter = 0
    
    for i,num in enumerate(nums): # O(n)
        if num == 1:
            curr_couter += 1
        else:
            curr_couter -= 1
        
        if curr_couter == target:
            max_arr_len = max(i+1, max_arr_len)

        # curr_sum - k:  curr_sum - 0 --> curr_sum
        if curr_couter in pref_counter_freq_map:
            max_arr_len = max(max_arr_len, i - pref_counter_freq_map[curr_couter] )
        
        if curr_couter not in pref_counter_freq_map:
            pref_counter_freq_map[curr_couter] = i
            
    return max_arr_len

print(findMaxLength([0,0,1,1,1,1,1,0,0,0,0,1]))