class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        s_len = len(s)
        for i_ch in range(s_len):
            if s.count( s[i_ch] ) == 1:
                return i_ch
            
        return -1
