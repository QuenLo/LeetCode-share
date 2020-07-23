class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        ans = []
        
        for i in nums:
            if i in ans:
                ans.remove(i)
            else:
                ans.append(i)
                
        return ans
