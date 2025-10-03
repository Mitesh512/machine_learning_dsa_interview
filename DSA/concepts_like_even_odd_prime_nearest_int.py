

def avg(arr):
    # for arrays we don't have avg inbuild funciton we have to get avg
    return sum(arr)/len(arr)

def get_nearest_int(n):
    """
    This function takes an integer n and returns the nearest integer to n.
    If n is already an integer, it returns n.
    """
    if isinstance(n, int):
        return n
    else:
        return round(n)


def sorting_an_array(arr):
    """
    This function takes an array and sorts it in ascending order.
    It uses the built-in sorted() function to sort the array.
    """
    
    return sorted(arr)

# sorting based on internal list
arr = [[1,3],[7,8],[1,8],[2,10],[12,66],[15,18]]
print(arr)
arr.sort(key= lambda x:x[1])
print(arr)
arr.sort(key=lambda x:x[0])
print(arr)


if __name__ == "__main__":
    # test_nearest_int = [4.5, 4.6, 4, -2.8, -2.3, -2.5]
    # for num in test_nearest_int:
    #     print(f"Nearest integer to {num} is {get_nearest_int(num)}")
        
    
    # arr = [4, 2, 5, 1, 3]
    # # Inplace soring
    # print(arr.sort())
    # print(arr)
    # sorted_arr = sorting_an_array(arr)
    # print(f"Sorted array: {sorted_arr}")
    
    
    
    import sys

    my_list = [23129344* 23129344* 23129344, 2, 3]

    print("---"*100)
    
    print("Memory address of list:", id(my_list))
    print("Memory addresses of elements:", [id(x) for x in my_list])
    print("Initial memory:", sys.getsizeof(my_list))  # 88 bytes (56 overhead + 32 pointers (8*4))
    print("Initial memory of the element:", sys.getsizeof(my_list[0])) 
    my_list.append(4)
    print("Memory address of list:", id(my_list))
    print("Memory addresses of elements:", [id(x) for x in my_list])
    print("Memory allocation After append 4:", sys.getsizeof(my_list))  # 88 bytes (still fits)
    my_list.append(5)
    print("Memory address of list:", id(my_list))
    print("Memory addresses of elements:", [id(x) for x in my_list])
    print("Memory allocation After append 5:", sys.getsizeof(my_list))  # 120 bytes (56 + 64 (16*4), capacity 8)
    my_list+=[1,2,3,4]
    print("Memory address of list:", id(my_list))
    print("Memory addresses of elements:", [id(x) for x in my_list])
    print("Memory allocation After adding [1,2,3,4]:", sys.getsizeof(my_list))  # 184 bytes (56 + 128 (32*4) , capacity 8)
            
    
    
