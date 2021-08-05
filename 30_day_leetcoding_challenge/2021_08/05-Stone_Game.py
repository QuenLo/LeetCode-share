class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        Alex = 0
        Lee = 0
        while len(piles):
            
            Alex += piles[-1 if piles[0] < piles[-1] else 0]
            piles.pop(-1 if piles[0] < piles[-1] else 0)
            
            Lee += piles[-1 if piles[0] > piles[-1] else 0]
            piles.pop(-1 if piles[0] > piles[-1] else 0)
            
        return Alex > Lee
      
# Time Complexity: O(N)
# Space Complexity: O(1)
## ALEX will always win

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        N = len(piles)
        
        def count( i, j ):
            
            if i > j: return 0 # the end
            who = (i-j-N) %2
            if who: # who == 1 -> Alex
                return max( piles[i] + count(i+1,j), piles[j] + count(i, j-1) )
            else: # Lee
                return min( -piles[i] + count(i+1,j), piles[j] + count(i, j-1) )
        
        return count( 0, N-1 ) > 0
      
# Time Complexity: O(N^2)
# Space Complexity: O(N^2)
