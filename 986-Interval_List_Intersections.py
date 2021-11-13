class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
        f_len, f = len(firstList), 0
        s_len, s = len(secondList), 0
        ans = []
        
        while f < f_len and s < s_len:
            low = max( firstList[f][0], secondList[s][0] )
            hight = min( firstList[f][1], secondList[s][1] )
            
            if low <= hight:
                ans.append( [low, hight] )
                
            if firstList[f][1] < secondList[s][1]:
                f += 1
            else:
                s += 1
                
        return ans
