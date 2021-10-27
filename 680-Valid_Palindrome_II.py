class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        if s == s[::-1]:
            return True
        
        left, right = 0 , len(s)-1
        s = list(s)
        while left < right:
            if s[left] != s[right]:
                s_l = s[left+1:right+1]
                s_r = s[left:right]
                return s_l == s_l[::-1] or s_r == s_r[::-1]
            left += 1
            right -= 1
        
        return True

class SolutionII:
    def validPalindrome(self, s: str) -> bool:
        
        def verify( s, left, right, deleted ):
            
            while left < right:
                
                if s[left] != s[right]:
                    if deleted:
                        return False
                    else:
                        return verify( s, left+1, right, True ) or verify( s, left, right-1, True )
                else:
                    left += 1
                    right -= 1
            
            return True
            
        return verify( list(s), 0, len(s)-1, False )
