// ref. https://leetcode.com/problems/4sum-ii/discuss/93920/Clean-java-solution-O(n2)

package app;

import java.util.*;

class Q454_4sum_2
{
    public int fourSumCount(int[] A, int[] B, int[] C, int[] D)
    {
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();
        int sol = 0;
        for( int i = 0; i < A.length; i++ )
            for( int j = 0; j < B.length; j++ )
            {
                int sum = A[ i ] + B[ j ];
                map.put( sum, map.getOrDefault( sum, 0 ) + 1 );
            }

        for( int i = 0; i < C.length; i++ )
            for( int j = 0; j < D.length; j++ )
                // -(C[ i ] + D[ j ]) since the target is 0 for this problem
                sol += map.getOrDefault( -(C[ i ] + D[ j ]), 0 );
        return sol;
    }
}