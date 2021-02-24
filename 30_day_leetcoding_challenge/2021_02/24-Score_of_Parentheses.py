class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        
        stack, score = [], 0
        for s in S:
            if s == '(':
                stack.append("(")
            else:
                last = stack[-1]
                if last == '(':
                    stack.pop()
                    stack.append(1)
                    
                # nothing to match
                else:
                    count = 0
                    while stack[-1] != '(':
                        count += stack.pop()
                    stack.pop()
                    stack.append( count*2 )
        
        return sum(stack)
