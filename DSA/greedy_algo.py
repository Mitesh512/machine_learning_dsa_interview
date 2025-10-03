from typing import Optional,List
"""
Greedy algorithms build up a solution step-by-step, 
always choosing the locally optimal option at each step — hoping it leads to a globally optimal solution.
Key Insight: No backtracking or exploring all combinations. Just make the best immediate decision and move forward.

1. Interval Scheduling / Merge Intervals
    Key idea: Sort by start or end times.
    Used in: Meeting Rooms, Merge Intervals, Minimum Platforms
    Greedy Rule: Pick the next earliest-ending interval to maximize usage.

2. Resource Allocation / Task Assignment
    Key idea: Sort both arrays, then match lowest-cost pairings.
    Used in: Assign Cookies, Job Scheduling
    Greedy Rule: Assign smallest available resource to the smallest requirement.

3. Min/Max Operations
    Key idea: Minimize/maximize result by always choosing extreme values.
    Used in: Jump Game, Candy Distribution
    Greedy Rule: Take largest/smallest value that satisfies constraints.

4. Priority Queue Greedy
    Key idea: Always process the task with the highest priority (based on custom comparator).
    Used in: Huffman Encoding, Meeting Rooms II, Platform Allocation
    Greedy Rule: Use min/max-heap to simulate greedy decision-making.

5. Greedy with Stack
    Key idea: Use stack to maintain valid state while processing in order.
    Used in: Valid Parentheses, Remove K Digits, Monotonic Stack Problems
    Greedy Rule: Pop from stack when current char makes solution better.

| Pattern        | Problem                                                                                                                | LC #     | Notes                            |
| -------------- | ---------------------------------------------------------------------------------------------------------------------- | -------- | -------------------------------- |
| Intervals      | [Merge Intervals](https://leetcode.com/problems/merge-intervals)                                                       | 56       | Sort + merge overlapping         |
| Intervals      | [Meeting Rooms I & II](https://leetcode.com/problems/meeting-rooms-ii)                                                 | 252, 253 | Track overlaps using heap        |
| Resource Match | [Assign Cookies](https://leetcode.com/problems/assign-cookies)                                                         | 455      | Sort and two pointers            |
| Resource Match | [Task Scheduler](https://leetcode.com/problems/task-scheduler)                                                         | 621      | Greedy + Counting                |
| Min Platform   | [Minimum Platforms (GFG)](https://practice.geeksforgeeks.org/problems/minimum-platforms)                               | -        | Sort arrival/departure, use heap |
| Parentheses    | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses)                                                   | 20       | Stack-based greedy               |
| Stack-Greedy   | [Remove K Digits](https://leetcode.com/problems/remove-k-digits)                                                       | 402      | Monotonic Stack                  |
| Optimization   | [Jump Game](https://leetcode.com/problems/jump-game)                                                                   | 55       | Track farthest reachable         |
| Optimization   | [Candy](https://leetcode.com/problems/candy)                                                                           | 135      | Two-pass greedy                  |
| Scheduling     | [Minimum Number of Arrows to Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons) | 452      | Greedy end time                  |
| Huffman        | [Huffman Coding (GFG)](https://practice.geeksforgeeks.org/problems/huffman-encoding)                                   | -        | Greedy + Min Heap                |

"""

"""
Key Concept for sorting in intervals
| Problem Goal                                    | Sort By        | Why                                     |
| ----------------------------------------------- | -------------- | --------------------------------------- |
| Timeline-based simulation (allocation, merging) | **Start Time** | You want to process events as they come |
| Maximize number of events, minimize resources   | **End Time**   | Early finish → more room for future     |




"""
class Solution:
    def merge(self, intervals):
        """
        sort intervals by start time
        why?
        If we sort the intervals based on their start times, any overlapping intervals will be placed next to each other in the list.
To merge intervals, we only need to track the end time since the sorted order ensures that the next interval's start time is always greater than or equal to the current interval's start time.
        """
        intervals.sort(key=lambda x:x[0])
        # print(intervals)
        non_overlapping_intervals = []
        curr_start = intervals[0][0]
        curr_end = intervals[0][1]
        for start,end in intervals[1:]:
            # print("curr_start,curr_end",curr_start,curr_end)
            # print(start,end)
            if start <= curr_end:
                if end > curr_end:
                    curr_end = end
            else:
                # this looks new interval
                # add curr interval and start new
                non_overlapping_intervals.append([curr_start,curr_end])
                curr_start = start
                curr_end = end
        non_overlapping_intervals.append([curr_start,curr_end])
        return non_overlapping_intervals


"""
252. Meeting Rooms
Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.
Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: false
Example 2:

Input: intervals = [[7,10],[2,4]]
Output: true
"""
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # finding number of overlapping intervals can help us solve this
        if len(intervals) ==0:
            return True
        
        # sort by start time
        intervals.sort(key=lambda x:x[0])
        

        curr_end = intervals[0][1]

        for start, end in intervals[1:]:
            if start < curr_end:
                return False
            else:
                curr_end = end
        return True


"""
Meeting Room 2
253. Meeting Rooms II
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
Example 2:

Input: intervals = [[7,10],[2,4]]
Output: 1

intervals = [[0, 30],[5, 10],[15, 20],[25, 35],[5, 15],[10, 40],[35, 50],[40, 45]]
output: 3

intervals: [[1,3],[7,8],[1,8],[2,10],[12,66],[15,18]]
output: 3
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if len(intervals) ==0:
            # no meeting rooms are required
            return 0

        # sorting by start time
        intervals.sort(key=lambda x:x[0])

        # maintaining rooms using min heap
        min_heap = []
        # starting the first meeting
        heapq.heappush(min_heap,intervals[0][1])

        max_meeting_rooms = 1
        for start,end in intervals[1:]:
            # smallest end
            if start >= min_heap[0]:
                # I can use the same room, remove the old min time of this meeting room
                # and add the new end 
                heapq.heappop(min_heap)
                heapq.heappush(min_heap,end)
            else:
                # start time is less then the previous meeting so I need to book a new room
                heapq.heappush(min_heap,end)
                max_meeting_rooms = max(max_meeting_rooms, len(min_heap))
        
        return max_meeting_rooms


"""
Minimum number of arrows to burst the balloons

points =
[[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]]
ans = 2
"""
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        """
        To Burst the Number of Balloons I need to find the intervals, which are voerlapping
        sort them by start time
        
        """
        if len(points)==0:
            return 0
        points.sort(key= lambda x:x[0])
        # once I have sorted balloons by their start node I need to find the overalpping area only
    
        # [1,5] and [2,6], overlapping will be [2,5]
        # [1,5] and [6,9] no overlapping you need to shoot to arrows

        # I know if I want to burst all Balloon I can always use n arrows for each ballon and I am done
        # But if i find any number of ballonns which are overlaping I can reduce the arrows I will shoot
        n = len(points)
        arrows_to_shoot = n

        current_overlap = []

        for start , end in points:
            # print(current_overlap)
            # I can update intervals when there is overlap
            if current_overlap and start <= current_overlap[1]:
                # I can reduce the number of arrows I have foudn the overlappign ballons
                arrows_to_shoot -= 1
                # Now I need to update the overlapping section
                overlap_start = max(start,current_overlap[0])
                overlap_end = min(end,current_overlap[1])
                current_overlap = [overlap_start,overlap_end]
            else:
                # there is no overlap with the previous one
                # so update the current overlap with new section
                current_overlap = [start,end]
        return arrows_to_shoot
        
"""
Assign Cookies:

Assume you are an awesome parent and want to give your children some cookies. 
But, you should give each child at most one cookie.

Each child i has a greed factor g[i], 
which is the minimum size of a cookie that the child will be content with;
and each cookie j has a size s[j]. If s[j] >= g[i], 
we can assign the cookie j to the child i, and the child i will be content. 
Your goal is to maximize the number of your content children and output the maximum number.

"""
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g_sorted = sorted(g)
        s_sorted = sorted(s)
        g_len = len(g)
        s_len= len(s)
        g_ind = 0
        s_ind = 0

        while s_ind < s_len:
            
            if g_sorted[g_ind] <= s_sorted[s_ind]:
                g_ind +=  1
            
            if g_ind >= g_len:
                break

            s_ind += 1
        
        return g_ind


        








import heapq
min_heap = []
max_heap = []
for ele in [5,45,2,34,1,2,3,4,51,2]:
    heapq.heappush(min_heap,ele)
    heapq.heappush(max_heap,-ele)
    
    print(min_heap[0], -max_heap[0])
    

arr = [[1,3],[7,8],[1,8],[2,10],[12,66],[15,18]]
print(arr)
arr.sort(key= lambda x:x[1])
print(arr)
arr.sort(key=lambda x:x[0])
print(arr)