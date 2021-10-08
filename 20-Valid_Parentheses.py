class Solution:
    def isValid(self, s: str) -> bool:
        
        op = [ '(', '{', '[' ]
        cl = [ ')', "}", "]" ]
        
        stack = []
        for s_char in s:
            if s_char in op:
                stack.append(s_char)
            elif stack:
                end = stack[-1]
                if end == op[ cl.index(s_char) ]:
                    stack.pop(-1)
                else:
                    return False
            else:
                return False
        
        return not stack
