class Solution(object):
    def flipAndInvertImage(self, A):
        Ans = []
        for a in A:
            LEN = len(a)
            row = []
            for i in range(LEN):
                row.append( [1,0][a[LEN-1-i]] )
            Ans.append(row)
        return Ans


class SolutionII(object):
    def flipAndInvertImage(self, A):
        for a in A:
            l,r = 0, len(a) - 1
            while l <= r:
                if a[l] == a[r]:
                    a[l],a[r] = a[l]^1, a[r]^1
                l += 1
                r -=1
        return A
        
class SolutionIII(object):
    def flipAndInvertImage(self, A):

        for row in A:
            for i in range((len(row)+1) / 2):
                if( row[i] == row[~i] ):
                    row[i], row[~i] = row[~i]^1, row[i]^1
        return A
