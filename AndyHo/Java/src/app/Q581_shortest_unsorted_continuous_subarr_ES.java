package app;

import java.util.*;

// sorted array comparison
class Q581_shortest_unsorted_continuous_subarr_ES
{
    public int findUnsortedSubarray( int[] nums )
    {
        int[] clone = nums.clone();
        Arrays.sort( clone );

        int r = 0, l = 0;
        for( int i = 0; i < nums.length; i++ )
            if( nums[ i ] != clone[ i ] )
            {
                l = i;
                break;
            }
        for( int j = nums.length - 1; j >= 0; j-- )
            if( nums[ j ] != clone[ j ] )
            {
                r = j;
                break;
            }
        if( r == l ) return 0;
        return (r - l + 1);
    }
}