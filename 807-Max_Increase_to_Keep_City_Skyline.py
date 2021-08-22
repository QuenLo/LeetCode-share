class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        
        total_height = 0
        row_max = []
        column_max = []
        
        for x, x_list in enumerate(grid):
            row_max.append( max(x_list) )
            c_max = 0
            
            for y in range( len(grid) ):
                if grid[y][x] > c_max:
                    c_max = grid[y][x]
            column_max.append( c_max )
            
            
        for i in range( len(grid) ):
            for y in range( len(grid) ):
                
                total_height += min(row_max[i], column_max[y])  - grid[i][y]
                
        return total_height
