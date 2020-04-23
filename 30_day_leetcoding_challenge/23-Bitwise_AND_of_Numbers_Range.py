class Solution1:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        while(m < n ):
            n &= (n-1)
        
        return m & n
        
class Solution2:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        mini = 2147483647
        while( (m & mini) != (n & mini) ):
            mini <<= 1
        
        return m & mini
