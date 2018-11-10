
import pdb
class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        max_left = [0] * len(height)
        max_right = [0] * len(height)

        pdb.set_trace()
        
        for i in range(1, len(height)):
            max_left[i] = max(max_left[i-1], height[i-1])
        
        for i in reversed(range(len(height)-1)):
            max_right[i] = max(max_right[i+1], height[i+1])
            
        water_collected = 0
        for i, h in enumerate(height):
            water_above = min(max_left[i], max_right[i])
            water_above = max(0, water_above - h)
            water_collected += water_above
        return water_collected
            


A = [0,1,0,2,1,0,1,3,2,1,2,1]
ans = 6

print(Solution().trap(A))
