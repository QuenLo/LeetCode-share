package app;

import java.lang.Math;

// Problem: If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

// one buy and one sell!!!

class Q121_best_time_to_buy_and_sell_stock
{
    int max_profit = 0;
    public int maxProfit(int[] prices)
    {
        for( int i = 0; i < prices.length; i++ )
            for( int j = i + 1; j < prices.length; j++ )
                // max profit == max difference and second (sell) > first (buy)
                max_profit = Math.max( max_profit, prices[ j ] - prices[ i ] );
        return max_profit;
    }
}