class Solution:

    def get_lps(self,needle):
        """
        proper LPS:
           Needeles:  aaacaaa   &  abababaaba
           lps array: 0120123      0012345123

        """
        m = len(needle)
        lps = [0 for i in range(m)]
        # since in any array lsp of first element is zero ABC: A canot have any proper pref or suff
        prev_lps_pointer = 0
        i = 1

        while i<m:
            # if current element of needle is equal to prev_lsp_pointer of needle
            if needle[i] == needle[prev_lps_pointer]:
                # they are same, lsp of current pointer will
                lps[i] = prev_lps_pointer + 1
                prev_lps_pointer = lps[i]
                i += 1
            # if current element is not equal to prev_lps_pointer element of needle,and prev_lps_pointer is zero
            elif prev_lps_pointer == 0:
                # it doesn't have any prefix and suffix of same length
                lps[i] = 0
                i+=1
            # if current element is not equal to prev lst pointer element of needle, then we will decrese the pointer to check where it matches
            else:
                # check with the previous one
                prev_lps_pointer = lps[prev_lps_pointer - 1]
        return lps



    def strStr(self, haystack: str, needle: str) -> int:
        """
        This problem can be solved in two ways:
        1. Brute force approach where I can iterate over the array twice O(m.n) and find hte first index of occurance of needle in haystack
        ## Brute Force Approach
        n, m = len(haystack), len(needle)
        # Edge Case: needle is empty
        if m == 0:
            return 0
        # check till n-m+1 only
        for i in range(n - m + 1):
            # keep checking till you find the needle
            # initially match is True
            match = True
            for j in range(m):
                if haystack[i + j] != needle[j]:
                    match = False
                    break
            if match:
                return i 
        return -1

        2. KMP algorith: O(m+n)
            1. Find LPS (Longest Prefix Suffix)
                proper LPS:
                    AAACAAA   &  ABABABAABA
                    0120123      0012345123
            2. Iterate with LPS to avoid duplicate checks of Brute Force Approach
        
        """
        n = len(haystack)
        m = len(needle)
        i = 0
        j = 0
        lps = self.get_lps(needle)
        # print(lps)

        while i<n:
            # both are matching keep progressing
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            # not matching
            else:
                # I need to decrease j such that I dont repeat myself using lps
                # if it reaches 0 then we will have to go to next index
                if j == 0:
                    i +=1
                else:
                    # check from last matching index
                    j = lps[j-1]
            
            if j ==m :
                # if j reaches m that means we have found the string
                return i - m
        return -1            
        




        




