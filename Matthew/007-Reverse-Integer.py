class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >=0:
            x = int(str(x)[::-1])
            if x< 2**31-1:
                return (x)
            else:
                return(0)
        else:
            x = int(str(abs(x))[::-1])
            if -x > -(2**31):
                return (-x)
            else:
                return(0)
