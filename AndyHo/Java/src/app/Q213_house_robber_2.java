package app;

import java.lang.Math;

class Q213_house_robber_2
{
    public int rob(int[] nums)
    {
        if( nums.length == 0 ) return 0;
        if( nums.length == 1 ) return nums[ 0 ];
        
        return Math.max( helper( nums, 0, (nums.length - 1) ),
                         helper( nums, 1, (nums.length) )
        );
    }
    
    public int helper( int[] nums, int start, int end )
    {
        int[] dp = new int[ nums.length ];

        if( start == 0 )
        {
            dp[ 0 ] = nums[ 0 ];
            dp[ 1 ] = Math.max( nums[ 0 ], nums[ 1 ] );
        }
        else
        {
            dp[ 0 ] = 0;
            dp[ 1 ] = nums[ 1 ]; // shift the start point (dp[ 0 ] = nums[ 0 ])
        }
        
        for( int i = 2; i < end; i++ )
            dp[ i ] = Math.max( dp[ i - 2 ] + nums[ i ], dp[ i - 1 ] );
        return dp[ end - 1 ];
    }
}