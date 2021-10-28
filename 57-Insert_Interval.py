class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        head, end = newInterval
        ind, n = 0, len(intervals)
        output = []
        
        while ind < n and head > intervals[ind][0]:
            output.append( intervals[ind] )
            ind += 1
            
        if not output or output[-1][1] < head:
            output.append( newInterval )
        else:
            output[-1][1] = max( end, output[-1][1] )
            
        # still need to merge
        while ind < n:
            head_i, end_i = intervals[ind]
            ind += 1
            if output[-1][1] >= head_i:
                output[-1][1] = max(end_i, output[-1][1])
            else:
                output.append( intervals[ind-1] )
                
        return output
