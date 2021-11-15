class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n < 0:
            x = 1/x
            n = -1*n
        
        i = n
        ans = 1
        cur = x
        while i > 0:
            if ( i%2 ) == 1:
                ans *= cur
            cur *= cur
            i = i // 2
        
        return ans
            
