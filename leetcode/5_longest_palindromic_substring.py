import pdb

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        pdb.set_trace()
        
        # 2D table that stores 1 if str[i..j] can be a palindrome
        # base case is table[i][i] = True
        # table[i][i+1] = True if str[i] == str[i+1]
        # for all others: table[i][j] = table[i+1][j-1] if str[i] == str[j] else False
        lens = [[0] * len(s) for _ in range(len(s))]
        
        for i in range(len(s)):
            lens[i][i] = 1
            if i+1 < len(s) and s[i] == s[i+1]:
                lens[i][i+1] = 1
        
        for dif in range(2, len(s)):
            for i in range(len(s) - dif):
                if s[i] == s[i+dif]:
                    lens[i][i+dif] = lens[i+1][i+dif-1]
        
        max_j, min_i = None, None
        # Figure out the entry with 1 such that col-row is maximum
        for dif in reversed(range(len(s))):
            for i in range(len(s)-dif):
                if lens[i][i+dif]:
                    max_j = i+dif
                    min_i = i
                    break
            if max_j:
                break
        return s[min_i:max_j+1]
        
s = "babad"
print(Solution().longestPalindrome(s))
