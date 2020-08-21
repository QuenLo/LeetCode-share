class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        
        
        if len(A) <2:
            return A
        
        s, f = -1, 0
        while f < len(A):
            if A[f]%2 == 0:
                s += 1
                A[s], A[f] = A[f], A[s]
            f += 1
            
        return A

class SolutionII:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        odd_L = []
        even_L = []
        
        for a in A:
            if a%2:
                odd_L.append(a)
            else:
                even_L.append(a)
                
        return even_L + odd_L
