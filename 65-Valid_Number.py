class Solution:
    def isNumber(self, s: str) -> bool:
        
            
        seen_digit = seen_exp = seen_dot = False
        for i, c in enumerate(s):
            if c.isdigit():
                seen_digit = True
            elif c in ["+", "-"]:
                if i > 0 and s[i-1] not in ["e", "E"]:
                    return False
            elif c in ["e", "E"]:
                if seen_exp or not seen_digit:
                    return False
                seen_exp = True
                seen_digit = False
            elif c == ".":
                if seen_dot or seen_exp:
                    return False
                seen_dot = True
            else:
                return False
            
        return seen_digit
