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

        skyline_Left = [max(Row) for Row in grid]
        skyline_Top = [max(Col) for Col in zip(*grid)]
        
        #print(skyline_Left)
        #print(skyline_Top)
        
        Total = 0
        for Row in range(0, RowLen):
            for Col in range(0, ColLen):
                Total += min(skyline_Left[Col],skyline_Top[Row]) - grid[Row][Col]
        
        return Total
