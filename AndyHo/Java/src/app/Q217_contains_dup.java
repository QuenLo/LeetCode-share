package app;

import java.util.*;

class Q217_contains_dup
{
    public boolean containsDuplicate(int[] nums)
    {
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();
        for( int n: nums )
        {
            if( map.containsKey( n ) ) return true;
            map.put( n, 1 );
        }
        return false;
    }
}