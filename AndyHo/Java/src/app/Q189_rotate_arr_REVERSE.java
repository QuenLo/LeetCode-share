package app;

// accepted, 0 ms
public class Q189_rotate_arr_REVERSE
{
    // Original List                   : 1 2 3 4 5 6 7
    // After reversing all numbers     : 7 6 5 4 3 2 1
    // After reversing first k numbers : 5 6 7 4 3 2 1
    // After revering last n-k numbers : 5 6 7 1 2 3 4 --> Result
    public void rotate(int[] nums, int k)
    {
        k %= nums.length;
        reverse( nums, 0, nums.length - 1 );
        reverse( nums, 0, k - 1);
        reverse( nums, k, nums.length - 1 );
    }
    public void reverse(int[] nums, int start, int end)
    {
        while( start < end )
        {
            int temp = nums[ start ];
            nums[ start ] = nums[ end ];
            nums[ end ] = temp;
            start++;
            end--;
        }
    }
}