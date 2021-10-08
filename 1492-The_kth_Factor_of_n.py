class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        
        def heappush_k(num):
            heappush( heap, -num )
            if len(heap) > k:
                heappop(heap) #throw out largest one (-num the mininum)
             
        heap = []    
        for x in range( 1, int(n**0.5)+1 ):
            if n % x == 0:
                heappush_k(x)
                if n // x != x:
                    heappush_k( n//x )
                    
        return -heappop(heap) if len(heap) == k else -1
