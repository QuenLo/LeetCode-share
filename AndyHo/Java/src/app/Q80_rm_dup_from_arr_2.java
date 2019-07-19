package app;

class Q80_rm_dup_from_arr_2 {
    public int removeDuplicates(int[] nums) {
        int start = 0, count = 1;
        for( int i = 1; i < nums.length; i++ )
        {
            if( nums[ i ] != nums[ start ] )
            {
                start++;
                nums[ start ] = nums[ i ];
                count = 1;
            }
            else
            {
                count++;
                if( count == 2 )
                {
                    start++;
                    // ensure the current position has the same value as previous
                    // ex: [1,1,1,1,2,3,3]
                    //     [1,1,1,1,2,3,2]
                    nums[ start ] = nums[ start - 1 ];
                }
            }
        }
        return start + 1;
    }
}