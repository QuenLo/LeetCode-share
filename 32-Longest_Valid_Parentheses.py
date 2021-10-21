class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        maxax = 0
        dp = [ 0 for _ in range(len(s)) ]
        
        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i-1] == '(':
                    dp[i] = dp[i-2] +2 if i >= 2 else 2
                elif( i - dp[i-1] > 0 and s[i-dp[i-1]-1] == '('):
                    more = dp[ i-dp[i-1]-2 ]+2 if (i-dp[i-1] >= 2) else 2
                    dp[i] = dp[i-1] + more
                
                maxax = max( maxax, dp[i] )
                
        return maxax
