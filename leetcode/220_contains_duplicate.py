import bisect
class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        knums = []
        for i in range(len(nums)):
            j = bisect.bisect_left(knums, nums[i])
            if j > 0 and nums[i]-knums[j-1] <= t:
                return True
            if j < len(knums) and knums[j] - nums[i] <= t:
                return True
            knums.insert(j, nums[i])
            
            if i >= k:
                knums.remove(nums[i-k])
        return False

import pdb
pdb.set_trace()
nums, k, t = [-1, -1], 1, 0
print(Solution().containsNearbyAlmostDuplicate(nums, k, t))
