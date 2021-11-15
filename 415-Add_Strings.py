class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        L1, L2 = len(num1), len(num2)
        if L1 > L2:
            num2 = "0"*(L1-L2) + num2
        elif L2 > L1:
            num1 = "0"*(L2-L1) + num1
        
        ans = []
        fix = 0
        for n1, n2 in zip(num1[::-1], num2[::-1]):
            temp = int(n1) + int(n2) + fix
            ans.append( str(temp % 10) )
            fix = temp // 10
            
        if fix != 0:
            ans.append(str(fix))
        
        # print(ans)
        return "".join(ans[::-1])
