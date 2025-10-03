"""
10. Regular Expression Matching

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

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        TC O(m*n)
        What we need to find is does this pattern matches with the string or not
        that means it should completely generate the string, nothing left either in s or p

        the pattern has 2 wild cards
        1. "." it can take form of anything which is okay we don't have to worry about that more
        2. "*" this guy is the real player he can make the whole sting or can decrease the size of pattern
        
        "a*" ----> "" empty, or  "a", "aa" ........ "aaaaaaaaaaaa......inf"
        ".*" ---> this can geneate any string that you can imaging
        

        To solve this we have to recursively find all possible options that can be done using 
        """

        ns = len(s)
        np = len(p)

        memo ={}

        def rec(i,j,s,p,ns,np,memo):
            if (i,j) in memo: return memo[(i,j)]
            # base case will be 
            if i == ns and j == np:
                # p was completely utilized to generate the s
                return True
            
            # p was over before n could have been generated
            if j == np:
                return False


            # check the first element
            match = False
            if (i<ns) and (s[i]==p[j] or p[j]=="."):
                match = True
            
            # check for the wild card "*" Hero of this problem
            if j+1 <= np-1 and p[j+1] == "*":
                # there can be two casesa
                # i=2
                # s = ascer
                # asd*cer
                # j 0123456
                #     i,j+2

            # i.  012345678910
                # asddddddcer
                # asc*dcer
              # j 0123456
                # j, i+1 , 2,3
                # j, i+1 =4
                # j = 2, i=8
                # j+2, 4, i=8
                # 


                # ascer ###
                # asd*cer
                # asdd*cer

                # either you keep using *, increase i keep j same or skip currletter, * and move to j+2 , i remains same
                # you can continue iterating only till you find match
                
                take = False
                if match:
                    # increase i and keep j same as you will keep iterating
                    take  = rec(i+1,j,s,p,ns,np,memo)
                
                # you will just skip the wild card to explore other path
                not_take = rec(i, j+2,s,p,ns,np,memo)

                # anyone of above can you get me pattern match?
                memo[(i,j)] = take or not_take
                return memo[(i,j)]

            else:
                # there is no wild at j+1 index keep iterating in normal way 
                # you will check further match only and only if current step is matching other wise there is no need

                if match:
                    # 
                    match = rec(i+1,j+1,s,p,ns,np,memo)

                memo[(i,j)] = match
                return memo[(i,j)]
        
        return rec(0,0,s,p,ns,np,memo)



        