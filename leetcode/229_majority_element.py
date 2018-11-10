from collections import defaultdict
class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        counts = defaultdict(int)
        
        for n in nums:
            counts[n] += 1
            if len(counts) == 3:
                for c in list(counts.keys()):
                    counts[c] -= 1
                    if counts[c] == 0:
                        del counts[c]
        
        for c in counts:
            counts[c] = 0
            
        for n in nums:
            if n in counts:
                counts[n] += 1
        
        return [x for x in counts if counts[x] > len(nums)//3]

import pdb
pdb.set_trace()
nums  = [1,2]
print(Solution().majorityElement(nums))
