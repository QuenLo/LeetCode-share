class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        ans = 1
        m -= 1
        n -= 1
        if m < n:
            m, n = n, m
        numerator = [x for x in range(m+1, m+n+1)]
        denominator = [x for x in range(1, n+1)]
        for z in range(len(numerator)):
            ans *= numerator[z]
            ans /= denominator[z]
        return int(ans)
