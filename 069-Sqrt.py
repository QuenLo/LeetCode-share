class Solution:
    def mySqrt(self, x):

        high = x
        low = 1
        
        if x == 0:
            return 0
        
        # digit-by-digit calculation
        while high - low > 1:
            mid = (low + high)//2
            #print("+++ ",mid)
            if mid**2 > x:
                high = mid
            else:
                low = mid

        return low
