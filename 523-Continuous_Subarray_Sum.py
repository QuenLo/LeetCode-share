class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        if len(nums) < 2:
            return False
        
        reminder = {0:-1}
        total = 0
        
        for ind, num in enumerate(nums):
            
            total += num
            remind = total % k
            if remind in reminder and ind - reminder[remind] >= 2:
                return True
            if remind not in reminder:
                reminder[remind] = ind
                
        return False
