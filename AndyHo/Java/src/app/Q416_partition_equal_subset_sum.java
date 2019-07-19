// ref. https://leetcode.com/problems/partition-equal-subset-sum/discuss/90592/01-knapsack-detailed-explanation

package app;

import java.util.*;

class Q416_partition_equal_subset_sum
{
    // public boolean canPartition(int[] nums)
    // {
    //     if( nums.length == 0 ) return true;
    //     int sum = 0;
    //     for( int n: nums ) sum += n;
        
    //     if( sum % 2 != 0 ) return false;
    //     // the targer
    //     sum /= 2;
        
    //     int n = nums.length - 1;
    //     boolean[][] dp = new boolean[ n + 1 ][ sum + 1];
    //     // dp array init
    //     for( int i = 0; i < dp.length; i++ )
    //         Arrays.fill( dp[ i ], false );
    //     dp[ 0 ][ 0 ] = true;
    //     for( int i = 1; i < n+1; i++ )
    //         dp[ i ][ 0 ] = true;
    //     for( int j = 1; j < sum + 1; j++ )
    //         dp[ 0 ][ j ] = false;
        
    //     // knapsack
    //     // For each number, if we don't pick it, dp[i][j] = dp[i-1][j], which means if the first i-1 elements has made it to j, dp[i][j] would also make it to j (we can just ignore nums[i]). If we pick nums[i]. dp[i][j] = dp[i-1][j-nums[i]], which represents that j is composed of the current value nums[i] and the remaining composed of other previous numbers. Thus, the transition function is dp[i][j] = dp[i-1][j] || dp[i-1][j-nums[i]]
    //     for( int i = 1; i < n+1; i++ )
    //         for( int j = 1; j < sum+1; j++ )
    //         {
    //             dp[ i ][ j ] = dp[ i-1 ][ j ];
    //             if( j >= nums[ i-1 ] )
    //                 // num[ (i-1) ]: i-1 since 0-index!!
    //                 dp[ i ][ j ] = dp[ i-1 ][ j ] || dp[ i-1 ][ j-nums[ i-1 ] ];
    //         }
    //     return dp[ n ][ sum ];
    // }

    // improve space usage
    public boolean canPartition(int[] nums)
    {
        if( nums.length == 0 ) return true;
        int sum = 0;
        for( int n: nums ) sum += n;
        
        if( sum % 2 != 0 ) return false;
        // the targer
        sum /= 2;

        boolean[] dp = new boolean[ sum + 1 ];
        // dp array init
        Arrays.fill( dp, false );
        dp[ 0 ] = true;
        
        // knapsack
        // For each number, if we don't pick it, dp[i][j] = dp[i-1][j], which means if the first i-1 elements has made it to j, dp[i][j] would also make it to j (we can just ignore nums[i]). If we pick nums[i]. dp[i][j] = dp[i-1][j-nums[i]], which represents that j is composed of the current value nums[i] and the remaining composed of other previous numbers. Thus, the transition function is dp[i][j] = dp[i-1][j] || dp[i-1][j-nums[i]]
        for( int n: nums )
            for( int i = sum; i > 0; i-- )
            {
                if( i >= n )
                    dp[ i ] = dp[ i ] || dp[ i-n ];
            }
        return dp[ sum ];
    }
}