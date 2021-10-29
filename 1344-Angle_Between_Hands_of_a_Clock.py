class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        
        # mins
        mins_a = minutes*(360/60)
        
        # hours
        hours_a = hour*(360/12) + (360/12)*(minutes/60)
        
        # print( mins_a, hours_a )
        sub = abs(mins_a-hours_a)
        
        return min( sub, 360-sub )
