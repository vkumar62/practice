import pdb

class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        pdb.set_trace()
        if False:
            maxleft = [-1] * len(nums)
            minright = [-1] * len(nums)

            for i, num in enumerate(nums):
                if i == 0 or nums[i] >= nums[maxleft[i-1]]:
                    maxleft[i] = i
                else:
                    maxleft[i] = maxleft[i-1]

            for i, num in reversed(list(enumerate(nums))):
                if i == len(nums) - 1 or nums[i] <= nums[minright[i+1]]:
                    minright[i] = i
                else:
                    minright[i] = minright[i+1]

            start = end = -1
            for i in range(len(nums)):
                if maxleft[i] != minright[i]:
                    start = i
                    break
            for i in reversed(range(len(nums))):
                if maxleft[i] != minright[i]:
                    end = i;
                    break
            if end != -1:
                return end-start+1
        if not nums:
            return 0
        
        start = end = -1
        maxleft = nums[0]
        for i, num in enumerate(nums[1:]):
            if num < maxleft:
                end = i+1
            maxleft = max(maxleft, num)
        minright = nums[-1]
        for i, num in reversed(list(enumerate(nums[:-1]))):
            if num > minright:
                start = i
            minright = min(minright, num)
        if end == -1:
            return 0
        return end - start + 1

nums = [2,6,4,8,10,9,15]
print(Solution().findUnsortedSubarray(nums))
nums = [2,3,3,2,4]
print(Solution().findUnsortedSubarray(nums))
