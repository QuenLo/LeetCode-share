### Peak Valley Approach ###
class Solution1:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        i = 0
        while i < len( prices )-1:
            #valley
            while( i < len( prices )-1 and prices[i] >= prices[i+1] ):
                i += 1
            valley = prices[i]
            #peak
            while( i < len( prices )-1 and prices[i] <= prices[i+1] ):
                i += 1
            peak = prices[i]
            
            profit += peak-valley
        return profit

### Simple One Pass ###
class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range( 1, len(prices) ):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
                
        return profit
        
### Brute Force - "Time Limit Exceeded" ###
class Solution3:
    def maxProfit(self, prices: List[int]) -> int:
        return self.findMax( prices, 0 )
    
    def findMax( self, prices: List[int], start: int ):
        
        Max = 0
        if start >= len( prices ) -1:
            return 0
        for s in range( start, len( prices )-1 ):
            max_profit = 0
            for i in range( s+1, len( prices ) ):
                if prices[s] < prices[ i ]:
                    profit = self.findMax( prices, i+1 ) + prices[ i ] - prices[s]
                    max_profit = max( max_profit, profit )
            Max = max( Max, max_profit )
        return Max
        

class Solution0:
    def maxProfit(self, prices: List[int]) -> int:
        low, high = -1, -1
        profit = 0
        for price in prices:
            
            #buy
            if (low == -1 or low > price) and high == -1:
                low = price
            else: 
                if (high != -1) and (high < price):
                    high = price
                elif (high != -1) and (high > price):
                    #sale
                    profit += high - low
                    high, low = -1, price
                elif (high == -1) and (low != -1):
                    high = price
                    
        #the last one
        if high > low:
            profit += high-low
        return profit
