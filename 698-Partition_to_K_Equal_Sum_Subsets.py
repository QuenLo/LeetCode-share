class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        
        total = sum(nums)
        n = len(nums)
        
        if total % k != 0:
            return False
        
        target = total // k
        
        nums.sort( reverse=True )
        used = ['0']*n
        
        memo = {}
        
        def backtrack( index, count, curr_sum ):
            
            used_str = "".join(used)
            
            if count == k-1:
                return True
            
            if curr_sum > target:
                return False
            
            if used_str in memo:
                return memo[ used_str ]
            
            if curr_sum == target:
                memo[used_str] = backtrack( 0, count+1, 0 )
                return memo[used_str]
            
            for j in range(index, n):
                if used[j] == '0':
                    used[j] = '1'
                    
                    if backtrack( j+1, count, curr_sum+nums[j] ):
                        return True
                    
                    used[j] = '0'
            
            memo[used_str] = False
            return memo[used_str]
        
        return backtrack( 0, 0, 0 )
