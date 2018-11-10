
# This doesn't work
import pdb
class NumMatrix:

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        
        if not matrix:
            return
        
        self.R = len(matrix)
        self.C = len(matrix[0])
    
        self.sumR = self.R + 1
        self.sumC = self.C + 1
        
        # Deep copy the matrix
        self.matrix = [[matrix[i][j] for j in range(self.C)] for i in range(self.R)]
        self.sums = [[0 for _ in range(self.sumC)] for _ in range(self.sumR)]
        
        #for r in range(self.R):
        self.update_sum(0, 0)
        
    def update_sum(self, row, col):
        for r in range(row+1, self.sumR):
            for c in range(col+1, self.sumC):
                self.sums[r][c] = self.matrix[r-1][c-1] + self.sums[r][c-1] + self.sums[r-1][c]

    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        if row < 0 or row >= self.R or col < 0 or col >= self.C:
            return
        self.matrix[row][col] = val
        self.update_sum(row, col)
        

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        pdb.set_trace()
        if not 0 <= row1 < self.R or not 0 <= row2 < self.R or not 0 <= col1 < self.C or not 0 <= col2 < self.C:
            return 0

        row1, row2, col1, col2 = row1 + 1, row2+1, col1+1, col2+1
        s = 0
        s = self.sums[row2][col2] + self.sums[row1-1][col1-1] - self.sums[row1-1][col2] - self.sums[row2][col1-1] 
        return s

matrix = [[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]
a = NumMatrix(matrix)
print(a.sumRegion(2,1,4,3))

