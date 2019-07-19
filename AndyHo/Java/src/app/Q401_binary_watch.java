// ref. https://leetcode.com/problems/binary-watch/discuss/215205/Java-backtracking-solution

package app;

import java.lang.Math;
import java.util.*;

class Q401_binary_watch {
    int numOfLights = 10;
    List<String> sol = new ArrayList<String>();

    public List<String> readBinaryWatch(int num)
    {
        backtrack( 0, num, 0, 0 );
        return sol;
    }
    
    /*
     * input:
     *      index: light index
     *      num:   num. of lights on
     */
    public void backtrack( int index, int num, int hour, int minute )
    {
        // out of bound
        if( hour > 11 || minute > 59 ) return;
        // got solution
        if( num == 0 )
        {
            sol.add( timeString( hour, minute ) );
            return;
        }
        
        // totally 10 lights, first 4 light for hours, remaining 6 lights for minutes
        for( int i = index; i < numOfLights; i++ )
        {
            // lights for hours (index 0 - 3)
            if( i < 4 )
            {
                int cur_hour = hour + (int) Math.pow( 2, i );
                backtrack( (i + 1), (num - 1), cur_hour, minute );
            }
            // lights for minutes (index 4 - 9)
            else
            {
                int cur_minute = minute + (int) Math.pow( 2, i - 4 ); // first 4 lights are for hours
                backtrack( (i + 1), (num - 1), hour, cur_minute );
            }
        }
    }
    
    public String timeString( int hour, int minute )
    {
        if( minute < 10 )
            return Integer.toString( hour ) + ":0" + Integer.toString( minute );
        else
            return Integer.toString( hour ) + ":" + Integer.toString( minute );
    }
}