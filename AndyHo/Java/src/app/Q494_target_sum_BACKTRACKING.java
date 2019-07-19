package app;

class Q494_target_sum_BACKTRACKING
{
    int count = 0;
    public int findTargetSumWays( int[] nums, int tar )
    {
        backtracking( 0, nums, tar, 0 );
        return count;
    }
    
    public void backtracking( int tmp, int[] nums, int tar, int ptr )
    {
        if( ptr == nums.length - 1 )
        {
            // not able to combine these 2 conditions, consider input [1,0] S = 1;
            // if combine, only on of the solution 1+0, 1-0 will be considered!
            if( tmp - nums[ ptr ] == tar ) count ++;
            if( tmp + nums[ ptr ] == tar )
            {
                count++;
                return;
            }
            return;
        }
        else
        {
            // try adding the nums
            backtracking( tmp + nums[ ptr ], nums, tar, ptr + 1 );
            // try reducing the nums
            backtracking( tmp - nums[ ptr ], nums, tar, ptr + 1 );
        }
    }
}

// logic improved, slower
// class Q494_target_sum_BACKTRACKING
// {
//     int count = 0;
//     public int findTargetSumWays( int[] nums, int tar )
//     {
//         backtracking( nums, tar, 0, 0 );
//         return count;
//     }
    
//     public void backtracking( int[] nums, int tar, int tmp, int ptr )
//     {
//         if( ptr == nums.length )
//         {
//             if( tmp == tar ) count++;
//         }
//         else
//         {
//             // try adding the nums
//             backtracking( nums, tar, tmp + nums[ ptr ], ptr + 1 );
//             // try reducing the nums
//             backtracking( nums, tar, tmp - nums[ ptr ], ptr + 1 );
//         }
//     }
// }