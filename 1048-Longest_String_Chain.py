class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        keep_dict = { word: None for word in words }
        
        def dfs(word):
            if word not in keep_dict:
                return 0
            if len(word) == 1:
                keep_dict[word] = 1
                return 1
            if keep_dict[word] != None:
                return keep_dict[word]

            keep_dict[word] = max( [ dfs( word[0:i]+word[i+1:] ) + 1 for i in range(len(word)) ] )
            return keep_dict[word]
        
        
        return max([ dfs(word) for word in words ])
