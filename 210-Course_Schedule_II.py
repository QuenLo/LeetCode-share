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
            
