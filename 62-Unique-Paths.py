class Solution(object):
    def uniquePaths(self, m, n):
        
        if n < 2:
            return 1
        
        top = m + n -2
        down = n -1
        
        for i in range(1,(n-1)):
            top *= (m+n-2-i)
            down *= (n-1-i)
    
        return top/down
