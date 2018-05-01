import math

class Solution(object):
    def plusOne(self,digits):

        AnsInt = 0
        Answer = []
        
        if digits[-1] < 9 :
            if len(digits) > 1:
                return digits[:-1] + [digits[-1]+1]
            else :
                return [digits[-1]+1]
        else :
            if len(digits) > 1:
                return plusOne(digits[:-1]) + [0]
            else :
                return [1,0]
