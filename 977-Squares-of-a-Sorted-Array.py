# Time Complexity: O(NlogN), where N is the length of A.
# Space Complexity: O(N)O(N).

class SolutionIII:
    def sortedSquares(self, A: List[int]) -> List[int]:
        #B = [ a*a for a in A ]
        #B.sort()
        return sorted( [ a*a for a in A ] )



# Space Complexity: O(N)
# Time Complexity: O(N), where N is the length of A.

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        Ans = collections.deque()
        r,l = len(A)-1, 0
        while( l <= r ):
            left, right = A[l]**2, A[r]**2
            if left > right:
                Ans.appendleft( left )
                l += 1
            else:
                Ans.appendleft( right )
                r -= 1
        
        return list(Ans)
        
# list
class SolutionII:
    def sortedSquares(self, A: List[int]) -> List[int]:
        Ans = [0]*(len(A))
        r,l = len(A)-1, 0
        while( l <= r ):
            left, right = A[l]**2, A[r]**2
            if left > right:
                Ans[r-l] = left
                l += 1
            else:
                Ans[r-l] = right
                r -= 1
        
        return Ans
