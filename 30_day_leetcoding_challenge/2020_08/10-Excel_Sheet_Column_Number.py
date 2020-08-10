class Solution:
    def titleToNumber(self, s: str) -> int:
        ans = 0
        place = 0
        for i in range( len(s) -1, -1, -1 ):
            i_num = ord(s[i]) - ord("A") + 1
            ans += i_num*(26**place)
            place += 1
            
        return ans
        
        
class SolutionII:
    def titleToNumber(self, s: str) -> int:
        return reduce(lambda x, y : x * 26 + y, [ord(c) - 64 for c in list(s)])
