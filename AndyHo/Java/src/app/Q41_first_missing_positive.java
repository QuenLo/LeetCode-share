package app;

import java.lang.Math;

class Q41_first_missing_positive
{
    public int firstMissingPositive(int[] nums)
    {
        if( nums.length == 0 ) return 1;
        // 1. mark the number < 0 or > n by a marker number (n+1)
        for( int i = 0; i < nums.length; i++ )
            if( nums[ i ] <= 0 || nums[ i ] > nums.length )
                nums[ i ] = (nums.length + 1);

        // 2. mark cell corresponding to the existing number
        for( int i = 0; i < nums.length; i++ )
        {
            int n = Math.abs( nums[ i ] );
            if( n > nums.length ) continue;
            // arr is 0-indexed
            n--;
            if( nums[ n ] > 0 ) nums[ n ] = -1 * nums[ n ];
        }
        
        // 3. find the solution (the first cell with pos value)
        for( int i = 0; i < nums.length; i++ )
            if( nums[ i ] >= 0 ) return (i + 1);
        
        // 4. no positive numbers were found, which means the array contains all numbers 1..n
        return (nums.length + 1);
    }
}