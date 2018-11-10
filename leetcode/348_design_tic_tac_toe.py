import pdb

class TicTacToe:

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.player_counts = [[0] * ((2*n)+2) for _ in range(2)]
        self.n = n
        #self.player_2_counts = [0] * (2*n+2)

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        player = player-1
        n = self.n
        self.player_counts[player][row] += 1
        self.player_counts[player][n+col] += 1
        if row == col:
            self.player_counts[player][2*n] += 1
        if row+col == n-1:
            self.player_counts[player][(2*n)+1] += 1
        
        #pdb.set_trace()
        if max(self.player_counts[player]) == n:
            return player+1
        return 0
            

t = TicTacToe(3)
moves = [[0,0,1],[0,2,2],[2,2,1],[1,1,2],[2,0,1],[1,0,2],[2,1,1]]

for move in moves:
    print(t.move(*move))
