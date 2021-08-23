class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        
        # first
        First = abs( (ax2 - ax1)*(ay2 - ay1) )
        
        # second
        Second = abs( (bx2 - bx1)*(by2 - by1) )
        
        # both
        weight, height = 0, 0
        if bx1 <= ax2 and bx1 >= ax1:
            if bx2 <= ax2:
                weight = bx2 - bx1
            else: weight = ax2 - bx1
        elif bx2 >= ax1 and bx2 <= ax2:
            weight = bx2 - ax1
        elif ax1 >= bx1 and ax2 <= bx2:
            weight = ax2 - ax1
        
        if by2 >= ay1 and by2 <= ay2:
            if by1 <= ay1:
                height = by2 - ay1
            else: height = by2 - by1
        elif by1 <= ay2 and by1 >= ay1:
            height = ay2 - by1
        elif ay1 >= by1 and ay2 <= by2:
            height = ay2 - ay1
            
        Both = abs( height*weight )
                
        return First + Second - Both
      
class SolutionII:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        
        # first
        First = abs( (ax2 - ax1)*(ay2 - ay1) )
        
        # second
        Second = abs( (bx2 - bx1)*(by2 - by1) )
        
        # both
        weight = min( ax2, bx2 ) - max( ax1, bx1 )
        height = min( ay2, by2 ) - max( ay1, by1 )
        
        if weight > 0 and height > 0:
            Both = abs( height*weight )
        else: Both = 0
                
        return First + Second - Both
