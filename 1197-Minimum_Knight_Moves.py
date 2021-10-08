class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        
        
        @lru_cache(maxsize=None)
        def dfs( x, y ):
            
            if x + y == 0:
                return 0
            elif x+y == 2:
                return 2
            
            else:
                return min(  dfs( abs(x-1), abs(y-2) ),dfs( abs(x-2), abs(y-1) )) + 1
            
    
        return dfs( abs(x), abs(y) )
