class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        
        lr = len(grid)
        lc = len(grid[0])
        target = ( lr-1, lc-1 )
        
        if k >= lr + lc -2:
            return lr + lc -2
        
        
        visited = set([(0, 0, k)])
        b_qu = collections.deque([ (0, (0, 0, k)) ])
        
        while b_qu:
            
            step, ( r, c, k ) = b_qu.popleft()
            if (r, c) == target:
                return step
            
            for n_r, n_c in [(r-1,c), (r+1,c), (r,c+1), (r,c-1)]:
                if ( 0 <= n_r < lr ) and ( 0<=n_c<lc ):
                    cur_k = k - grid[n_r][n_c]
                    new_state = ( n_r, n_c, cur_k )
                    if cur_k >= 0 and new_state not in visited:
                        visited.add( new_state )
                        b_qu.append( ( step+1, new_state ) )
                    
        return -1
      
      # By exploring, we refer to the BFS strategy, rather than DFS. The BFS algorithm works like detecting an object with sonar. 
      # A sound wave propagages in all directions with equal speed. At any given moment, 
      # all the objects that the sound wave reaches have the same distance to the source of the sound. 
      # On the other hand, as soon as the sound wave reaches the object, the path is guaranteed to be the shortest, 
      # since the distance is proportional to the time, the more time it takes, the longer the distance is.
