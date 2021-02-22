class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        
        result = ""
        
        for d_str in d:
            diff = len(d_str) - len(result)
            if diff >= 0:
                
                # longer or smaller lexicographical order
                if diff > 0 or d_str < result:
                    try:
                        pos = -1
                        # formed by deleting some characters of the given string
                        for d_char in d_str:
                            pos = s.index(d_char, pos+1)
                        result = d_str
                    except ValueError:
                        pass
        return result

class SolutionI:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        
        for _str in sorted( d, key=lambda x: (-len(x),x) ):
            it = iter(s)
            
            if all( char in it for char in _str ):
                return _str
            
        return ""

class SolutionII:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        
        re_str = ""
        for d_str in d:
            
            i = 0
            for s_char in s:
                if (i < len(d_str)) and (d_str[i] == s_char):
                    i += 1

            if i == len(d_str) and i >= len(re_str):
                if i == len(re_str):
                    re_str = min(str(d_str),str(re_str))
                else:
                    re_str = d_str
        
        return re_str
