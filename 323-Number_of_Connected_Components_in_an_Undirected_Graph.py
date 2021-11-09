from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        edge_col = defaultdict(list)
        for edge in edges:
                edge_col[edge[0]].append(edge[1])
                edge_col[edge[1]].append(edge[0])
            
        visited = [0]*n
        def dfs( cur ):
            visited[cur] = 1
            
            for nn in edge_col[cur]:
                if visited[nn] == 0:
                    dfs( nn )
        
        total = 0
        for i in range(n):
            if visited[i] == 0:
                total += 1
                dfs(i)
            
        return total
