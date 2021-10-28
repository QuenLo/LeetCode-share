class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        
        N = len(grid)
        
        def neighbors(r,c):
            valid_n = []
            for nr, nc in ( (r+1,c), (r-1,c), (r,c+1), (r,c-1) ):
                if 0 <= nr < N and 0 <= nc < N:
                    valid_n.append( (nr, nc) )
            return valid_n
                    
        def dfs( r, c, ind ):
            space = 1
            grid[r][c] = ind
            for nr, nc in neighbors(r,c):
                if grid[nr][nc] == 1:
                    space += dfs( nr, nc, ind )
            return space
        
        ind = 2
        area = {}
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 1:
                    area[ind] = dfs( r, c, ind )
                    ind += 1
        
        
        ans = max( area.values() or [0] )
        
        # get one to 1
        for r in range(N):
            for c in range(N):
                seen = {}
                if grid[r][c] == 0:
                    for nr, nc in neighbors(r,c):
                        if grid[nr][nc] > 1:
                            seen[ grid[nr][nc] ] = area[ grid[nr][nc] ]
                    ans = max( ans, 1+sum(seen.values()) )
        return ans
