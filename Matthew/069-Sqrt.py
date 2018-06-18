class Solution:
    def mySqrt(self, x, init=1):
        """
        :type x: int
        :rtype: int
        """
        if abs(init**2 - x) < 1:
            return int(init)
        else:
            return self.mySqrt(x, init - (init**2 - x)/(2*init))
