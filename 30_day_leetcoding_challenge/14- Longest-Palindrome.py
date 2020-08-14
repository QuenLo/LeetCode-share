class Solution:
    def longestPalindrome(self, s: str) -> int:
        if s == "":
            return 0
        
        Length = 0
        for item in set(s):
            if (Length%2==0) and (s.count(item)%2==1):
                Length += 1
            Length += (s.count(item)//2 * 2)
            
        return Length
