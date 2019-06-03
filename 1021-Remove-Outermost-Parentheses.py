class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        out = []
        count = 0
        for s in S:
            if s == ')':
                count -= 1
            if count > 0:
                out.append(s)
            if s == '(':
                count += 1
        return "".join(out)
        
        
class SolutionII:
    def removeOuterParentheses(self, S: str) -> str:
        out = []
        count = 0
        for s in S:
            if s == '(' and count > 0: out.append(s)
            elif s == ')' and count > 1: out.append(s)
            count += 1 if s == '(' else -1
        return "".join(out)
