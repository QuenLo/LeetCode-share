class Solution:
    def toGoatLatin(self, S: str) -> str:
        
        s_goat = []
        ma = "ma"
        for s in S.split(" "):
            ma = ma + "a"
            
            # first letter
            if s[0].lower() in ['a', 'e', 'i', 'o', 'u']:
                s = s + ma
                s_goat.append( s )
                continue
            else:
                s = s[1:] + s[0] + ma 
                s_goat.append( s )
                
        return " ".join( s_goat )
