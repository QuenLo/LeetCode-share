# Time Complexity: O((R*C)^2), where R, CR,C is the number of rows and columns in board.
# Space Complexity: O(1)
class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        
        R, C = len(board), len(board[0])
        nextR = False
        
        # crash Row
        for r in range(R):
            for c in range(C-2):
                if abs(board[r][c]) == abs(board[r][c+1]) == abs(board[r][c+2]) != 0:
                    board[r][c] = board[r][c+1] = board[r][c+2] = -abs(board[r][c])
                    nextR = True
        
        # crash Column
        for r in range(R-2):
            for c in range(C):
                if abs(board[r][c]) == abs(board[r+1][c]) == abs(board[r+2][c]) != 0:
                    board[r][c] = board[r+1][c] = board[r+2][c] = -abs(board[r][c])
                    nextR = True
                    
        # gravity
        for c in range(C):
            wr = R-1 #write from the botton
            for r in range(R-1,-1,-1):
                if board[r][c] > 0:
                    board[wr][c] = board[r][c]
                    wr -= 1
            for r in range(wr,-1,-1):
                board[r][c] = 0
                
        return self.candyCrush(board) if nextR else board
