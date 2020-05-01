# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    
    def firstBadVersion(self, n):
        MAX = n
        MIN = 1
        
        while MAX >= MIN:
            MID = (MAX+MIN)//2
            #bad
            if isBadVersion(MID):
                MAX = MID - 1
            #good
            else:
                MIN = MID + 1
                
        return MAX+1
