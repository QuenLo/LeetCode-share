package app;

import java.util.Map;
import java.util.HashMap;

class Q169_majority_element {
    public int majorityElement(int[] nums)
    {
        HashMap<Integer, Integer> dict = new HashMap<Integer, Integer>();
        
        for( int i = 0; i < nums.length; i++ )
        {
            if( dict.containsKey( nums[ i ] ) )
                dict.put( nums[ i ], dict.get( nums[ i ] ) + 1 );
            else
                dict.put( nums[ i ], 1 );
        }
        
        int sol = Integer.MIN_VALUE;
        int cur = Integer.MIN_VALUE;
        for( Map.Entry<Integer, Integer> entry : dict.entrySet() )
        {
            if( entry.getValue() > cur && entry.getValue() > (nums.length / 2) )
            {
                sol = entry.getKey();
                cur = entry.getValue();
            }
        }
        return sol;
    }
}