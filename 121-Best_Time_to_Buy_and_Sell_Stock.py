class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_p = 0
        
        if len(prices) < 1:
            return max_p
        
        buy = prices[0]
        for i in range( 1, len(prices) ):
            if prices[i] > buy:
                max_p = max( max_p, prices[i]-buy )
            elif prices[i] < buy:
                buy = prices[i]
                
        return max_p
