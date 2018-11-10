import pdb

class Solution:
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        def average_neighbor(M, x, y):
            neighbors = [M[i][j] for i in range(x-1, x+2) for j in range(y-1, y+2) if i >= 0 and i < len(M) and j >= 0 and j < len(M[0])]
            avg = sum(neighbors)//len(neighbors)
            return avg
        
        if not M:
            return M
        
        pdb.set_trace()
        s = [[average_neighbor(M, x, y) for y in range(len(M[0]))] for x in range(len(M))]
        return s

M = [[1,1,1],[1,0,1],[1,1,1]]
print(Solution().imageSmoother(M))
