package app;

import java.util.*;

class Q136_single_number {
    public int singleNumber(int[] nums)
    {
        HashMap<Integer, Integer> dict = new HashMap<Integer, Integer>();

        for( int i = 0; i < nums.length; i++ )
        {
            if( dict.containsKey( nums[ i ] ) )
                dict.put( nums[ i ], dict.get( nums[ i ] ) + 1 );
            else
                dict.put( nums[ i ], 1 );
        }

        for( Map.Entry<Integer, Integer> entry : dict.entrySet() )
        {
            if( entry.getValue() < 2 )
                return entry.getKey();
        }
        return Integer.MIN_VALUE;
    }
}