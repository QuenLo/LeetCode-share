## Binary Sort
# Time: O(nlog(MAX-MIN))
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        def countless(value):
            
            total = 0
            N = len(matrix)
            i, j = 0, N-1
            while i < N and j >= 0:
                if matrix[i][j] <= value:
                    total += j+1
                    i += 1
                else:
                    j -= 1
            
            return total
        
        
        start = matrix[0][0]
        end = matrix[-1][-1]
        
        while start < end:
            mid = (start+end) // 2
            # print(mid, countless(mid))
            if countless(mid) < k:
                start = mid+1
            else:
                end = mid
                
        if countless( start ) >= k:
            return start
        else:
            return end

## HEAP
# Time Complexity: let X=min(K,N); X+Klog(X)
# Space: O(X)

import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        N = len(matrix)
        
        minHeap = []
        for r in range(min(k, N)):
            minHeap.append( (matrix[r][0], r, 0) )
            
        heapq.heapify(minHeap)
        
        while k:
            element, r, c = heapq.heappop(minHeap)
            
            if c < N-1:
                heapq.heappush( minHeap, (matrix[r][c+1], r, c+1) )
            
            k -= 1
            
        return element
