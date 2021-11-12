# You must write an algorithm that runs in O(n) time and without using the division operation.
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        N = len(nums)
        ans = [0]*N
        
        ans[0] = 1
        for i in range(1, N):
            ans[i] = ans[i-1]*nums[i-1]
            
        K = 1
        for i in range(N-1, -1, -1):
            ans[i] = ans[i]*K
            K *= nums[i]
            
        return ans
