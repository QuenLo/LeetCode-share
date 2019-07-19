// ref. https://leetcode.com/problems/sqrtx/discuss/25047/A-Binary-Search-Solution

package app;

class Q69_sqrt
{
    public int mySqrt(int x)
    {
        if( x == 0 ) return x;

        int left = 1, right = x;
        while( left <= right )
        {
            int mid = left + (right - left)/2;
            if( mid == x/mid )
                return mid;
            else if( mid < x / mid )
                left = mid + 1;
            else
                right = mid - 1;
        }
        return right;
    }
}