"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        
        all_ints = []
        for employ in schedule:
            [all_ints.append(sc) for sc in employ]
            
        all_ints.sort( key = lambda sc: sc.start )
        
        ## merge
        merge_schedule = []
        for i in all_ints:
            if not merge_schedule or i.start > merge_schedule[-1].end:
                merge_schedule.append( i )
            else:
                merge_schedule[-1].end = max( i.end, merge_schedule[-1].end )
                
        empty = []
        for i in range(1,len(merge_schedule)):
            interval = Interval(end=merge_schedule[i].start, start=merge_schedule[i-1].end)
            empty.append(interval)
            
        return empty
      
      
"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class SolutionII:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        
        all_ints = []
        for employ in schedule:
            [all_ints.append(sc) for sc in employ]
            
        all_ints.sort( key = lambda sc: sc.start )
        
        ## merge
        merge_schedule = []
        empty = []
        for i in all_ints:
            if not merge_schedule or i.start > merge_schedule[-1].end:
                merge_schedule.append( i )
                if len(merge_schedule) > 1:
                    empty.append(Interval(end=merge_schedule[-1].start, start=merge_schedule[-2].end))
            else:
                merge_schedule[-1].end = max( i.end, merge_schedule[-1].end )
                
            
        return empty
