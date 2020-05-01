### Left and Right product lists ###
class Solution1:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = 1
        r = 1
        length = len(nums)
        ans = [1]*length
        
        for i in range( 0, length ):
            ans[i] *=l
            ans[length -i-1] *= r
            l *= nums[i]
            r *= nums[length-i-1]
            
        return ans
