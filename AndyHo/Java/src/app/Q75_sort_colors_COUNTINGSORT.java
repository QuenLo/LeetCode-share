// ref. https://leetcode.com/problems/sort-colors/discuss/148221/Java-2-pass-counting-sort-and-1-pass-quick-partition-(with-video-tutorial-links)

package app;

class Q75_sort_colors_COUNTINGSORT
{
    // counting sort
    public void sortColors(int[] nums)
    {
        int[] count = new int[ 3 ]; // value ranging from 0 to 2
        // count the occurence
        for( int i: nums )  count[ i ]++;
        
        for( int i = 0; i < nums.length; i++ )
        {
            if( i < count[ 0 ] )
                nums[ i ] = 0;
            else if( i < (count[ 0 ] + count[ 1 ]) )
                nums[ i ] = 1;
            else
                nums[ i ] = 2;
        }
    }
}