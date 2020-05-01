class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        
        move = 0
        for sh in shift:
            if sh[0] == 0:
                move += sh[1]
            else:
                move -=sh[1]
        move = move % len(s)
        return s[move:] + s[:move]
