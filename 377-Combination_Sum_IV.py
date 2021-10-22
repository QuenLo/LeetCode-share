class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        dp = [0]*(target+1)
        dp[0] = 1
        nums.sort()
        
        for sub_sum in range(target+1):
            for num in nums:
                if sub_sum - num >= 0:
                    dp[ sub_sum ] += dp[ sub_sum-num ]
                else:
                    break
        
        return dp[target]
