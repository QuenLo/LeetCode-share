from collections import defaultdict, deque

# Time Complexity: O(V + E) where V represents the number of vertices and E represents the number of edges.
# Space Complexity: O(V + E)
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        required = collections.defaultdict(list)
        allow = collections.defaultdict(int)
        
        for pre in prerequisites:
            required[pre[1]].append(pre[0])
            
            allow[pre[0]] += 1
            
        c_order = []
        zero_queue = deque( [ k for k in range(numCourses) if k not in allow ] )
        
        while zero_queue:
            
            v = zero_queue.popleft()
            c_order.append(v)
            
            for nn in required[v]:
                allow[nn] -= 1

                if allow[nn] == 0:
                    zero_queue.append(nn)
                    
        return c_order if len(c_order) == numCourses else []
            
class SolutionII:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # WHITE: 1, GRAY: 2, BLACK: 3
        
        course_col = collections.defaultdict(list)
        
        for nex, pre in prerequisites:
            course_col[pre].append(nex)
            
        ans = []
        is_possible = True
        
        state = { k: 1 for k in range(numCourses) }
        
        def dfs( c ):
            nonlocal is_possible
            
            if not is_possible:
                return
            
            state[c] = 2
            if c in course_col:
                for nex in course_col[c]:
                    if state[nex] == 1:
                        dfs( nex )
                    elif state[nex] == 2:
                        # is a cycle
                        is_possible = False
            
            state[c] = 3
            ans.append(c)
            
        for v in range(numCourses):
            if state[v] == 1:
                dfs(v)
                
        return ans[::-1] if is_possible else []
