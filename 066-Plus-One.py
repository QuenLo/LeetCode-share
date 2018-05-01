import math

class Solution(object):
    def plusOne(self, digits):

        AnsInt = 0
        Answer = []
        # switch to int
        for digit in digits:
            AnsInt = int(digit) + 10*AnsInt
        
        # plus one to int
        AnsInt += 1
        
        # switch back to List
        while AnsInt > 0 :
            Append_Temp = AnsInt % 10
            Answer.append(Append_Temp)
            AnsInt = AnsInt/10
        
        # The answer
        Answer.reverse()
        return Answer
        
