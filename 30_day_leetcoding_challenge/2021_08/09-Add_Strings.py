class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        output = ""
        vex, res = 0, 0
        
        Max = num2 if len(num2) > len(num1) else num1
        
        for index in range( 1, min(len(num1), len(num2))+1 ):
            total = int( num1[-index] ) + int( num2[-index] ) + vex
            vex = total // 10
            res = total % 10
            output = str( res ) + output
        
        Max = Max[:-(len(output))]
        for i in Max[::-1]:
            total = int( i ) + vex
            vex = total // 10
            res = total % 10
            output = str( res ) + output
        
        if vex != 0: return str(vex) + output
        return output
