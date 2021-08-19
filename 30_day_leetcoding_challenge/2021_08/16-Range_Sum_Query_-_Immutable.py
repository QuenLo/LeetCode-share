## Sol: prefix sum
# Time: O(1) time per query, O(n)O(n) time pre-computation
# Space: O(N)
class NumArray:
    
    presum = []
    
    def __init__(self, nums: List[int]):
        
        self.presum = [0]
        for index, num in enumerate(nums):
                num += self.presum[index]
                self.presum.append( num )
    
        
    def sumRange(self, left: int, right: int) -> int:
        return self.presum[right+1] - self.presum[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
