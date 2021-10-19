class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        
        # is 0
        if not numerator or not denominator:
            return "0"
        
        ans = ""
        
        # negative
        if (numerator < 0) != (denominator < 0):
            ans += '-'
            
        # to positive
        numerator = abs( numerator )
        denominator = abs( denominator )
        
        remainder = numerator % denominator
        ans += str(numerator // denominator)
        
        # whole integer
        if remainder == 0 :
            return ans
        
        
        ans += "."
        remainder_hash = {}
        
        while remainder != 0:
            if remainder in remainder_hash:
                ans = ans[:remainder_hash[remainder]] + "(" + ans[remainder_hash[remainder]:] + ")"
                break
            
            remainder_hash[remainder] = len(ans)
            
            remainder *= 10
            ans += str(remainder // denominator)
            
            remainder %= denominator
            
        return ans
