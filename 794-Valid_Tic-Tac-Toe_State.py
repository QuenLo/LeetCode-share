class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        
        def win( c ):
            
            col = [0]*3
            row = [0]*3
            right = 0
            left = 0
            total = 0
            
            for i in range(3):
                for j in range(3):
                    if board[i][j] == c:
                        total += 1
                        col[j] += 1
                        row[i] += 1
                        if i == j:
                            right += 1
                        if (i+j) == 2:
                            left += 1
            
            return total, (3 in col or 3 in row or left == 3 or right == 3)
        
        
        Ocount, Owin = win("O")
        Xcount, Xwin = win("X")
        
        # both win
        if Owin and Xwin:
            return False
        
        # not win
        if not Owin and not Xwin:
            return (Ocount == Xcount) or (Ocount == Xcount-1)
        
        # X win
        if Xwin:
            return Xcount == Ocount+1
        
        # O win
        return Xcount == Ocount
