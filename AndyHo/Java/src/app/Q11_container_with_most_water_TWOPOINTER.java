package app;

import java.lang.Math;

class Q11_container_with_most_water_TWOPOINTER
{
    public int maxArea(int[] height)
    {
        int sol = Integer.MIN_VALUE, l = 0, r = height.length - 1;
        while( r > l )
        {
            sol = Math.max( sol, Math.min( height[ l ], height[ r ] ) * ( r - l ) );
            // volume is limited by the shorter line
            if( height[ l ] < height[ r ] )
                l++;
            else
                r--;
        }
        return sol;
    }
}