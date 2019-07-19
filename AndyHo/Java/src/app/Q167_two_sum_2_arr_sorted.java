// ref. https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/discuss/51239/Share-my-java-AC-solution.

package app;

class Q167_two_sum_2_arr_sorted
{
    public int[] twoSum(int[] nums, int target)
    {
        if( nums.length == 0 || nums == null ) return new int[0];
        if( target < nums[ 0 ] ) return new int[0];
        
        int left = 0, right = nums.length - 1;
        while( left < right )
        {
            int cur = nums[ left ] + nums[ right ];
            if( cur == target )
                return new int[]{ (left + 1), (right + 1) };
            else if( cur < target ) left++;
            else right--;
        }
        return new int[0];
    }
}