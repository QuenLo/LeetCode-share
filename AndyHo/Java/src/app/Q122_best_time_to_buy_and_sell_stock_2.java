package app;

class Q122_best_time_to_buy_and_sell_stock_2
{
    public int maxProfit(int[] prices)
    {
        if( prices.length == 0 || prices == null ) return 0;

        int valley = prices[ 0 ];
        int peak = prices[ 0 ];
        int i = 0, maxprofit = 0;
        while( i < prices.length - 1 )
        {
            // find the valley
            while( i + 1 < prices.length && prices[ i ] >= prices[ i + 1 ] ) i++;
            valley = prices[ i ];
            // find the peak
            while( i + 1 < prices.length && prices[ i ] <= prices[ i + 1 ] ) i++;
            peak = prices[ i ];
            maxprofit += (peak - valley);
        }
        return maxprofit;
    }
}