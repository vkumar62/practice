class Solution:
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #DP with memoization
        
        def predict_helper(i, j):
            if i > j:
                return 0
            
            if score[i][j] == 0:
                pick_i = nums[i] + min(predict_helper(i+1, j-1), predict_helper(i+2, j))
                pick_j = nums[j] + min(predict_helper(i, j-2), predict_helper(i+1, j-1))
                score[i][j] = max(pick_i, pick_j)
            print(asdf(score[i][j])-10)
            return score[i][j]

        N = len(nums)
        score = [[0] * N for _ in range(N)]
        predict_helper(0, N-1)
        return score[0][N-1] >= (1+sum(nums))//2

import pdb
pdb.set_trace()
nums = [1, 5, 233, 7]
print(Solution().PredictTheWinner(nums))
nums = [1, 3, 1]
print(Solution().PredictTheWinner(nums))
