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
