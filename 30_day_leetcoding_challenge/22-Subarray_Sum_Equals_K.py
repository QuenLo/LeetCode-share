### Using hashmap ###
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        sum_from_head = {}
        Sum = 0
        total = 0
        for i in range(len(nums)):
            Sum += nums[i]
            if Sum == k:
                total += 1
            total += sum_from_head.get( Sum-k, 0 )
            sum_from_head[Sum] = sum_from_head.get( Sum, 0 ) + 1

        return total
        

### Without space [Time Limit Exceeded] ###
class Solution2:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        total = 0
        for start in range( len(nums) ):
            SUM = 0
            for end in range( start, len(nums) ):
                SUM += nums[end]
                if SUM == k:
                    total += 1
            
        return total
