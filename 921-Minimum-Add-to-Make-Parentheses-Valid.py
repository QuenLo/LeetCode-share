class Solution(object):
    def minAddToMakeValid(self, S):

        Sstack = []
        Wrong = []
        for s in S:
            if s == "(":
                Sstack.append(s)
            elif s == ")":
                if len(Sstack) < 1:
                    Wrong.append(s)
                else:
                    Sstack.pop()
        
        return len(Sstack) + len(Wrong)
