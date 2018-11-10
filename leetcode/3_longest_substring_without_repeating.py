class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_set = set()
        left = right = 0
        maxlen = 0
        
        for right in range(len(s)):
            if s[right] in char_set:
                maxlen = max(maxlen, right-left)
            
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            
            char_set.add(s[right])
        
        maxlen = max(maxlen, right-left)
        return maxlen
import pdb
pdb.set_trace()
s = ' '
print(Solution().lengthOfLongestSubstring(s))
