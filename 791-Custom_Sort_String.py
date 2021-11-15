class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        count = collections.Counter(s)
        ans = []
        
        for o in order:
            ans.append( count[o]*o )
            count[o] = 0
        
        for ch in count:
            ans.append( ch*count[ch] )
            
        return "".join( ans ) 
