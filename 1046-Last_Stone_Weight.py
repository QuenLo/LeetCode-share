class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        import heapq
        
        for i in range( len(stones) ):
            stones[i] *= -1 
        
        heapq.heapify(stones)
        
        while len(stones) > 1:
            
            largest = heapq.heappop( stones )
            largest_2 = heapq.heappop( stones )
            if largest != largest_2:
                heapq.heappush( stones, (largest-largest_2) )
            
        return -stones[0] if stones else 0
