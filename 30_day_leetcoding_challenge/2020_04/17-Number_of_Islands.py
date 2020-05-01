class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
 
        total = 0
        y_length = len(grid)
        if not y_length: return 0
        x_length = len(grid[0])
        
        for y in range(y_length):
            for x in range(x_length):
                if grid[y][x] == "1":
                    total += 1
                    self.toOcean( grid, x, y, x_length, y_length )
                
        return total
    
    def toOcean( self, grid: List[List[str]], x, y, x_length, y_length ):
        if x < 0 or y < 0 or x >= x_length or y >= y_length or grid[y][x] == "0":
            return
        grid[y][x] = "0"
        self.toOcean( grid, x-1, y, x_length, y_length )
        self.toOcean( grid, x+1, y, x_length, y_length )
        self.toOcean( grid, x, y-1, x_length, y_length )
        self.toOcean( grid, x, y+1, x_length, y_length )
