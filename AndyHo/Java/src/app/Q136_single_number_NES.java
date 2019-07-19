package app;

import java.util.*;

// Math
class Q136_single_number_NES {
    public int singleNumber(int[] nums)
    {
        Set<Integer> set = new HashSet<Integer>();
        int sumOfArr = 0;
        for( int i = 0; i < nums.length ; i++ )
        {
            // calculate the sum of array
            sumOfArr += nums[ i ];
            // put elements into set
            set.add( nums[ i ] );
        }
        // 2 * (a + b + c) - (a + a + b + b + c) = c
        return (2 * (set.stream().mapToInt(Integer::intValue).sum()) - sumOfArr);
    }
}

// XOR
// class Solution {
//     public int singleNumber(int[] nums)
//     {
//         int a = 0;
//         for( int i = 0; i < nums.length ; i++ )
//             a ^= nums[ i ];
//         return a;
//     }
// }