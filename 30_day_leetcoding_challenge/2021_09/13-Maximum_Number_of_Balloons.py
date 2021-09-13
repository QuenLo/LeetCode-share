class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        having = { 'b':0, 'a': 0, 'l':0, 'o':0, 'n':0 }
        
        for t in text:
            if t in having.keys():
                having[t] += 1
        
        Ans = 0
        having['l'] = having['l'] // 2
        having['o'] = having['o'] // 2
        
        return having[min(having.keys(), key=(lambda k: having[k]))]
