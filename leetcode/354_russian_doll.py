
import pdb
class Solution:
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        if not envelopes:
            return 0
        maxenvelopes = [1] * len(envelopes)
        pdb.set_trace()
        
        for i in range(len(envelopes)):
            n = 0
            for j in range(len(envelopes)):
                if envelopes[i][0] > envelopes[j][0] and envelopes[i][1] > envelopes[j][1]:
                    #n += 1
                    n = max(n, maxenvelopes[j])
            maxenvelopes[i] += n
        return max(maxenvelopes)

inp = [[4,5],[4,6],[6,7],[2,3],[1,1]]

outpe = 4

outp = Solution().maxEnvelopes(inp)
