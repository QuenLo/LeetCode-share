class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        order_map = {}
        for ind, value in enumerate(order):
            order_map[value] = ind
        
        for ind, word in enumerate(words[:-1]):
            
            for j in range( len(word) ):
                if j >= len(words[ind+1]): return False
                if word[j] != words[ind+1][j]:
                    if order_map[word[j]] > order_map[words[ind+1][j]]: return False
                    break;
        
        return True
