// ref. https://leetcode.com/problems/4sum/discuss/8609/My-solution-generalized-for-kSums-in-JAVA

package app;

import java.util.*;

class Q18_4sum
{
    public List<List<Integer>> fourSum(int[] nums, int target)
    {
        Arrays.sort( nums );
        return kSum( nums, 4, target, 0 );
    }
    
    public List<List<Integer>> kSum( int[] nums, int k, int tar, int start )
    {
        List<List<Integer>> sol = new ArrayList<List<Integer>>();
        if( start > nums.length - 1 ) return sol;
        
        // reduced to 2 sum problem
        if( k == 2 )
        {
            int left = start, right = nums.length - 1;
            while( left < right )
            {
                if( nums[ left ] + nums[ right ] == tar )
                {
                    List<Integer> s = new ArrayList<Integer>();
                    s.add( nums[ left ] );
                    s.add( nums[ right ] );
                    sol.add( s );
                    
                    left++;
                    right--;

                    // skip duplicate values
                    while( left < right && nums[ left ] == nums[ left-1 ] ) left++;
                    while( left < right && nums[ right ] == nums[ right+1 ] ) right--;
                }
                else if( nums[ left ] + nums[ right ] > tar ) right--;
                else left++;
            }
        }
        // reducing k sum to k-1 sum
        else
        {
            // the len of the arr should be at least == k - 1!
            for( int i = start; i < nums.length - (k - 1); i++ )
            {
                List<List<Integer>> tmp = kSum( nums, k-1, tar - nums[ i ], i + 1 );
                if( tmp != null )
                {
                    // add the current num to all the previous results
                    // previous result is the solution of k-1 sum
                    for( List<Integer> t: tmp )
                        // add at index 0
                        t.add( 0, nums[ i ] );
                    // copy the solution to the solution set
                    sol.addAll( tmp );
                }
                // skip duplicate values
                while( i < nums.length - 1 && nums[ i ] == nums[ i + 1 ] ) i++;
            }
        }
        return sol;
    }
}