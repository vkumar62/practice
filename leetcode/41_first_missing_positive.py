import pdb
class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pdb.set_trace()
        
        i = 0
        while i < len(nums):
            if 0 < nums[i] <= len(nums):
                if nums[i] != i+1 and nums[nums[i]-1] != nums[i]:
                    nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
                else:
                    i = i + 1
            else:
                nums[i] = 0
                i = i + 1
        
        for i, num in enumerate(nums):
            if num != i+1:
                return i+1
        return len(nums)+1

nums = [1,1]
print(Solution().firstMissingPositive(nums))
