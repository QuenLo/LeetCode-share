class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        dp = [1]*len(nums)
        
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max( dp[i], dp[j]+1 )
                    
        return max(dp)

class SolutionII:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        sub = []
        for num in nums:
            i = bisect_left(sub, num)
            
            if i == len(sub):
                sub.append(num)
                
            else:
                sub[i] = num
                
        return len(sub)
