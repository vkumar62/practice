import pdb
class Solution:
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
#        pdb.set_trace()
        LIVE = 1
        DEAD = 0
        
        NEXT_VAL = {
            LIVE : lambda x: DEAD if x < 2 or x > 3 else LIVE,
            DEAD : lambda x: LIVE if x == 3 else DEAD
        }
        
        if not board:
            return
        
        N = len(board)
        M = len(board[0])
        result = [[None] * M for _ in range(N)]
        
        for i in range(N):
            for j in range(M):
#                neighbors = [board[x][y] for x in range(i-1, i+2) for y in range(j-1, j+2) if x >= 0 and x < N and y >= 0 and y < M and x != i and y != j]
                neighbors = [board[x][y] for x in range(i-1, i+2) for y in range(j-1, j+2) if x >= 0 and x < N and y >= 0 and y < M and (x != i or y != j)]
                neighbor_count = sum(neighbors)
                result[i][j] = NEXT_VAL[board[i][j]](neighbor_count)
        
        for i in range(N):
            for j in range(M):
                board[i][j] = result[i][j]
                
       

board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]] 
Solution().gameOfLife(board)
print(board)
