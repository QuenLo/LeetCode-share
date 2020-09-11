class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        if len(nums) < 2: return nums[0]
        
        MAX = MAX_temp = Min_temp = nums[0]

        for num in nums[1:]:
            mt, min_t = MAX_temp, Min_temp
            MAX_temp = max( max( num, mt*num ), min_t*num )
            Min_temp = min( min( num, mt*num ), min_t*num )
            MAX = max( MAX , MAX_temp )
            
        return MAX
