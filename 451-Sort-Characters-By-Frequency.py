class Solution(object):
    def frequencySort(self, s):
        
        letterDict = {}
        AnswerStr = ""
        for ss in s:
            if letterDict.has_key(ss) :
                letterDict[ss] += 1
            else:
                letterDict[ss] = 1
                
        #sorted(iterable, cmp=None, key=None, reverse=False)
        letterTuple = sorted(letterDict.items(), key=lambda letter: letter[1],reverse=True) 
        
        for key in letterTuple:
            AnswerStr += key[0]*key[1]
            
        return AnswerStr
