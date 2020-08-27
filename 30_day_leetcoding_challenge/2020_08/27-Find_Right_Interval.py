class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        
        import bisect
        
        end_list = [ ( interval[0], i ) for i, interval in enumerate(intervals) ]
        end_list.sort()
        
        ans = []
        for interval in intervals:
            end_loc = bisect.bisect_right(end_list, (interval[1], -1))
            ans.append( end_list[end_loc][1] if end_loc < len( intervals ) else -1)
            
        return ans
        
