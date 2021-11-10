class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        
        lr = len(grid)
        lc = len(grid[0])
        
        # where am I
        find = False
        for r in range(lr):
            for c in range(lc):
                if grid[r][c] == '*':
                    find = True
                    me = (r, c)
                    break
            if find:
                break
                
        state = ( 0, me )
        visited = set([me])
        #Visited = [[False for j in range(lc)] for i in range(lr)]
        b_qu = [ state ]
        
        while b_qu:
            step, (r,c) = b_qu.pop(0)
            
            if grid[r][c] == '#':
                return step
            
            for n_r, n_c in [ (r-1, c), (r+1,c), (r,c+1), (r,c-1) ]:
                if 0<=n_r<lr and 0<=n_c<lc:
                    if grid[n_r][n_c] != 'X' and (n_r,n_c) not in visited:
                        visited.add( (n_r,n_c) )
                        b_qu.append( ( step+1, (n_r,n_c) ) )
                        
        return -1
        
