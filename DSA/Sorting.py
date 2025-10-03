
def bubble_sort(arr, ascending=True):
    """
    Theroy: Bubble Sort
    Psuedo code:
    1. Start from the first element of the array.
    2. Compare the current element with the next element.
    3. If the current element is greater than the next element, swap them.
    4. Move to the next element and repeat the process until the end of the array.
    5. Repeat the process for the entire array until no swaps are needed.
    Time Complexity:
    Best Case: O(n) (when array is already sorted, with flag optimization).

    Average Case: O(n²) (multiple passes with comparisons and swaps).

    Worst Case: O(n²) (when array is reverse sorted).

    Space Complexity: O(1) (in-place, only uses a constant amount of extra space).


    """
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n-i-1):
            if ascending:
                if arr[j]>arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1] , arr[j]
                    swapped = True
            else:
                if arr[j]<arr[j+1]:
                    arr[j],arr[j+1] = arr[j+1], arr[j]
                    swapped = True
                    
        if swapped == False:
            break
    return arr


def selection_sort(arr):
    """
    Theory: Selection Sort
    Psuedo code:
    1. Start from the first element of the array.
    2. Find the minimum element in the unsorted part of the array.
    3. Swap it with the first element of the unsorted part.
    4. Move to the next element and repeat the process until the entire array is sorted.
    Time Complexity:
    Best Case: O(n²) (no optimization).

    Average Case: O(n²) (multiple passes with comparisons).

    Worst Case: O(n²) (when array is reverse sorted).

    Space Complexity: O(1) (in-place, only uses a constant amount of extra space).
    """
    
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[i]:
                min_index =j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr            

# insertion sort
def insertion_sort(arr):
    """
    Theory: Insertion Sort
    Psuedo code:
    1. Start from the second element of the array.
    2. Compare it with the elements before it.
    3. Shift all larger elements to the right.
    4. Insert the current element in its correct position.
    5. Repeat the process for all elements in the array.
    Time Complexity:
    Best Case: O(n) (when array is already sorted).

    Average Case: O(n²) (multiple passes with comparisons and shifts).

    Worst Case: O(n²) (when array is reverse sorted).

    Space Complexity: O(1) (in-place, only uses a constant amount of extra space).
    """
    

def quick_sort(arr):
    """
    Theory: Quick Sort
    Psuedo code:
    1. Choose a pivot element from the array.
    2. Partition the array into two sub-arrays:
        - Elements less than the pivot.
        - Elements greater than the pivot.
    3. Recursively apply the same process to the sub-arrays.
    Time Complexity:
    Best Case: O(n log n) (when pivot divides array evenly).

    Average Case: O(n log n) (random pivot selection).

    Worst Case: O(n²) (when array is already sorted or reverse sorted).

    Space Complexity: O(log n) (due to recursion stack).
    """
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr)//2]
        return quick_sort([x for x in arr if x< pivot]) + [x for x in arr if x == pivot] + quick_sort([x for x in arr if x> pivot])


class mergeSort:
    """
    [64,    34,     25,     12,     22, 11, 90] 
    
    given a array first I divide the array from its middle till it has only 1 element 
    
    left:  0 0 0 0      1         2
    right: 6 3 1 0      1         3
    mid:   3 1 0 return return    2
    
    """
    def __init__(self, arr):
        self.arr = arr
    
    def merge_sort(self):
        left = 0
        right = len(self.arr) -1
        self.divide(left, right)
        
        
        
    def divide(self,left, right):
        if left >= right:
            return

        mid = (left + right) //2 # I am taking floor value of division
        # Now divide the left array
        self.divide(left, mid)
        self.divide(mid+1, right)
        
        self.conquer(left,mid,right)
        
    
    def conquer(self,left,mid,right):
        
        """
        Basically the job here is to merge two soted arrays 
        we already know that 
        (left to mid ) and (mid+1 to right )
        are sorted
        """
        p1 = left
        p2 = mid+1
        p = 0
        temp = [0 for i in range(left, right+1)]
        
        while p1 < mid +1 and p2 <= right:
            if self.arr[p1] < self.arr[p2]:
                temp[p] = self.arr[p1]
                p1 +=1
            else:
                temp[p] = self.arr[p2]
                p2 += 1
            p+=1
        
        while p1 < mid +1:
            temp[p] = self.arr[p1]
            p1 +=1
            p += 1
        
        while p2 <= right:
            temp[p] = self.arr[p2]
            p2 += 1
            p += 1
            
        for i in range(len(temp)):
            self.arr[left+i] = temp[i]
        
            
            
        
        

if __name__ == "__main__":

    
    # 5 test cases list:
    # 1. Random order
    # 2. Already sorted
    # 3. Reverse order
    # 4. All elements the same
    # 5. Large numbers
    test_cases = [
        [64, 34, 25, 12, 22, 11, 90],  # Random order
        [1, 2, 3, 4, 5],              # Already sorted
        [5, 4, 3, 2, 1],              # Reverse order
        [7, 7, 7, 7],                  # All elements the same
        [1000000, 999999, 888888]      # Large numbers
    ]
    for i, arr in enumerate(test_cases):
        # Bubble Sort
        # bubble_sorted = bubble_sort(arr.copy(),ascending=False)
        # print("Bubble Sorted array:", bubble_sorted)

        # # Selection Sort
        # selection_sorted = selection_sort(arr.copy())
        # print("Selection Sorted array:", selection_sorted)

        # # Insertion Sort
        # insertion_sorted = insertion_sort(arr.copy())
        # print("Insertion Sorted array:", insertion_sorted)

        # # Merge Sort

        arr_copy = arr.copy()
        obj = mergeSort(arr_copy)
        obj.merge_sort()
        print(arr, " --> Merge Sorted array: --->", obj.arr)

        
        # # Quick Sort
        # quick_sorted = quick_sort(arr.copy())
        # print(arr, " --> Quick Sorted array: --> ", quick_sorted)

