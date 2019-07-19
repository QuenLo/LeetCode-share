package app;

import java.lang.Math;

class Q11_container_with_most_water_BF
{
    public int maxArea(int[] height)
    {
        int sol = Integer.MIN_VALUE;
        for( int i = 0; i < height.length; i++ )
            for( int j = i + 1; j < height.length; j++ )
            {
                int volume = Math.min( height[ i ], height[ j ] ) * (j - i);
                sol = Math.max( sol, volume );
            }
        return sol;
    }
}