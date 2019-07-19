package app;

// dynamic programming
// dp[ i ] = dp[ i - 1 ] + dp[ i - 2 ]
class Q70_climbing_stairs_DP {
    public int climbStairs(int n)
    {
        // base case
        if( n == 1 ) return 1;
        
        int[] dp = new int[ (n + 1) ];
        dp[ 1 ] = 1;    // 1 solution for 1 steps
        dp[ 2 ] = 2;    // 2 solutions for 2 steps
        // dp[ 3 ] = 3  -> 3 solutions for 3 steps (dp[ 1 ] + dp[ 2 ])
        // dp[ 4 ] = 5  -> 4 solutions for 4 steps (dp[ 2 ] + dp[ 3 ])
        for( int i = 3; i < dp.length; i++ )
            dp[ i ] = dp[ i - 1 ] + dp[ i - 2 ];
        return dp[ n ];
    }
}