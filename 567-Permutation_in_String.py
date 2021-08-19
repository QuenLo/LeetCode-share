## Sliding Window
# Time: O(m+n)
# Space: O(1)
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2): return False
        s1_l = [0]*26
        s2_l = [0]*26
        s1_len = len(s1)
        
        for i in range(s1_len):
            s1_l[ord(s1[i])-ord('a')] += 1
            s2_l[ord(s2[i])-ord('a')] += 1
            
        if s1_l == s2_l: return True
        
        right = s1_len
        while right < len(s2):
            s2_l[ord(s2[right])-ord('a')] += 1
            s2_l[ord(s2[right-s1_len])-ord('a')] -= 1
            
            if s2_l == s1_l: return True
            right += 1
            
        return False
