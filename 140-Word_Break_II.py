from collections import defaultdict
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        memo = defaultdict(list)
        wordset = set(wordDict)
        result = []
        
        def topdown( s ):
            
            if not s:
                return [[]]
            
            if s in memo:
                return memo[s]
            
            for end in range( 1, len(s)+1 ):
                word = s[:end]
                if word in wordset:
                    for subword in topdown(s[end:]):
                        memo[s].append( [word] + subword )
                        
            return memo[s]
        
        topdown(s)
        print(memo)
        return [ " ".join( m_list ) for m_list in memo[s] ]
