## Recursive
# Time: O(2^n), Time Limit
# Space: O(n)
# (if you use lru_cache, then it won't be time limit)
class Solution:
    def numDecodings(self, s: str) -> int:
        
        def countNext( S: str, headnum: int ) -> int:
            
            if len(S) == 0:
                return headnum
            
            # 1 digit
            OneD = 0
            if S[0] == '0':
                OneD = 0
            else:
                OneD = countNext( S[1:], headnum*1 )
            
            # 2 digit
            TwoD = 0
            if len(S) > 1:
                if 9 < int(S[0:2]) < 27:
                    TwoD = countNext( S[2:], headnum*1 )
                else:
                    TwoD = 0
            
            return TwoD + OneD
        
        return countNext( s, 1 )

## Iterative
# Time; O(n)
# Space: O(n)
class Solution:
    def numDecodings(self, s: str) -> int:
        
        if s[0] == '0': return 0
        
        s_len = len(s)
        memo = [0]*(s_len+1)
        memo[0] = 1
        
        for i in range(1,s_len):
            
            # 1 digit
            OneD = 0
            if s[i] != '0':
                OneD = 1
            
            # 2 digit
            TwoD = 0
            if s[i-1] == '1' or ( s[i-1] == '2' and s[i] < '7' ):
                TwoD = 1
            else: 
                TwoD = 0
            
            if i < 2:
                memo[i] = OneD + TwoD
            else:
                memo[i] = (OneD*memo[i-1]) + (TwoD*memo[i-2])
            

        return memo[s_len-1]

## IterativeII
# Time; O(n)
# Space: O(1)
class Solution:
    def numDecodings(self, s: str) -> int:
        
        if s[0] == '0': return 0
        
        first, second = 1, 1
        
        for i in range(1, len(s)):
            
            current = 0
            
            # 1 digit
            if s[i] != '0':
                current = first
            
            # 2 digit
            if s[i-1] == '1' or (s[i-1] == '2' and s[i] < '7'):
                current += second
            
            second = first
            first = current
