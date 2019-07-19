// ref. https://leetcode.com/problems/two-sum/discuss/3/Accepted-Java-O(n)-Solution

package app;

import java.util.*;

// public class Q1_two_sum {
//     public int[] twoSum(int[] nums, int target) {
//         HashMap<Integer, Integer> dict = new HashMap<Integer, Integer>();
//         // number as key, index as value
//         for( int i = 0; i < nums.length; i++ )
//         {
//             dict.put( nums[ i ], i );
//         }
//         for( int i = 0; i < nums.length; i++ )
//         {
//             int complement = target - nums[ i ];
//             if( dict.containsKey( complement ) &&
//                 dict.get( complement ) != i )
//             {
//                 return new int[] { i, dict.get( complement ) };
//             }
//         }
//         throw new IllegalArgumentException( "No two sum solution" );
//     }
// }

// updated
class Q1_two_sum
{
    public int[] twoSum(int[] nums, int target)
    {
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();
        for( int i = 0; i < nums.length; i++ )
        {
            if( map.containsKey( target - nums[ i ] ) )
                return new int[]{ map.get( target - nums[ i ] ), i };
            // number as key, index as value
            map.put( nums[ i ], i );
        }
        return new int[0];
    }
}