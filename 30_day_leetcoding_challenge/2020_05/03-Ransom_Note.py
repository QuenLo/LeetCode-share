class Solution1:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        C_r = Counter( ransomNote )
        C_m = Counter( magazine )
        
        for r in C_r:
            if C_r[r] > C_m[r]:
                return False
            
        return True
        
class Solution2:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        C_r = Counter( ransomNote )
        
        for r in C_r:
            if C_r[r] > magazine.count(r):
                return False
            
        return True

class Solution3:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        magazine = list(magazine)
        for r in ransomNote:
            if r in magazine:
                magazine.remove(r)
            else:
                return False
                    
        return True
        
class Solution4:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for r in ransomNote:
            if r not in magazine:
                return False
            magazine = magazine.replace(r, "", 1)
            
        return True
