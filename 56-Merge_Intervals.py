class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        start, end = intervals[0]
        output = []
        for interval in intervals[1:]:
            start_i, end_i = interval
            if start_i > end:
                output.append( [start,end] )
                start, end = start_i, end_i
            else:
                end = max( end_i, end )
                
        output.append( [start, end] )
        return output
