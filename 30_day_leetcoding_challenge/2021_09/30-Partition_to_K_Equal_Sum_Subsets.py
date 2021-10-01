class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        
        total = sum(nums)
        if (total % k) > 0: return False
        
        sub_total = total // 4
        visited = [False]*len(nums)
        nums = sorted(nums)
        
        return self.calling( nums, visited, 0, k, sub_total )
    
    def calling( self, nums, visited, cur_sum, k, sub_total ):
        
        if k == 1: return True
        if (sub_total < cur_sum): return False
        if cur_sum == sub_total: return self.calling( nums, visited, 0, k-1, sub_total )
        for i in range( len(nums) ):
            if visited[i]: continue
            visited[i] = True
            if ( self.calling( nums, visited, cur_sum+nums[i], k, sub_total ) ): return True
            visited[i] = False
        
        return False
