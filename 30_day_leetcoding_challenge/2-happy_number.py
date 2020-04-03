class Solution1:
    def isHappy(self, n: int) -> bool:
        next_list = []
        
        while n != 1:
            next_n = 0
            
            while(n):
                next_n += (n%10) * (n%10)
                n = n // 10
            
            n = next_n
            
            if n not in next_list:
                next_list.append( n )
            else:
                break

        return n == 1

class Solution2:
    def isHappy(self, n: int) -> bool:
        next_list = [n]
        
        while True:
            next_n = sum( [ int(d)**2 for d in str(n) ] )
            if next_n == 1:
                return True
            elif next_n in next_list:
                return False
            else:
                next_list.append( next_n )
                n = next_n
