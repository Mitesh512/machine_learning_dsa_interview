# Generate all subarrays
# given an array and string
# O(N²) substrings total (approximately N*(N+1)/2)
s = "abc"
n = len(s)
substrings = []

for i in range(n):        # start index
    for j in range(i+1, n+1):  # end index (exclusive)
        substrings.append(s[i:j])

print(substrings)


## Generate all subsequences:
"""
A subsequence is a sequence that can be derived by deleting some (or no) characters, without changing the order of remaining characters.
Example for "abc":
Subsequences = ["", "a", "b", "c", "ab", "ac", "bc", "abc"]

Number of subsequences | 2ⁿ         
Time Complexity        | O(2ⁿ)      
Space Complexity       | O(2ⁿ x N)  
(because each subsequence can be of length up to N)
"""
def generate_subsequences(s):
    result = []
    
    def backtrack(index, path):
        if index == len(s):
            result.append(path)
            return
        
        # Include current character
        backtrack(index + 1, path + s[index])
        
        # Exclude current character
        backtrack(index + 1, path)
    
    backtrack(0, "")
    return result

# Test
s = "abc"
subsequences = generate_subsequences(s)
print(subsequences)


### Univeral template for recursion, backtracking, 
"""
| Step                       | Meaning                        |
| :------------------------- | :----------------------------- |
| **path.append(...)**       | Make a choice: include element |
| **solve(index + 1, path)** | Move forward with choice       |
| **path.pop()**             | Backtrack: undo the choice     |
| **solve(index + 1, path)** | Try excluding that element     |

"""
def solve(index, path):
    # Base case: reached end of input
    if index == len(input_data):
        # Do something with the current path
        result.append(path[:])   # or process path
        return
    
    # Step 1: Include the current element
    path.append(input_data[index])
    solve(index + 1, path)
    
    # Step 2: Exclude the current element (backtrack)
    path.pop()
    solve(index + 1, path)

# Driver code
input_data = [1, 2, 3]  # Can be string, array, etc.
result = []
solve(0, [])
print(result)
