from collections import Counter
class Solution(object):
    def frequencySort(self, s):
        
        letterTuple = Counter(s).most_common()
        AnswerStr = "" 
        
        for key in letterTuple:
            AnswerStr += key[0]*key[1]
            
        return AnswerStr
