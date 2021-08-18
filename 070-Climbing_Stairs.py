## Dynamic Programing
# Time: O(n)
# Space: O(n)
class Solution:
    def climbStairs(self, n: int) -> int:
        
        # dp[i] = dp[i-1] + dp[i-2]
        
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 2
        
        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]
            
        return dp[n-1]

## Fibonacci Number
# Time: O(n)
# Space: o(1)
class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n == 1: return 1
        
        first = 1
        second = 2
        for i in range(2,n):
            third = first + second
            first = second
            second = third
            
        return second
      
## Brute Force
# Time: O(2^n)
# Space: O(n) The depth of the recursion tree can go upto nn.
class Solution:
    def climbStairs(self, n: int) -> int:
        
        def climb( i, n ):
            if i>n:  return 0
            if i == n: return 1
            
            return climb(1+i,n) + climb(2+i,n)
        
        return climb(0,n)
      
## Recursion with Memoization
# Time: O(n)
# Space: O(n)
class Solution:
    def climbStairs(self, n: int) -> int:
        
        memo = [0]*(n+1)
        
        def climb( i, n, memo):
            
            if i > n: return 0
            if i == n : return 1
            if memo[i] > 0: return memo[i]
            
            memo[i] = climb( i+1, n, memo ) + climb( i+2, n, memo )
            return memo[i]
        
        
        return climb( 0, n, memo )
