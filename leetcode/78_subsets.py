class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def power_set(offset, partial):
            print(100, offset, partial)
            if offset == len(nums):
                result.append(partial[:])
                return

            print(200, offset, partial)
            power_set(offset+1, partial)
            print(300, offset, partial)
            partial.append(nums[offset])
            power_set(offset+1, partial)
            print(400, offset, partial)
            partial.pop()
            print(500, offset, partial)
                      
        import pdb
        pdb.set_trace()
        result = []
        power_set(0, [])
        return result

nums = [1,2,3]
print(Solution().subsets(nums))
