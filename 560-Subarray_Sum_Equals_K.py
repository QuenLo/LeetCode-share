## Hash mpa
# Time: O(n)
import collections
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        ans_count = 0
        sum_int = 0
        hash_map = collections.defaultdict(int)
        hash_map[0] = 1
        for num in nums:
            sum_int += num
            ans_count += hash_map[ sum_int-k ]
            hash_map[sum_int] += 1
        
        return ans_count

## Using Cumulative Sum (Time Limited)
# Time: O(n^2)
class SolutionI:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        ans_count = 0
        sum_array = [0]*(len(nums)+1)
        for i in range(1,len(nums)+1):
            sum_array[i] = sum_array[i-1] + nums[i-1]
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)+1):
                if (sum_array[j] - sum_array[i]) == k:
                    ans_count += 1
        
        return ans_count


## Brute Force (Time Limited)
# Time: O(n^3)
class SolutionII:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        ans_count = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)+1):
                if sum(nums[i:j]) == k:
                    ans_count += 1
        
        return ans_count
