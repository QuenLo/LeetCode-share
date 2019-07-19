package app;

import java.util.List;
import java.util.Arrays;
import java.util.ArrayList;

public class Q15_3sum {
    // two pointers
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        Arrays.sort( nums );

        for( int i = 0; i + 2 < nums.length; i++ )
        {
            // If the number is the same as the number before, we have used it as target already, continue.
            if( i > 0 && nums[ i ] == nums[ i - 1 ] ) continue;
            // set the pointers
            int j = i + 1, k = (nums.length - 1);
            int target = -nums[ i ];
            // (j < k): condition for termination
            while( j < k )
            {
                if( nums[ j ] + nums[ k ] == target )
                {
                    result.add( Arrays.asList( nums[ i ], nums[ j ], nums[ k ] ) );
                    j++;
                    k--;
                    // prevent using same number as target
                    // (j < k): condition for termination
                    while( j < k && nums[ j ] == nums[ j - 1 ] ) j++;
                    while( j < k && nums[ k ] == nums[ k + 1 ] ) k--;
                }
                else if( nums[ j ] + nums[ k ] > target ) k--;
                else j++;
            }
        }
        return result;
    }
}