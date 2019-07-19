// ref. https://www.techiedelight.com/convert-set-to-array-java/

package app;

import java.util.*;

class Q349_intersection_of_2_arrs
{
    public int[] intersection(int[] nums1, int[] nums2)
    {
        Set<Integer> set1 = new HashSet<Integer>();
        Set<Integer> set2 = new HashSet<Integer>();
        for( int n: nums1 ) set1.add( n );
        for( int n: nums2 ) set2.add( n );
        
        Set<Integer> sol = new HashSet<Integer>();
        if( set1.size() > set2.size() )
            for( int num: set2 )
            {
                if( set1.contains( num ) ) sol.add( num );
            }
        else
            for( int num: set1 )
            {
                if( set2.contains( num ) ) sol.add( num );
            }
        int[] res = new int[ sol.size() ];
        int i = 0;
        for( int num: sol ) res[ i++ ] = num;
        return res;
    }
}