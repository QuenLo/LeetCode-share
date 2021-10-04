class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        i, N, result = 0, len(words), []
        while i < N:

            oneline, j, currwidth, positionNum, spaceNum = [words[i]], i+1, len(words[i]), 0, maxWidth - len(words[i])
            while j < N and currwidth + 1 + len(words[j]) <= maxWidth:
                oneline.append( words[j] )
                currwidth += 1 + len(words[j])
                spaceNum -= len(words[j])
                positionNum, j = positionNum + 1, j + 1
            
            i = j
            
            space = []
            if i < N and positionNum:
                for k in range(positionNum):
                    if k < spaceNum % positionNum:
                        space.append( ' '*(spaceNum // positionNum + 1) )
                    else:
                        space.append( ' '*(spaceNum // positionNum) )
                space.append('')
            else:
                for w in range(positionNum):
                    space.append(' ') 
                space.append( ' '*(maxWidth - currwidth) )
        
            
            result.append( ''.join( [s for pair in zip(oneline, space) for s in pair] ) )
            
        return result
