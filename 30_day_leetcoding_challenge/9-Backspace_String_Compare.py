### Build String ###
class Solution1:
    def backspaceCompare(self, S: str, T: str) -> bool:
        
        def check(S):
            S_new = []
            for w in S:
                if w != "#":
                    S_new.append(w)
                elif len(S_new):
                    S_new.pop()
            return S_new
                
        return check(S) == check(T)
        
### Two Pointer ###
