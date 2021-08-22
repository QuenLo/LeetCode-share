class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        N = 9
        
        row = [ set() for _ in range(N) ]
        column = [ set() for _ in range(N) ]
        grid = [ set() for _ in range(N) ]
        
        for i in range(N):
            for x in range(N):
                
                val = board[i][x]
                if val == '.':
                    continue
                    
                if val in row[i]:
                    return False
                row[i].add(val)
                
                if val in column[x]:
                    return False
                column[x].add(val)
                
                if val in grid[ (i // 3)*3 + (x // 3) ]:
                    return False
                grid[ (i // 3)*3 + (x // 3) ].add(val)
                
        return True
