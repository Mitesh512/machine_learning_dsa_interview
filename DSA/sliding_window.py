# fixed size sliding window:
def maximum_sum_of_k_elements_in_arr(arr,k):
    window_sum = sum(arr[:k])
    max_sum = window_sum
    n = len(arr)
    for i in range(k, n): 
        window_sum += arr[i] - arr[i-k]
        if window_sum > max_sum:
            max_sum = window_sum
    return max_sum
    
# arr = [1,2,34,4,5,6,3,2,34,5, 1,7, 3, 4] 
#        0 1 2  3 4 5 6 7 8  9 10 11 12 13

# print(maximum_sum_of_k_elements_in_arr(arr,4))

"""
Easy Problem 1: Analyzing Sensor Data (Fixed-Size Window - Array)
Scenario: You're part of a team at Google building an internal health monitoring dashboard for data center servers.
Each server sends a temperature reading every second. You're given a list of temperature readings taken over several seconds.
To analyze stability, your task is to find the highest average temperature over any continuous window of exactly k seconds.

✨ Inputs:
readings: List of integers representing temperatures.

k: Integer, size of the time window.

🔍 Goal:
Return the maximum average temperature over any subarray of size k.
# Input: readings = [1, 3, 2, 6, -1, 4, 1, 8, 2], k = 5
# Output: 3.6
"""

def get_avg_of_k_readings(readings,k):
    # TC O(n), SC O(1)
    n = len(readings)
    if k>n:
        return sum(readings)/k
    curr_k_sum = sum(readings[:k])
    max_avg = curr_k_sum/k
    for i in range(k,n):
        curr_k_sum += readings[i] - readings[i-k]
        curr_avg = curr_k_sum /k 
        if curr_avg > max_avg:
            max_avg = curr_avg
    return max_avg
        
readings = [1, 3, 2, 6, -1, 4, 1, 8, 2]
k = 5
# print(get_avg_of_k_readings(readings,k))
# Output: 3.6
"""
Easy Problem 2: Longest Good Signal (Variable-Size Window - String)
Scenario: You're working on a Google Maps feature that decodes a binary signal sent by roadside sensors. 
Each character in the signal string is either '1' (good signal) or '0' (dropped signal).

Your goal is to identify the longest continuous stretch of strong signal (i.e., '1') — 
but you're allowed to tolerate at most one '0' during a poor connection.

📌 In short:
Find the length of the longest substring that contains only '1' and at most one '0'.

Input: signal = "11011101111"
Output: 8
"""

def find_largest_good_signal(signal):
    zero_cnt = 0
    l = 0
    r = 0
    n = len(signal)
    longest_good_signal = 0
    while r<n:
        if signal[r] == "0":
            zero_cnt +=1
        if zero_cnt <= 1:
            longest_good_signal = max(longest_good_signal, r-l+1)
        else:
            while zero_cnt >1:
                if signal[l] == "0":
                    zero_cnt -= 1
                l += 1
        r+= 1
    return longest_good_signal

# print(find_largest_good_signal("11111111011101111"))



"""
Easy Problem 3: Secret Message Scanner (Fixed-Size Window - Anagram Check in String)
Scenario: Imagine you're helping the Gmail security team. A user has flagged a suspicious email, 
and you're scanning the email's text to detect hidden codes (anagrams of known secret keywords).

You're given a text string and a pattern string. Your task is to find how many substrings in the text are anagrams of the pattern.

✨ Input:
text: a string that may contain lowercase English letters.

pattern: a string of lowercase letters.

📌 A substring is an anagram of pattern if it contains the same characters in any order, with exact frequency.

Input: text = "cbaebabacd", pattern = "abc"
Output: 2
Explanation: "cba" and "bac" are anagrams of "abc".

Input: text = "abab", pattern = "ab"
Output: 3
Explanation: "ab", "ba", and "ab" are all valid anagrams.
"""


def find_valid_patterns(text,pattern):
    """
    Conquere and Shrink based on some conditions.
    TC O(n) + O(k) + O(n.k)
    SC O(n)
    """
    n = len(text)
    k = len(pattern)
    
    if k > n:
        return 0

    ptrn_map = {}
    for c in pattern:
        ptrn_map[c] = ptrn_map.get(c,0) + 1
    
    wind_text_map = {}
    # go only till k
    for c in text[:k]:
        wind_text_map[c] = wind_text_map.get(c,0) + 1
        
    pattern_anagram_count = 0
    
    if ptrn_map == wind_text_map:
        pattern_anagram_count += 1
    
    for i in range(k,n):
        # remove the left char
        left_chr = text[i-k]
        wind_text_map[left_chr] -= 1
        if wind_text_map[left_chr] == 0:
            del  wind_text_map[left_chr]
        
        # add the new char
        right_chr = text[i]
        wind_text_map[right_chr] = wind_text_map.get(right_chr,0) + 1
        
        if ptrn_map == wind_text_map:
            pattern_anagram_count += 1
    return pattern_anagram_count
            
# texts = ["abcabcabcabacbabacd", "abab", "abcdefg"]
# patterns = ["abc","ab","xyz"]
# for text, pattern in zip(texts,patterns):
#     print("text, pattern : ", text, pattern )
#     print(find_valid_patterns(text,pattern))

"""
problem 1: Find all substrings of length k in a string
Goal: Given a string s and an integer k, return all substrings of length k.

📌 Example
s = "abcdefg", k = 3
→ Output: ["abc", "bcd", "cde", "def", "efg"]

This teaches basic sliding window on fixed size.
"""
def get_all_substring_of_len_k(s,k):
    if k > len(s):
        return []
    all_substring = []    
    
    for i in range(len(s)-k+1):
        curr_substring = s[i:i+k]
        all_substring.append(curr_substring)
        print(curr_substring)
    
    return all_substring
        
# print(get_all_substring_of_len_k(s = "abcdefg", k = 3))



def count_word_occurrences(s: str, word: str) -> int:
    """
    Problem: Count how many times a given word appears in a string s.
    """
    n = len(s)
    k = len(word)
    if n<k:
        return 0
    word_freq = 0
    for i in range(n-k+1):
        curr_word = s[i:i+k]
        if curr_word == word:
            word_freq += 1
    
    return word_freq

# s = "barfoofoobarbar"
# word = "bar"
# print(count_word_occurrences(s, word))

def get_all_word_freq(s,words):
    """
    Problem: Given a list of words (all same length), and a string s, 
    count how many individual word matches appear in s.
    """
    n = len(s)
    k = len(words[0])
    if n < k:
        return {}
    words_freq = {word:0 for word in words}
    for i in range(n-k+1):
        curr_word = s[i:i+k]
        if curr_word in words_freq:
            words_freq[curr_word] += 1
    return words_freq
# s = "barfoofoobarbar"
# words = ["bar", "foo", "baz"]
# print(get_all_word_freq(s,words))


def detect_consecutive_substrings(s,words):
    """
    Detect a group of len(words) consecutive substrings that form a
    valid concatenation
    
    Problem: Given string s, and list of words, 
    check for each window of total length k * len(words), 
    if it's a valid permutation of all words.
    
    s = "barfoofoobarthe"
    words = ["bar", "foo", "the"]

    """
    n = len(s)
    k = len(words[0])
    substr_len = len(words) * k
    if n<k:
        return 0    
    word_freq = {}
    for word in words:
        word_freq[word] = word_freq.get(word,0)  + 1
        
    consecutive_substrings_for_all_words = []
    consecutive_substrings_for_all_words_indices = []  # Instead of s[i:i+substr_len]

    for i in range(n-substr_len+1):
        curr_word = s[i:i+k]
        if curr_word in word_freq:
            # this means the we can check the full string of size substr_len 
            # if it contains all the words or not
            curr_str_freq = {}
            j=i
            while j< i+ substr_len:
                curr_str = s[j:j+k]
                curr_str_freq[curr_str] = curr_str_freq.get(curr_str,0) + 1
                j += k
            if curr_str_freq == word_freq:
                consecutive_substrings_for_all_words.append(s[i:i + substr_len])
                consecutive_substrings_for_all_words_indices.append(i)
    return consecutive_substrings_for_all_words  ,consecutive_substrings_for_all_words_indices     

            
s = "barfoothefoobarthefoo"
words = ["bar", "foo", "the"]  
# ['barfoothe', 'thefoobar', 'foobarthe', 'barthefoo']    
                
# print(detect_consecutive_substrings(s,words))
                
                
    
"""
Scenario 4: Detecting Suspicious Purchase Patterns
You work at a fintech company analyzing user transactions. 
One suspicious activity your fraud detection team has flagged involves users making consecutive purchases of the same value, 
say exactly three $100 purchases in a row. These are often associated with fraudulent automation scripts.

Your task is to detect if any sequence of exactly k identical values occurs consecutively in the transaction logs.

You are given:

A list of transaction values (List[int] transactions)

An integer k — the count of consecutive identical transactions you are looking for.

🎯 Objective:
Return all starting indices where a group of exactly k consecutive identical transactions occurred.

"""

def detect_k_consecutive(nums,k):
    # Return all starting indices 
    # where a group of exactly k consecutive identical transactions occurred.
    """
    This has to be addressed through a dynmaic sliding window
    move r if previous one is equal to curr one 
    use a variable cnt, once we find k consecutive, get index of the start 
    r-k+1
    update l +1, decrease the cnt and check the next element
    continue this process
    """

    n = len(nums)
    if k>n:
        return []
    # # edge case len of nums is 1 and k is also 1 , we can return [0]
    # if n==1 and k==1:
    #     return [0]
    
    r = 0
    cnt = 0
    prev = None
    start_indices_of_k_consecutive = []
    
    while r<n:
        curr = nums[r]
        if curr == prev:
            cnt += 1
        else: # curr != prev:
            cnt = 1
        
        if cnt == k:
            # we have found the k consecutive characters
            ind = r - k + 1
            start_indices_of_k_consecutive.append(ind)
            
            # we will update the l and cnt
            # by increasing l by 1 and reducing cnt by 1
            cnt -= 1
            
        prev = curr
        r += 1
    
    return start_indices_of_k_consecutive

print(detect_k_consecutive([100, 100, 100, 200, 100, 100, 300, 300, 300],k=3))
print(detect_k_consecutive([100],k=3))
print(detect_k_consecutive([100],k=1))
    
"""
1004. Max Consecutive Ones III
Solved
Medium
Topics
conpanies icon
Companies
Hint
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
"""      

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """

        I need to find cosecutive ones and I can flip at most k 0s
        so it means k 0s are allowed

        we can try to catch a string where maximum 0 should be less than k

        """

        n = len(nums)
        l = 0
        r = 0
        zero_cnt = 0
        longest_ones = 0

        while r<n:
            if nums[r] == 0:
                zero_cnt += 1
            
            if zero_cnt <= k:
                longest_ones = max(longest_ones ,r-l+1)
                
            while zero_cnt > k:
                if nums[l] == 0:
                    zero_cnt -= 1
                l+=1

            r+=1
        return longest_ones
    
    

def find_str_anomalies(s,words):
    """
    Scenario:
    You're working with a team at Google on log inspection tools. 
    You've received a report that in a stream of system logs (represented as a single string), 
    certain keywords appear in a specific pattern. 
    You are given a string of logs s and a list of suspicious words words, 
    where each word has equal length.

    Your job is to find all starting indices in s where a concatenation of all suspicious words
    (in any order, without overlap) appears as a substring.
    ❗ Each word in the list must appear exactly once in the window.
    ❗ You can assume the words are all the same length.
    ❗ Words may repeat in the input list.
    """
    n = len(s)
    k = len(words[0])
    substr_len = k*len(words)
    if n<k:
        return []
    
    # I need to find all words I can create a map, with frequency of the words to check the words
    word_map = {}
    for word in words:
        word_map[word] = word_map.get(word,0) + 1

    # I can use a pointer to move through the string O(n), i need to check till last valid word
    r = 0
    str_anomalies_indices = []
    
    while r < n-substr_len+1:

        # check a sub_str of len k from index r if it is in words we will check rest of the string
        curr_word = s[r:r+k]
        if curr_word in word_map:
            # I have foudn a word now I can check till len of substring of words if that actually contains all the words with same frequency

            curr_str_word_map = {}
            j = r
            while j < r+substr_len:
                new_word = s[j:j+k]
                if new_word in word_map:
                    # we found the word
                    curr_str_word_map[new_word] = curr_str_word_map.get(new_word,0) + 1
                else:
                    # if the word is not in word there is no point in exploring letter part
                    break
                
                j += k
            
            if curr_str_word_map == word_map:
                str_anomalies_indices.append(r)
        r+=1
    
    return str_anomalies_indices

# s = "barfoofoobarthefoobarman"
# words = ["bar","foo","the"]

# print(find_str_anomalies(s,words))


def find_transaction_frauds_for_target(transactions,target):
    """
    Transaction Surge Monitoring System
    You're helping build an automated fraud detection system for a financial product at Google. 
    The system monitors transaction amounts over time, represented as an integer array transactions.

    You're given an array of integers transactions and an integer target.
    Your task is to detect the number of continuous windows (subarrays) where the sum of elements equals exactly the target.

    This allows fraud detection teams to analyze patterns like multiple small deposits adding up to a suspicious amount.

    🔍 Constraints:
    The transactions can be positive, zero

    You need to handle millions of entries, so performance matters.

    You can only use O(n) time.
    
    *** If there are negative values then we will have to use prefix sum
    
    """
    l = 0
    r = 0
    n = len(transactions)
    windows = []
    curr_sum =0
    while r <n:
        curr_sum += transactions[r]
        # update l 
        while curr_sum >= target:
            if curr_sum == target:
                windows.append(transactions[l:r+1])
            curr_sum -= transactions[l]
            l+=1
        r+=1
    return windows

transactions = [3, 4, 7, 2, 1, 4, 2]
target = 7
print(find_transaction_frauds_for_target(transactions,target))