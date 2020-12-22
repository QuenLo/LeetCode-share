class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        A.sort()
        NOW = A[-1] - A[0]
        
        for i in range( 0, len(A)-1, 1 ):
            NOW = min( NOW, max( A[i] + K, A[-1] - K ) - min( A[i+1] - K, A[0] + K ) )
        return NOW
