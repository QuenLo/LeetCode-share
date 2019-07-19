package app;

// ref. https://leetcode.com/problems/combination-sum-iv/discuss/314215/C-bottom-up-dynamic-programming-solution
// ref. https://leetcode.com/problems/combination-sum-iv/discuss/315703/DP-Java-solution-faster-than-90

class Q377_combination_sum_4
{
    // the solution is built up by all the number < target,
    // which could also be composed by the given elements.
    public int combinationSum4(int[] nums, int target)
    {
        if( target == 0 ) return 1;
        if( nums.length == 0 ) return 0;
        if( nums.length == 1 )
            // ex n = [9], tar = 3 -> ans = 0
            if( target > nums[0] ) 
                return 1;
            else
                return 0;
        
        int[] dp = new int[ target + 1 ];
        dp[ 0 ] = 1;
        for( int i = 1; i <= target; i++ )
            for( int j = 0; j < nums.length; j++ )
            {
                if( i >= nums[ j ] )
                    dp[ i ] += dp[ i - nums[ j ] ];
            }
        return dp[ target ];
    }
}