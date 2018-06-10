class Solution:
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        connected = [[-1 for n in range(len(grid))] for n in range(len(grid[0]))]
        connected[0][0] = grid[0][0]
        pending = {'0_0':grid[0][0]}
        
        for n in range(len(grid)*len(grid[0])):
            site, height= min(pending.items(), key=lambda x: x[1])
            del pending[site]
            site = [int(n) for n in site.split('_')]
            connected[site[0]][site[1]] = height
            self.check_four_direction(site, height, grid, connected, pending)
        return (connected[len(grid)-1][len(grid[0])-1])
    
    def check_four_direction(self, site, height, grid, connected, pending):
        if site[0]>0 and connected[site[0]-1][site[1]] == -1:
            pending[str(site[0]-1)+'_'+str(site[1])] = max(grid[site[0]-1][site[1]], height)
        if site[1]>0 and connected[site[0]][site[1]-1] == -1:
            pending[str(site[0])+'_'+str(site[1]-1)] = max(grid[site[0]][site[1]-1], height)
        if site[0]<len(grid)-1 and connected[site[0]+1][site[1]] == -1:
            pending[str(site[0]+1)+'_'+str(site[1])] = max(grid[site[0]+1][site[1]], height)
        if site[1]<len(grid[0])-1 and connected[site[0]][site[1]+1] == -1:
            pending[str(site[0])+'_'+str(site[1]+1)] = max(grid[site[0]][site[1]+1], height)
