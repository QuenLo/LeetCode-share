class Solution:
    def maxDistToClosest(self, seats):

        spacetmp = 0
        space = 0
        
        for seat in seats:
            if seat == 0:
                spacetmp += 1
            if seat != 0:
                space = max(space,spacetmp)
                spacetmp = 0
        
        return max( int(math.floor((space+1)/2)) , seats.index(1) , seats[::-1].index(1) )
