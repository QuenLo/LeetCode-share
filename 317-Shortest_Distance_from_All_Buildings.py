class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        
        R = len(grid)
        C = len(grid[0])
        
        step_grid = [ [(0,0)] * C  for _ in range(R) ]
        
        seen = set()
        
        def bfs( r, c ):
            nonlocal seen, step_grid
            qu = []
            for nr, nc in [ (r+1,c), (r-1,c), (r,c+1), (r,c-1) ]:
                if (0<=nr<R) and (0<=nc<C) and grid[nr][nc] == 0:
                    qu.append( [nr, nc, 1] )
            
            while qu:
                
                cur_r, cur_c, cur_s = qu.pop(0)
                # print(qu, cur_r, cur_c, grid[cur_r][cur_c])
                if (cur_r, cur_c) not in seen:
                    step, house = step_grid[cur_r][cur_c]
                    step_grid[cur_r][cur_c] = ( cur_s + step, house + 1 )
                    seen.add( (cur_r,cur_c) )
                    for nr, nc in [ (cur_r+1,cur_c), (cur_r-1,cur_c), (cur_r,cur_c+1), (cur_r,cur_c-1) ]:
                        if (0<=nr<R) and (0<=nc<C) and grid[nr][nc] == 0 and (nr,nc) not in seen:
                            qu.append( [nr, nc, cur_s+1] )
        
        
        house = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    bfs(r, c)
                    # print(step_grid)
                    house += 1
                    seen = set()
        
        mini = float("inf")
        for r in range(R):
            for c in range(C):
                if step_grid[r][c][1] == house and grid[r][c] == 0:
                    mini = min( step_grid[r][c][0], mini )
        
        return mini if mini != float('inf') else -1
