// ref. https://leetcode.com/problems/contains-duplicate-ii/discuss/61397/Short-AC-JAVA-solution

package app;

import java.util.*;

class Q219_contains_dup_2_MAP
{
    public boolean containsNearbyDuplicate(int[] nums, int k)
    {
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();
        for( int i = 0; i < nums.length; i++ )
        {
            if( map.containsKey( nums[ i ] ) )
            {
                int pre = map.get( nums[ i ] );
                if( i != pre && Math.abs( i - pre ) <= k ) return true;
            }
            map.put( nums[ i ], i );
        }
        return false;
    }
}