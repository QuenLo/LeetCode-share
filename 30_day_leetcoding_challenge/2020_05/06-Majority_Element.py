
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        nums_c = Counter(nums)
        return max( nums_c.keys(), key = nums_c.get )
