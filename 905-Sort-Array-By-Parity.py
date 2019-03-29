class Solution(object):
    def sortArrayByParity(self, A):
        Ans = []
        for a in A:
            if a%2:
                Ans.append(a)
            else:
                Ans.insert(0,a)
        
        return Ans
        
# solution by sort
class Solution_sort(object):
    def sortArrayByParity(self, A):
        A.sort( key= lambda a : a%2 )
        
        return A
        
# solution by two pass        
class Solution_two(object):
    def sortArrayByParity(self, A):
        Ans = [ x for x in A if x % 2 == 0 ] + [ x for x in A if x % 2 == 1 ]
        return Ans
        
        
# solution by two list        
class Solution_list(object):
    def sortArrayByParity(self, A):
        even, odd = [], []
        for a in A:
            if a % 2: odd.append(a)
            else: even.append(a)
        return even + odd
        
        
# solution by in-place
class Solution_in_place(object):
    def sortArrayByParity(self, A):
        l,r = 0, len(A) -1
        while l < r:
            if A[l] % 2 > A[r] % 2:
                A[l], A[r] = A[r], A[l]
                l += 1
                r -= 1
            elif A[l] % 2 == 0:
                l += 1
            elif A[r] % 2 == 1:
                r -= 1
        return A
