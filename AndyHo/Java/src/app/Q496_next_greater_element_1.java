// ref. https://leetcode.com/problems/next-greater-element-i/discuss/97595/Java-10-lines-linear-time-complexity-O(n)-with-explanation

package app;

import java.util.*;

class Q496_next_greater_element_1
{
    // where nums1’s elements are subset of nums2!!!!!!
    // that's why the map will work
    public int[] nextGreaterElement(int[] nums1, int[] nums2)
    {
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();
        Stack<Integer> stack = new Stack<Integer>();
        for( int i = 0; i < nums2.length; i++ )
        {
            while( !stack.isEmpty() && stack.peek() < nums2[ i ] )
            {
                map.put( stack.pop(), nums2[ i ] );
            }
            stack.push( nums2[ i ] );
        }
        int[] sol = new int[ nums1.length ];
        for( int i = 0; i < nums1.length; i++ )
            sol[ i ] = map.getOrDefault( nums1[ i ], -1 );
        return sol;
    }
}