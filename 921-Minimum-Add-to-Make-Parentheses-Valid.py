class Solution(object):
    def minAddToMakeValid(self, S):

        Sstack = 0
        Wrong = 0
        for s in S:
            if s == "(":
                Sstack += 1
            elif s == ")":
                if Sstack < 1:
                    Wrong += 1
                else:
                    Sstack -= 1
        
        return Sstack + Wrong
