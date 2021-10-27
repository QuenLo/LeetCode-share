class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        slist = list(s)
        queue = []
        
        for ind, c in enumerate(s):
            if c == "(":
                queue.append(ind)
            if c == ")":
                
                if not queue:
                    slist[ind] = ""
                    continue
                queue.pop()
                
        for i in queue:
            slist[i] = ""
                
                
        return "".join( slist )

class SolutionII:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        queue = []
        need_remove = []
        ans_str = ""
        
        for ind, s_char in enumerate(s):
            if s_char not in "()":
                continue
            if s_char == "(":
                queue.append( ind )
            elif not queue:
                need_remove.append( ind )
            else:
                queue.pop()
                
        need_remove.extend( queue )
        for ind, c in enumerate(s):
            if ind not in need_remove:
                ans_str += c
                
        return ans_str
