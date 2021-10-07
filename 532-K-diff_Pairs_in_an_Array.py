from collections import Counter

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        
        counter_nums = Counter(nums)
        ans = 0
        
        for c in counter_nums:
            if k > 0 and c+k in counter_nums:
                ans += 1
            elif k == 0 and counter_nums[c] > 1:
                ans += 1
                
        return ans
