import pdb
class Solution:
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        def dfs_helper(i, j):
            if visited[i][j]:
                return
            
            result[i][j] += 1
            visited[i][j] = True
            
            neighbors = ((x,y) for x, y in ((i-1, j), (i, j-1), (i, j+1), (i+1, j)) if 0 <= x < N and 0 <= y < M)
            for x,y in neighbors:
                if matrix[x][y] >= matrix[i][j]:
                    dfs_helper(x, y)
            
            
        #pdb.set_trace()   
        if not matrix:
            return matrix
        N = len(matrix)
        M = len(matrix[0])
        
        result = [[0 for _ in range(M)] for _ in range(N)]
        visited = [[False for _ in range(M)] for _ in range(N)]
        
        for i in range(N):
            dfs_helper(i, 0)
        for j in range(M):
            dfs_helper(0, j)
                
        # Now reset the visited and start from Atlantic side
        visited = [[False for _ in range(M)] for _ in range(N)]
        
        for i in range(N):
            dfs_helper(i, M-1)
        for j in range(M):
            dfs_helper(N-1, j)
                
        result = [[x,y] for x in range(N) for y in range(M) if result[x][y] == 2]
        return result

matrix = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
print(Solution().pacificAtlantic(matrix))
