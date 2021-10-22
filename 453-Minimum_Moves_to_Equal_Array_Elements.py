class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return sum(nums)-len(nums)*min(nums)


class SolutionII:
    def minMoves(self, nums: List[int]) -> int:
        
        minin = float('inf')
        time = 0
        for num in nums:
            time += num
            minin = min( minin, num )
        
        return time - len(nums)*minin
