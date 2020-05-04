class Solution1:
    def findComplement(self, num: int) -> int:
        
        n = num
        flip = 1
        
        while n > 1:
            n = n >> 1
            flip = (flip << 1) | 1
            
        return num ^ flip
        
class Solution2:
    def findComplement(self, num: int) -> int:
        
        num_bin = bin(num)[2:]
        ans_str = ""
        
        for n in num_bin:
            ans_str += str(1-int(n))
            
        return int(ans_str, 2)
        
class Solution3:
    def findComplement(self, num: int) -> int:
        
        num_bit = bin(num)
        #ans_str = ''.join([ str(1-int(n)) for n in num_bit[2:] ])
        ans_str = ''.join([ '0' if n == '1' else '1' for n in num_bit[2:] ])
        
        return int( ans_str, 2 )
        
class Solution4:
    def findComplement(self, num: int) -> int:
        
        num_bit = []
        # if num == 0:
        #     return 1
        
        while(num > 0):
            num_bit.append(num%2)
            num = num // 2
            
        n_len = len(num_bit)
        ans = 0
        for n in range(n_len):
            if num_bit[n] == 0:
                ans += pow(2,n)
                
        return ans
