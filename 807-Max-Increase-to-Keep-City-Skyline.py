class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        skyline_Top = []
        skyline_Left = []
        RowLen = len(grid)
        ColLen = len(grid[0])
        
        for Row in range(0,RowLen):
            Max = 0
            for Col in range(0,ColLen):
                Max = max(Max,grid[Row][Col])
            skyline_Left.append(Max)
        
        
        for Col in range(0,ColLen):
            Max = 0
            for Row in range(0,RowLen):
                Max = max(Max,grid[Row][Col])    
            skyline_Top.append(Max)
        
        
        #print(skyline_Left)
        #print(skyline_Top)
        
        Total = 0
        for Row in range(0, RowLen):
            for Col in range(0, ColLen):
                Total += min(skyline_Left[Col],skyline_Top[Row]) - grid[Row][Col]
        
        return Total
