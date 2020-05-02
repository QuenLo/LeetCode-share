class Solution1:
    def numJewelsInStones(self, J: str, S: str) -> int:
        
        total = 0
        Jset = set(J)
        
        for s in S:
            if s in Jset:
                total += 1
                
        return total
        
class Solution2:
    def numJewelsInStones(self, J: str, S: str) -> int:
        
        total = 0
        Jset = set(J)
        Sdict = {}
        
        for s in S:
            if s in Sdict:
                Sdict[s] += 1
            else:
                Sdict[s] = 1
        
        for s in Sdict:
            if s in Jset:
                total += Sdict[s]
                
        return total
