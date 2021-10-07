class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
        coll_s = collections.Counter(s)
        coll_t = collections.Counter(t)
        
        return sum( (coll_s-coll_t).values() )

class Solution2:
    def minSteps(self, s: str, t: str) -> int:
        
        for ch in s:
            
            t = t.replace( ch, "", 1 )
            
        return len(t)


from collections import defaultdict 

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
        t_dedict = defaultdict(int)
        for t_char in t:
            t_dedict[t_char] += 1
            
        ans = 0
        for s_char in s:
            if t_dedict[s_char] > 0:
                t_dedict[s_char] -= 1
            else:
                ans += 1
        
        return ans
