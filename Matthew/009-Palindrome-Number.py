class Solution:
    def xlen(self, x):
        n = 1
        while(x>=10):
            n += 1
            x /= 10
        return (n)
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:return (False)
        else:
            ori = x
            n = self.xlen(x)
            newx = 0
            for z in range(n,0,-1):
                a = x//(10**(z-1))
                b = a*(10**(n-z))
                newx += b
                x -= a*(10**(z-1))  
            if ori == newx: return (True)
            else:return (False)

