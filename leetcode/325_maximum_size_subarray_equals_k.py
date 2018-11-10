
import pdb
class Solution:
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        pdb.set_trace()
        prefix_sums = {}
        prefix_sums[0] = -1
        cur_sum = 0
        maxlen = 0
        
        for i, num in enumerate(nums):
            cur_sum += num
            if cur_sum not in prefix_sums:
                prefix_sums[cur_sum] = i
            if cur_sum-k in prefix_sums:
                maxlen = max(maxlen, i-prefix_sums[cur_sum-k])
        
        return maxlen
            

nums, k = [-2,-1,2,1], 1
print(Solution().maxSubArrayLen(nums,k))
