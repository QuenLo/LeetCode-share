class Solution:
    
    def binery_next(self, endtime, startTime, position ):
        
        start, end = position, len(startTime) - 1
        nextindex = end + 1
        
        while( start <= end ):
            mid = (start + end) // 2
            if( startTime[mid] < endtime ):
                start = mid + 1
            else:
                nextindex = mid
                end = mid - 1
                
        return nextindex
        
        
    def findMaxProfit(self, works, startTime, n, position ):
        
        # the end, no more job
        if position == n:
            return 0
        
        # already count
        if memo[position] != -1:
            return memo[position]
        
        # find Nextindex
        nextIndex = self.binery_next( works[position][1], startTime, position )
        
        # do or not to do
        maxProfit = max( works[position][2] + self.findMaxProfit( works, startTime, n, nextIndex ), self.findMaxProfit( works, startTime, n , position+1 ) )
        
        memo[position] = maxProfit
        
        return maxProfit
    
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        
        global memo
        memo = [ -1 for _ in range(50001) ]
        
        works = []
        for s, e, p in zip( startTime, endTime, profit ):
            works.append( [s,e,p] )
        
        # sort 1 -> ...
        works.sort( key = lambda work: work[0] )
        startTime = [ work[0] for work in works ]
        
        return self.findMaxProfit( works, startTime, len(works) ,0 )
