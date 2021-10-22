class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        rows = len( matrix )
        if not rows:
            return 0
        
        columns = len( matrix[0] )
        
        dp = [0]*(columns+1)
        
        maxax = 0
        pre = 0
        
        for i in range(1,rows+1):
            for j in range(1,columns+1):
                
                temp = dp[j]
                if matrix[i-1][j-1] == "1":
                    dp[j] = min( [dp[j-1], pre, temp] ) + 1
                    maxax = max( dp[j], maxax )
                else:
                    dp[j] = 0
                
                pre = temp
        return maxax*maxax
