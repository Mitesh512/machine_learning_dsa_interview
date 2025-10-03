class Solution:
    def generate_expression(self,curr_ind,exp, exp_val, prev_val, n, num, target, result):
        """
        why prev_val is needed:
        2 ,3 ,4
        2 + 3 + 4 ---> 2+3, 5 + 4 =>2+3+4, 9
        4-2 * 3 = 2*3 ---> 2 -(-2) = 4
        2 + 3 * 4 ---> 2+3, 5 * 4 =>2+3*4, 20 ---> (5-prev_val)2 + prev_val * 4 --> 2 + 3 * 4 --- > 2 + 12  
        2 + 3 * 4 * 4 ---> prev_val (3*4) , curr_num 4, exp = 2 + 3 * 4, exp_val = 14
        14 - 12 + 12 * 4 =    2+48 = 50        
        """
        ## Base Condition
        if curr_ind ==n:
            if exp_val == target:
                result.append("".join(exp))
            return result
        
        # Now we will iterate for all possible numbers from curre index
        # 1203 : 1 , 12 , 120 ,1203

        for i in range(curr_ind, n):
            # 1 + , * , -
            # 1 2 3 0
            # 1
            #   rec(2)
            #.  rec(23)
            #.  rec(230)

            # 2 + 3 + 
            
            # 0 4 5
            # 0
            # 04


            curr_str = num[curr_ind:i+1]
            curr_num = int(curr_str)

            # if we are just starting then there won't be any other expression 1203
            if curr_ind == 0:
                #                                ,curr_ind,exp, exp_val, prev_val, n, num, target, result
                #                                   1, ["1"] ,      1,       1                      []
                result = self.generate_expression(i+1,exp + [curr_str], curr_num , curr_num, n, num, target, result)
            
            else:
                # + operation
                result = self.generate_expression(i+1 ,exp + ["+"] + [curr_str] , exp_val + curr_num, curr_num, n, num, target, result)
                # - operation
                result = self.generate_expression(i+1 ,exp + ["-"] + [curr_str], exp_val - curr_num, -curr_num, n, num, target, result)
                # * operation
                result = self.generate_expression(i+1, exp + ["*"] + [curr_str] , exp_val - prev_val + prev_val * curr_num, prev_val * curr_num, n, num, target, result)
            
            # break the iteration for leading zero value
            if curr_num == 0:
                break
        
        return result


    def addOperators(self, num , target):
        """
        what do I have a num string and target
        1203 target 6
        what operations I can perform
        +
        -
        *

        No leading zeros allowed
        I can use it like as numbers for operations
        1 
        12
        120
        1203

        1 2 0 3

        0*3
        0+3

        but 03 can not be used
        """

        n = len(num)
        possible_expression = self.generate_expression(0,[], 0, 0, n, num, target, [])

        return possible_expression




def find_expression(num_list, target):
    n = len(num_list)
    result = []

    def rec(ind, expr):
        if ind == n:
            try:
                if eval(expr) == target:
                    result.append(expr)
            except Exception:
                pass
            return

        curr_str = str(num_list[ind])

        if ind == 0:
            rec(ind + 1, curr_str)
        else:
            # Plain addition
            rec(ind + 1, expr + "+" + curr_str)

            # Plain multiplication
            rec(ind + 1, expr + "*" + curr_str)

            if len(expr) > 2:
                # Wrap previous expression in parentheses and multiply
                rec(ind + 1, f"({expr})*{curr_str}")

                # Wrap previous expression in parentheses and add
                rec(ind + 1, f"({expr})+{curr_str}")

    rec(0, "")
    return result







# # Test cases
print(find_expression([2, 3, 4], 20))  # Expected: ['(2+3)*4']
print(find_expression([2, 3, 4], 14))  # Expected: ['2+(3*4)']
numbers = [2, 3, 4, 1, 2, 3, 1]
for target in [24, 16, 14, 24, 26, 9, 8, 10]:
    print(numbers, target, "--->", find_expression(numbers, target))















# # Merge Sort 
# """
# This is divide and conquer algorithm
# It has two parts divide and conquer

# Divide is a recursive algorithm
# While conquer is subpart that merges two sorted lists
# so we can create two functions 
# 1. divides the arrays
# 2. merges the arrays
# [3,1,2,7,4,5,2] --->n =7
# l = 0
# r = n -1 =7 -1 =6
# mid = l+r //2 = 0+6//2 = 3

# """

# def conquer(l_arr,r_arr):
#     p1 = 0
#     p2 = 0
#     sorted_arr = []
#     while p1< len(l_arr) and p2 < len(r_arr):
#         if l_arr[p1] < r_arr[p2]:
#             sorted_arr.append(l_arr[p1])
#             p1+=1
        
#         else:
#             sorted_arr.append(r_arr[p2])
#             p2+=1
    
#     while p1< len(l_arr):
#         sorted_arr.append(l_arr[p1])
#         p1+=1
#     while p2<len(r_arr):
#         sorted_arr.append(r_arr[p2])
#         p2+=1
        
#     return sorted_arr
    
# def merge(arr,left,right):
#     if left == right:
#         return [arr[left]]

#     mid = (left + right) //2 # 3
    
#     l_arr = merge(arr,left,mid) #[3,1,2,7] --> mid 2 -->[3,1] --> mid =0 -->[3]
#                                                                             #[1] 
#                                                   # -->[2,7]--> mid = 0 --> [2]
#                                                                         # -->[7]
#     r_arr = merge(arr,mid+1,right) # [4,5,2]-->mid 1 --> [4,5] --> [4]
#                                                               #--> [5]
#                                                 # -->[2] 
    
#     sorted_arr = conquer(l_arr,r_arr)
#     return sorted_arr
    


# def merge_sort(arr):
#     sorted_arr = merge(arr,0,len(arr)-1)
#     return sorted_arr
    
    
# arr = [90123,1234,234,45,3213,0,0,0,0,0,0,-12,-3,1,2,7,4,5,2]

# sorted_arr = merge_sort(arr)
# print(arr, "--->", sorted_arr)