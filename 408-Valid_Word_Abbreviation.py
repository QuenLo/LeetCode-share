class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        
        rep_num = 0
        cur_i = 0
        for ind, a in enumerate(abbr):
            
            if a.isdigit():
                if int(a) == 0 and rep_num == 0:
                    return False
                rep_num = rep_num*10 + int(a)
            else:
                cur_i += rep_num
                rep_num = 0
                if cur_i >= len(word) or a != word[cur_i]:
                    return False
                cur_i += 1
            
        return True and rep_num+cur_i == len(word)
