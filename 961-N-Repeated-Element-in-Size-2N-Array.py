class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        uni = []
        for i in A:
            if i not in uni:
                uni.append(i)
            else:
                return i
                
# use N-Repeated
class SolutionII:
    def repeatedNTimes(self, A: List[int]) -> int:
        Length = len(A)
        A.sort()
        if( A[0] == A[1] ):
            return A[0]
        elif( A[Length-1] == A[Length-2] ):
            return A[Length -1]

        return A[(Length)//2]
        
# use counter
class SolutionIII:
    def repeatedNTimes(self, A: List[int]) -> int:
        count = collections.Counter(A)
        for k in count:
            if count[k] > 1:
                return k
                
# Random Solution
class SolutionIIV:
    def repeatedNTimes(self, A: List[int]) -> int:
        while 1:
            s = random.sample(A,2)
            if s[0] == s[1]:
                return s[0]
