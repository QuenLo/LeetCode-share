// ref. https://leetcode.com/problems/3sum-closest/discuss/7872/Java-solution-with-O(n2)-for-reference

package app;

import java.util.*;

class Q16_3sum_losest
{
    public int threeSumClosest(int[] nums, int target)
    {
        int diff = Integer.MAX_VALUE, sol = 0;
        Arrays.sort( nums );
        
        for( int i = 0; i + 2 < nums.length; i++ )
        {
            // If the number is the same as the number before, we have used it as target already, continue.
            if( i > 0 && nums[ i ] == nums[ i - 1 ] ) continue;
            // set the pointers
            int left = i + 1, right = (nums.length - 1);
            while( left < right )
            {
                int sum = nums[ i ] + nums[ left ] + nums[ right ];
                
                if( Math.abs( sum - target ) < diff )
                {
                    diff = Math.abs( sum - target );
                    sol = sum;
                }
                
                if( sum > target ) right--;
                else left++;
            }
        }
        return sol;
    }
}