## Two Pass
# Time: O(N)
# Space: O(N)
class SolutionI:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        
        odd = 1
        even = 0
        ans = [0]*len(nums)
        
        for num in nums:
            if num % 2:
                ans[odd] = num
                odd += 2
            else: 
                ans[even] = num
                even += 2
        
        return ans
      
## Read / Write Heads
# Time: O(N)
# Space: O(1)
class SolutionII:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        
        odd = 1
        for i in range(0,len(nums),2):
            if nums[i] % 2:
                while nums[odd] % 2:
                    odd+=2
                nums[odd], nums[i] = nums[i], nums[odd]
                
        return nums
