"""
Classic Binary Search (Find element in sorted array)
➤ Condition: nums[mid] == target

Lower Bound (First True / Smallest value that satisfies a condition)
➤ Think: What is the minimum value such that condition becomes true?

Upper Bound (Last True / Largest value that satisfies a condition)
➤ Think: What is the maximum value such that condition remains true?



Let's say you're trying to find the first day you can cross a flooded field:
lower bound: First day where crossing is possible (First True in [False, False, False, True, True])
upper bound: Last day where crossing is not possible (Last False in [False, False, False, True, True])

"""


def lower_bound(arr,target):
    """
    lb ===> smallest ind such that arr[ind] >= target
    arr = [3,5,5,8,10,29,40]
           0 1 2 3  4  5 6 
    target val : 5 10 9  28 4 3
    lower bound: 1 4  4  5  1 0
    """
    n = len(arr)
    l = 0
    r = n-1 
    # if there is no answer that means there will be lower boudn outside of the arr
    lb = n
    while l<=r:
        mid = int(r - (r-l)/2)
        if arr[mid] >= target:
            lb = mid
            r = mid - 1
        else:
            l = mid+1
    return lb

# for t in [5, 10, 9,  28, 4, 3]:
#     print(lower_bound([3,5,5,8,10,29,40],t))
    
            

def upper_bound(arr,target):
                
    """
    Upper Bound: smallest ind such that arr[ind] > target
    arr = [3,5,5,8,10,29,40]
            0 1 2 3  4  5 6 
    target val : 5 10 9  28 4 3
    lower bound: 3 4  4  5  1 0
    """
    n = len(arr)
    l = 0
    r = n-1
    while l<=r:
        mid = int(r-(r-l)/2)
        if arr[mid]>target:
            r = mid -1
        else:
            l = mid + 1
    return l

for t in [5, 10, 9,  28, 4, 3]:
    print(upper_bound([3,5,5,8,10,29,40],t))


"""
painter partition or split array largest sum
"""