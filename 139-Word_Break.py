## Recursion with memoization
# Time: O(n^3)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @lru_cache
        def recur( s, word_dict, start ):
            if start == len(s):
                return True
            for end in range( start+1, len(s)+1 ):
                if s[start:end] in word_dict and recur( s, word_dict, end ):
                    return True
            return False
        
        return recur( s, frozenset(wordDict), 0 )

class SolutionII:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        memo = [-1]*len(s)
        
        def recur( s, word_dict, start ):
            if start == len(s):
                return True
            if memo[start] != -1:
                return memo[start]
            for end in range( start+1, len(s)+1 ):
                if s[start:end] in word_dict and recur( s, word_dict, end ):
                    memo[start] = True
                    return True
            
            memo[start] = False
            return False
        
        return recur( s, set(wordDict), 0 )

## Brute Force
# Time: O(2^n)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        def recur( s, word_dict, start ):
            if start == len(s):
                return True
            for end in range( start+1, len(s)+1 ):
                if s[start:end] in word_dict and recur( s, word_dict, end ):
                    return True
            return False
        
        return recur( s, set(wordDict), 0 )
