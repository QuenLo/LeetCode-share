class TicTacToe:

    def __init__(self, n: int):
        self.rows = [0]*n
        self.cols = [0]*n
        self.right = 0
        self.left = 0
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        p_int = 1 if player == 1 else -1
        
        self.rows[row] += p_int
        self.cols[col] += p_int
        
        if row == col:
            self.right += p_int
        if (row+col) == self.n-1:
            self.left += p_int
        
        if self.n == abs(self.rows[row]) or self.n == abs(self.cols[col]) or self.n == abs(self.right) or self.n == abs(self.left):
            return player
        
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
