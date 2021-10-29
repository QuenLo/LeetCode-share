class Solution:
    def calculate(self, s: str) -> int:
        
        if len(s) < 1: return 0
        currN, lastN, result = 0, 0, 0
        length = len(s)
        operate = "+"
        
        for i in range(length):
            if s[i].isdigit():
                currN = currN*10 + int(s[i])
            
            if( not s[i].isdigit() and s[i] != " " ) or (i == length-1):
                if operate in ["-", "+"]:
                    result += lastN
                    if operate == "-":
                        lastN = -1*currN
                    else:
                        lastN = currN
                elif operate == "*":
                    lastN *= currN
                elif operate == "/":
                    if lastN < 0:
                        lastN = -1*(-1*lastN//currN)
                    else:
                        lastN //= currN
                
                operate = s[i]
                currN = 0
        
        result += lastN
        return result
