class Solution:
    def isHappy(self, n):
        res = 0
        HappyNum = [1,7]
        print(n)
        while ( n > 0 ):
            res += (n%10)**2
            n = n // 10
        
        if(res < 10):
            if res in HappyNum:
                return True
            else:
                return False
        
        return self.isHappy(res)
