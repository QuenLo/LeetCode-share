package app;

import java.lang.Math;

class Q53_maximum_subarray {
    public int maxSubArray(int[] nums)
    {
        int[] dp = new int[ nums.length ];
        // base case (largest number from 0 to 0 is element 0)
        dp[ 0 ] = nums[ 0 ];
        // store the solution
        int max = nums[ 0 ];
        for( int i = 1; i < nums.length; i++ )
        {
            dp[ i ] = Math.max( dp[ i - 1 ] + nums[ i ], nums[ i ] );
            max = Math.max( max, dp[ i ] );
        }
        return max;
    }
}