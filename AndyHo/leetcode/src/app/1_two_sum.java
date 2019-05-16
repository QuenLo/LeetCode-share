package app;

import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> dict = new HashMap<Integer, Integer>();
        // number as key, index as value
        for( int i = 0; i < nums.length; i++ )
        {
            dict.put( nums[ i ], i );
        }
        for( int i = 0; i < nums.length; i++ )
        {
            int complement = target - nums[ i ];
            if( dict.containsKey( complement ) &&
                dict.get( complement ) != i )
            {
                return new int[] { i, dict.get( complement ) };
            }
        }
        throw new IllegalArgumentException( "No two sum solution" );
    }
}