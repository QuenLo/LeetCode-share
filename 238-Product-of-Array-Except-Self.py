# -----------------------------------------------
# v1 solution (70.66%) --------------------------
# -----------------------------------------------

class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def productExceptSelf(self, nums):
        
        # count len of nums[]
        n = len(nums)
        
        output = []
        left2right=[]
        right2left=[]
        tmpnumL = 1
        tmpnumR = 1
        
        # multiply left to right and right to left
        for i in range(0,n):
            left2right.append(tmpnumL)
            tmpnumL = tmpnumL * nums[i]
            
            right2left.append(tmpnumR)
            tmpnumR = tmpnumR * nums[(n-1)-i]
            
        # multiply each
        for i in range(0,n):
            output.append( right2left[(n-1)-i] * left2right[i] )
        
        return output
        
# -----------------------------------------------
# v2 solution (84.95%) --------------------------
# -----------------------------------------------

class Solution2:
    # @param {integer[]} nums
    # @return {integer[]}
    def productExceptSelf(self, nums):
        
        # count len of nums[]
        n = len(nums)
        
        output = [1] * n
        tmpnumL = 1
        tmpnumR = 1
        
        # multiply left to right
        for i in range(0,n-1):
            tmpnumL = tmpnumL * nums[i]
            output[i+1] = tmpnumL
            
        # multiply right to left
        for i in range((n-1),0,-1):
            tmpnumR = tmpnumR * nums[i]
            output[i-1] *= tmpnumR 
        
        return output
