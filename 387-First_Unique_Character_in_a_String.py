class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = collections.Counter(s)
        
        for indx, ch in enumerate(s):
            if count[ch] < 2:
                return indx
        
        return -1
