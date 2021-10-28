## heap
# Time: O(NlogK)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        return heapq.nlargest(k, nums)[-1]

## sort
# Time: O(NlogN)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        return nums[-k]
