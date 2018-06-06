class Solution(object):
    def uniquePaths(self, m, n):
        
        # there's the only way when row is less than two
        if n < 2:
            return 1
        
        # The number of steps is the number of row/column minus one
        top = m + n -2
        down = n -1
        
        # count permutations
        for i in range(1,(n-1)):
            top *= (m+n-2-i)
            down *= (n-1-i)
    
        return top/down
