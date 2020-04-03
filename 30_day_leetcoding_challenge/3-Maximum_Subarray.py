class Solution1:
    def maxSubArray(self, nums: List[int]) -> int:
        total_max, total  = -1e10, 0

        for i in range( len(nums) ):
            if total > 0:
                total += nums[i]
            else:
                total = nums[i]
                
            if total > total_max:
                total_max = total
                
        return total_max

class Solution2:
##  divide and conquer approach
    def middlemax( self, nums, LL, mid, RR ):
        totalL, totalR, totalL_max, totalR_max = 0, 0, nums[mid], nums[mid+1]
        # Left
        for i in range( mid, LL-1, -1 ):
            totalL += nums[i]
            
            if( totalL_max < totalL ):
                totalL_max = totalL
        
        # Right
        for i in range( mid+1, RR+1 ):
            totalR += nums[i]
            
            if( totalR_max < totalR ):
                totalR_max = totalR
                
        return totalR_max + totalL_max
    
    def findmax( self, nums, LL, RR ):
        if LL >= RR:
            return nums[LL]
        
        mid = LL + (RR-LL)//2

        mmax = self.middlemax( nums, LL, mid, RR )
        lmax = self.findmax( nums, LL, mid )
        rmax = self.findmax( nums, mid+1, RR )
        
        return max( [mmax, lmax, rmax] )
    
    def maxSubArray(self, nums: List[int]) -> int:
        Length = len(nums)

        return self.findmax( nums, 0, Length-1 )
    

        
