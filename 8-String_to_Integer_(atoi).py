class Solution:
    def myAtoi(self, s: str) -> int:
        
        positive, start = True, True
        cur_number = 0
        
        for s_char in s:
            
            if s_char == " " and start:
                continue
            
            elif s_char == "-" and start:
                positive = False
                start = False
            
            elif s_char == "+" and start:
                positive = True
                start = False
            
            elif s_char.isnumeric():
                cur_number = cur_number*10 + int(s_char)
                start = False
            
            else:
                break
                
        # out of the 32-bit signed integer range [-231, 231 - 1]
        if cur_number >= 2**31:
            return 2**31 - 1 if positive else -2**31
                
        return cur_number if positive else -1*cur_number
