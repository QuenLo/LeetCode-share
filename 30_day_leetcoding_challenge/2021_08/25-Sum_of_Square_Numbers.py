class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        squ_list = []
        squ = int(c**0.5)
        while squ >= 0:
            lef = c - squ*squ
            b_lef = math.sqrt( lef )
            if b_lef == int(b_lef):
                return True
            squ -= 1
        # print( squ_list )
            
        return False
