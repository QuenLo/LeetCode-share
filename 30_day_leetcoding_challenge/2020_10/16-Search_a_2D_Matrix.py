class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        Y = len(matrix)
        if Y == 0: return False
        
        X = len(matrix[0])
        if X == 0: return False
        lo, height = 0, Y*X-1
        
        #binary
        while lo <= height:
            
            #get value
            pos = (lo + height) //2
            matrix_num = matrix[ pos//X ][ pos%X ]
            if matrix_num == target:
                return True
            if matrix_num < target:
                lo = pos + 1
            else:
                height = pos - 1
                
        return False
