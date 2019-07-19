package app;

// accepted, 82 ms
class Q189_rotate_arr_SHIFT
{
    public void rotate(int[] nums, int k)
    {
        // num. of steps that really needs to perform
        k = k % nums.length;
        while( k != 0 )
        {
            int tmp = nums[ nums.length - 1 ];
            // shift
            for( int i = nums.length - 2; i >= 0; i-- )
                nums[ i + 1 ] = nums[ i ];
            nums[ 0 ] = tmp;
            k--;
        }
    }
}