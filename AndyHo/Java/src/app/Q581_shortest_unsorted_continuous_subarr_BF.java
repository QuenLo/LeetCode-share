package app;

import java.lang.Math;

// brute force
class Q581_shortest_unsorted_continuous_subarr_BF
{
    public int findUnsortedSubarray(int[] nums)
    {
        int sol = nums.length;
        // arr[ 0, i] & arr[ j, n-1 ] should be sorted
        // arr[ i, j ] should be the answer
        // try all the possibilities for (i, j)
        for( int i = 0; i < nums.length; i++ ) {
            // see line 17 for the reason of (j <= nums.length)
            for( int j = i; j <= nums.length; j++ )
            {
                int min = Integer.MAX_VALUE, max = Integer.MIN_VALUE, pre = Integer.MIN_VALUE;

                // find the min and max within the subarray
                for( int k = i; k < j; k++ )
                {
                    min = Math.min( min, nums[ k ] );
                    max = Math.max( max, nums[ k ] );
                }
                // not yet
                if(
                    (i > 0 && nums[ i - 1 ] > min ) ||
                    (j < nums.length && nums[ j ] < max )
                )
                    continue;

                // check if arr[ 0, i ] is sorted
                int k = 0;
                while( k < i && pre <= nums[ k ] )
                {
                    pre = nums[ k ];
                    k++;
                }
                if( k !=  i ) continue;

                // check if arr[ j, n-1 ] is sorted
                k = j;
                while( k < nums.length && pre <= nums[ k ] )
                {
                    pre = nums[ k ];
                    k++;
                }

                // record the mininum solution
                if( k == nums.length ) sol = Math.min( sol, (j - i) );
            }
        }
        return sol;
    }
}

// better burte force
class Q581_shortest_unsorted_continuous_subarr_IMPROVEDBF
{
    public int findUnsortedSubarray(int[] nums)
    {
        int r = 0, l = nums.length;
        for( int i = 0; i < nums.length - 1; i++ )
        {
            for( int j = i + 1; j < nums.length; j++ )
            {
                if( nums[ j ] < nums[ i ] )
                {
                    r = Math.max( r, j  );
                    l = Math.min( l, i );
                }
            }
        }
        if( r - l < 0 ) return 0;
        else return (r - l + 1);
    }
}