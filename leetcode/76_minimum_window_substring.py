import pdb

from collections import OrderedDict
class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # can T have duplicate characters? - then this won't work
        locations = OrderedDict()
        pdb.set_trace()
        
        min_window_len = float('inf')
        min_left, min_right = -1, -1
        
        for i, c in enumerate(s):
            char_count = t.count(c)
            if char_count:
                added = False
                for char_idx in range(char_count):
                    if (c, char_idx) not in locations:
                        locations[(c, char_idx)] = i
                        added = True
                        break
                if not added:
                    # Need to delete the one with the min index
                    min_index = min((x for (char, _), x in locations.items() if c == char))
                    for char_idx in range(char_count):
                        if locations[(c,char_idx)] == min_index:
                            del locations[(c, char_idx)]
                            locations[(c, char_idx)] = i
                            break
                if len(locations) == len(t):
                    # We're covering all the characters
                    # Extract the character with the min-index and pop-it
                    #left = min((x[0] for x in locations.values()))
                    _, left = locations.popitem(last=False)
                    if min_window_len > i-left+1:
                        min_window_len = i-left+1
                        min_left = left
                        min_right = i
        if min_window_len == float('inf'):
            result = ''
        else:
            result = s[min_left:min_right+1]
        return result
        
from collections import defaultdict
class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        pdb.set_trace()
        t_char_counts = defaultdict(int)
        for c in t:
            t_char_counts[c] += 1

        s_char_counts = defaultdict(int)
        s_chars_formed = 0

        min_len, min_left, min_right = float('inf'), -1, -1
        left = 0


        for right in range(len(s)):
            char = s[right]

            if char in t_char_counts:
                s_char_counts[char] += 1
                if s_char_counts[char] == t_char_counts[char]:
                    s_chars_formed += 1

                    while left <= right and s_chars_formed == len(t_char_counts):
                        if min_len > right-left+1:
                            min_len = right-left+1
                            min_left = left
                            min_right = right

                        char_drop_s = s[left]
                        if char_drop_s in t_char_counts:
                            s_char_counts[char_drop_s] -= 1
                            if s_char_counts[char_drop_s] < t_char_counts[char_drop_s]:
                                s_chars_formed -= 1
                                
                        left += 1

        if min_len == float('inf'):
            result = ''
        else:
            result = s[min_left:min_right+1]
        return result

        
s = "ADOBECODEBANC"
t = "ABC"
print(Solution().minWindow(s, t))
s = "aa"
t = "aa"
print(Solution().minWindow(s, t))
s = "aBbaBBBBA"
t = "BBA"
print(Solution().minWindow(s, t))
