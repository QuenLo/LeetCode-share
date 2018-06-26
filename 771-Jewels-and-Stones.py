class Solution:
    def numJewelsInStones(self, J, S):
        
        countnum = 0
          
        for stone in S:
            if stone in J:
                countnum += 1
                
        return countnum
