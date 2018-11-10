class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def get_neighbors(x,y):
            return ((i, j) for i, j in ((x-1, y), (x, y-1), (x, y+1), (x+1, y)) if 0 <= i < N and 0 <= j < M)
        
        def dfs_helper(x,y, word_index):
            if word_index == len(word):
                return True
            
            if seen[x][y] or word[word_index] != board[x][y]:
                return False
            
            seen[x][y] = True
            for i,j in get_neighbors(x,y):
                retval = dfs_helper(i,j, word_index+1)
                if retval:
                    return retval
            seen[x][y] = False
            return False
        
        if not board:
            return False
        
        N = len(board)
        M = len(board[0])
        
        seen = [[False] * M for _ in range(N)]
        
        for i in range(N):
            for j in range(M):
                retval = dfs_helper(i, j, 0)
                if retval:
                    return retval
        return False
        
import pdb
pdb.set_trace()
board, word =[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"
print(Solution().exist(board,word))
