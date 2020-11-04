class Solution:
    def maxPower(self, s: str) -> int:
        power = []
        
        i, temp = 1, ""
        for s_char in s:
            if s_char == temp:
                i += 1
            else:
                power.append( i )
                i = 1
            temp = s_char
        power.append(i)

        return max(power)
