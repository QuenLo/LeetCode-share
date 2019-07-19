package app;

import java.util.*;

class Q350_intersection_of_2_arrs_2
{
    public int[] intersect(int[] nums1, int[] nums2)
    {
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();
        List<Integer> res = new ArrayList<Integer>();
        
        for( int n: nums1 )
            map.put( n, map.getOrDefault( n, 0 ) + 1 );
        for( int n: nums2 )
        {
            if( map.containsKey( n ) )
            {
                map.put( n, map.get( n ) - 1 );
                if( map.get( n ) >= 0 )
                    res.add( n );
            }
        }

        int[] sol = new int[ res.size() ];
        for( int i = 0; i < res.size(); i++ ) sol[ i ] = res.get( i );
        return sol;
    }
}