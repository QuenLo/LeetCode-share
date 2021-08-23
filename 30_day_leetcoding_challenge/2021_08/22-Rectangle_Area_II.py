class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
         
            def helper( All, cur, start ):
                if len(All) <= start:
                    All.append( cur )
                    return
                
                rec = All[start]
                
                # seperate
                if ( cur[0] >= rec[2] or cur[2] <= rec[0] or cur[1] >= rec[3] or cur[3] <= rec[1] ):
                    helper( All, cur, start+1 )
                    return
                
                # overlap
                if rec[0] > cur[0]:
                    helper( All, [ cur[0], cur[1], rec[0], cur[3] ], start+1 )
                    
                if rec[2] < cur[2]:
                    helper( All, [ rec[2], cur[1], cur[2], cur[3] ], start+1 )
                    
                if cur[1] < rec[1]:
                    helper( All, [ max( rec[0], cur[0] ), cur[1], min(cur[2], rec[2]), rec[1] ], start+1 )
                    
                if cur[3] > rec[3]:
                    helper( All, [ max( rec[0], cur[0] ), rec[3], min( cur[2], rec[2] ), cur[3] ], start+1 )
                    
            All = []
            for rectangle in rectangles:
                helper( All, rectangle, 0 )
            
            total = 0
            print( All )
            for a in All:
                total += abs( (a[2]-a[0])*(a[3]-a[1]) ) 
            
            return total % ( 10**9 + 7 )
            
            
                    
