class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if not nums: return 0
        if len(nums) == 1: return nums[0] 
        if len(nums) == 2: return max( nums[0], nums[1] )
        
        N = len(nums) - 1
        return max( self.rob_deep( nums[0:N] ), self.rob_deep( nums[1:N+1] ) )
        
    def rob_deep(self, nums: List[int]) -> int:
        
        if not nums: return 0
        
        Length = len(nums)
        if Length == 1: return nums[0] 
        if Length == 2: return max( nums[0], nums[1] )
        
        dp = [0]*Length
        dp[0] = nums[0]
        dp[1] = max( nums[0], nums[1] )
        for i in range( 2, Length ):
            dp[i] = max( dp[i-2] + nums[i], dp[i-1] )
        
        #print(dp)
        return dp[-1]
