
"""
**Original Google-Style Interview Question:**

Recently appeared for phone screening for L4 role with Google.
Leetcode discuss section was really useful in my preparation. So writing this to give back to the community.

Was asked below question. "some messages" were some actual message, skipping them as they don't matter.

**Example 1:**

```python
message = [
    {'A'}: "some message", {'B'}: "some message", {'A'}: "some message",
    {'A'}: "some message", {'B'}: "some message", {'B'}: "some message",
    {'C'}: "some message", {'C'}: "some message", {'A'}: "some message",
    {'C'}: "some message", {'B'}: "some message", {'A'}: "some message",
    {'C'}: "some message", {'C'}: "some message", {'B'}: "some message"
]
# Truncate the messages to have a list of 9 messages.
# We need fair allocation of message.
# Actual message don't matter.
# Question: how many messages from each category will you retain?


**Example 2:**

python
message = [
    {'A'}: "some message", {'B'}: "some message", {'A'}: "some message",
    {'A'}: "some message", {'B'}: "some message", {'B'}: "some message",
    {'A'}: "some message", {'C'}: "some message", {'B'}: "some message",
    {'A'}: "some message", {'B'}: "some message"
]
# Truncate the messages to have a list of 9 messages.
# We need fair allocation of message.


**Additional Clarification from Interviewer:**
Then asked what is meant by "fair allocation?"
Candidate responded: "We will do a fractional allocation to ensure fairness."
Interviewer said: "We need to have one max cap for all messages."
This led to thinking in the direction of binary search on answers.

---

**Interpretation:**
You are given a list of messages by category, and you must reduce the total list to exactly N messages (here N=9) such that no category gets more than a "cap" number of messages, and the allocation is as fair as possible.

**Key Observations:**

* Need to cap the number of messages per category.
* Total selected messages = N
* Find the **maximum cap** such that after capping each category to that number, we can fill exactly N messages.

This is equivalent to: **binary search the maximum allowed cap (per category) that allows selecting exactly N messages.**

---

**LeetCode Related Problems:**

* [L1231. Divide Chocolate](https://leetcode.com/problems/divide-chocolate/): Binary Search on Answer
* [L875. Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/): Binary Search on rate/capacity
* [L1283. Find the Smallest Divisor Given a Threshold](https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/): similar binary search on max-cap answer

---

**Modular Python Solution:**

"""
from collections import Counter

def fair_message_allocation(messages, total_allowed):
    # Step 1: Count how many messages from each category
    freq = Counter()
    for m in messages:
        for k in m:
            freq[k] += 1

    categories = list(freq.keys())

    def can_allocate(cap):
        return sum(min(cap, freq[k]) for k in categories) >= total_allowed

    # Step 2: Binary search the maximum cap
    low, high = 1, max(freq.values())
    best_cap = 1

    while low <= high:
        mid = (low + high) // 2
        if can_allocate(mid):
            best_cap = mid
            high = mid - 1  # Try smaller cap to be more fair
        else:
            low = mid + 1

    # Step 3: Construct final message allocation
    result = []
    counts = {k: 0 for k in categories}
    cap = best_cap

    for msg in messages:
        if len(result) == total_allowed:
            break
        for k in msg:
            if counts[k] < min(cap, freq[k]):
                result.append({k})
                counts[k] += 1
            break

    return result

# Example usage
messages = [
    {'A'}, {'B'}, {'A'}, {'A'}, {'B'}, {'B'},
    {'C'}, {'C'}, {'A'}, {'C'}, {'B'}, {'A'}, {'C'}, {'C'}, {'B'}
]

selected = fair_message_allocation(messages, 9)
print(selected)
"""

**Time Complexity:**

* O(N log M) where N is number of messages, M is max frequency per category (binary search range).

**Space Complexity:**

* O(K) where K is number of unique categories.
"""