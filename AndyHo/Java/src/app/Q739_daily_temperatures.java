// https://leetcode.com/problems/daily-temperatures/discuss/109869/JavaC%2B%2B-Clean-Code

package app;

import java.lang.Math;
import java.util.*;

class Q739_daily_temperatures
{
    public int[] dailyTemperatures(int[] T)
    {
        int n = T.length;
        int[] waits = new int[ n ];
        Arrays.fill( waits, 0 );
        // max. temperature is 100
        // store the corresponding index of a certain temperature in T
        int[] next = new int[ 101 ];
        for( int i = n - 1; i >= 0; i-- )
        {
            int earliest = Integer.MAX_VALUE;
            // try to find the earliest temp in T that is larger than the current temperature
            // var earliest stores the index if found
            for( int j = T[ i ] + 1; j <= 100; j++ )
            {
                if( next[ j ] != 0 )
                    earliest = Math.min( earliest, next[ j ] );
            }
            if( earliest != Integer.MAX_VALUE )
                waits[ i ] = earliest - i;
            next[ T[ i ] ] = i;
        }
        return waits;
    }
}
