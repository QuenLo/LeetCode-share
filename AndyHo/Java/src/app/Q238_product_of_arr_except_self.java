// ref. https://leetcode.com/problems/product-of-array-except-self/discuss/65622/Simple-Java-solution-in-O(n)-without-extra-space

package app;

class Q238_product_of_arr_except_self
{
    // Numbers:     2    3    4     5
    // Lefts:            2  2*3 2*3*4
    // Rights:  3*4*5  4*5    5 
    public int[] productExceptSelf(int[] nums)
    {
        int n = nums.length;
        int[] res = new int[ n ];
        
        // calculating left
        int left = 1;
        for( int i = 0; i < n; i++ )
        {
            if( i > 0 ) left = left * nums[ i - 1 ];
            res[ i ] = left;
        }
        
        // calculating right
        int right = 1;
        for( int i = n - 1; i >= 0; i-- )
        {
            if( i < n - 1 ) right = right * nums[ i + 1 ];
            res[ i ] *= right;
        }
        return res;
    }
}