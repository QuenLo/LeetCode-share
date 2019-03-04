class Solution:
    def countSubstrings(self, s: str) -> int:
        Length, count = len(s), 0
        
        for i in range( Length - 1 ):
            temp = 0
            while( i - temp >= 0 and i + 1 + temp < Length and s[i - temp] == s[i + 1 + temp] ):
                count += 1
                temp += 1
            
            temp = 1
            while( i - temp >= 0 and i + temp < Length and s[i - temp] == s[i + temp] ):
                count += 1
                temp += 1
                
        return count + Length
        
#slower
class SolutionII:
    def countSubstrings(self, s: str) -> int:
        count, Length = 0, len(s)
        for i in range(Length):
            for j in range(i, Length):
                if s[i:j+1] == s[i:j+1][::-1]:
                    count += 1
        return count

# faster
class SolutionIII:
    def countSubstrings(self, s: str) -> int:
        count, Length = 0, len(s)
        
        # there are 2*Length - 1 centers
        # s[1], between s[1] and s[2], s[2], between s[2] and s[3] ... etc
        for center in range( 2*Length - 1 ):
            left = center // 2
            right = left + center % 2
            
            while( left >= 0 and right < Length and s[left] == s[right] ):
                count += 1
                left -= 1
                right += 1
        
        return count
