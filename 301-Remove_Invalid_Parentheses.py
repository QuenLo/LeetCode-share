class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        
        ## count (, )
        left, right = 0, 0
        for ch in s:
            if ch == "(":
                left += 1
            elif ch == ")":
                right = right + 1 if left < 1 else right
                left = left - 1 if left > 0 else left
                
        result = set()
        def recurse( s, index, left_c, right_c, left_remain, right_remain, expr ):
            
            if index == len(s):
                # check valid
                if left_remain == 0 and right_remain == 0:
                    ans = "".join(expr)
                    result.add(ans)
            else:
                
                # too much
                if (s[index] == "(" and left_remain > 0) or (s[index] == ")" and right_remain > 0):
                    recurse( s, index+1, left_c, right_c, 
                            left_remain - (s[index]=="("),
                           right_remain - (s[index]==")"), expr)
                    
                expr.append(s[index])
                
                # not (, )
                if s[index] not in [ "(", ")" ]:
                    recurse( s, index+1, left_c, right_c, left_remain, right_remain, expr )
                    
                elif s[index] == "(":
                    recurse( s, index+1, left_c + 1, right_c, left_remain, right_remain, expr )
                
                elif s[index] == ")" and left_c > right_c:
                    recurse( s, index+1, left_c, right_c+1, left_remain, right_remain, expr )
                    
                expr.pop()
                
        recurse( s, 0, 0, 0, left, right, [] )
        return list(result)
