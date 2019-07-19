// ref. https://leetcode.com/problems/sort-colors/discuss/148221/Java-2-pass-counting-sort-and-1-pass-quick-partition-(with-video-tutorial-links)

package app;

class Q75_sort_colors_QUICKSORT3WAY
{
    // quick sort 3-way partition
    public void sortColors(int[] nums)
    {
        // i = idex of element unvisited
        int l = 0, i = 0, r = nums.length - 1;
        while( i <= r )
        {
            if( nums[ i ] == 2 )
            {
                swap( nums, i, r );
                r--;
            }
            else if( nums[ i ] == 0 )
            {
                swap( nums, l, i );
                l++; i++;
            }
            else    i++;
        }
    }
    
    public void swap( int[] nums, int idx_a, int idx_b )
    {
        int tmp = nums[ idx_a ];
        nums[ idx_a ] = nums[ idx_b ];
        nums[ idx_b ] = tmp;
    }
}