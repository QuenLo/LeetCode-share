class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        if not s: return 0
        
        queue = 0
        move = 0
        for char in s:
            if char == "(":
                queue += 1
            else:
                if queue < 1:
                    move += 1
                else:
                    queue -= 1
        
        return move + queue
