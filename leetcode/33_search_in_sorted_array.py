class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        import pdb
        pdb.set_trace()
        left, right = 0, len(nums)-1
        
        while left <= right:
            mid = (left + right)//2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                if target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return -1
                
nums, target = [4,5,6,7,8,1,2,3], 8
print(Solution().search(nums, target))
