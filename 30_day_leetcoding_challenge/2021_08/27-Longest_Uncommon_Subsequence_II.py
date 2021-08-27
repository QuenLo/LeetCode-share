class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        
        now_comm = -1
        i, x = 0, 0
        
        l_strs = []
        
        for s_strs in strs:
            l_strs.append( len(s_strs) )
        
        while i < len(strs):
            x = i + 1

            while x < len(strs):
                if strs[i] == strs[x]:
                    l_strs[x], l_strs[i] = -1, -1
                    break
                if len(strs[i]) > len(strs[x]):
                    comm = self.checkcommon( strs[x], strs[i] )
                    l_strs[x] = min( l_strs[x], comm )
                else:
                    comm = self.checkcommon( strs[i], strs[x] )
                    l_strs[i] = min( l_strs[i], comm )
                
                x += 1
            i += 1
        
        return max(l_strs)
    
    def checkcommon( self, A: str, B: str ) -> int:
        a, b = 0, 0
        while a < len(A) and b < len(B):
            
            if A[a] == B[b]:
                a += 1
                b += 1
            else: b += 1
                
        if a == len(A): return -1
        else: return len(A)
