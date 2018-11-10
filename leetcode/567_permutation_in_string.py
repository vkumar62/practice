from collections import defaultdict
class Solution:
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        a_counts = defaultdict(int)
        for c in s1:
            a_counts[c] += 1
            
        s_counts = defaultdict(int)
        chars_formed = 0
        
        for right in range(len(s2)):
            c = s2[right]
            if c in a_counts:
                s_counts[c] += 1
            
                if s_counts[c] == a_counts[c]:
                    chars_formed += 1
            
            if chars_formed == len(a_counts):
                return True
            
            if right + 1 >= len(s1):
                remove_char = s2[right+1-len(s1)]
                if remove_char in s_counts:
                    if s_counts[remove_char] == a_counts[remove_char]:
                        chars_formed -= 1
                    s_counts[remove_char] -= 1
                    #if s_counts[remove_char] == 0:
                     #   del s_counts[remove_char]
        return False

import pdb
pdb.set_trace()
s1, s2 = "ab", "eidbaooo"
print(Solution().checkInclusion(s1, s2))
