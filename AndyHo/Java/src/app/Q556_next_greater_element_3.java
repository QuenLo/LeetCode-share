// ref. https://leetcode.com/problems/next-greater-element-iii/discuss/101824/Simple-Java-solution-(4ms)-with-explanation.

package app;

import java.util.*;

class Q556_next_greater_element_3
{
    public int nextGreaterElement(int n)
    {
        String in = Integer.toString( n );
        String[] digits = new String[ in.length() ];
        for( int i = 0; i < digits.length; i++ )
            digits[ i ] = in.substring( i, i+1 );
        
        int i = 0, j = 0;
        // find the first digit that is smaller than before
        for( i = in.length() - 1; i > 0; i-- )
            if( Integer.parseInt( digits[ i - 1 ] ) < Integer.parseInt( digits[ i ] ) )
                break;
        
        // no solution (case I, descending order, ex. 432)
        if( i == 0 ) return -1;
        
        // find the smallest digit that is larger than nums[ (i - 1) ]
        int x = Integer.parseInt( digits[ i - 1 ] ), smallest = i;
        for( j = i+1; j < digits.length; j++ )
            if( Integer.parseInt( digits[ j ] ) > x &&
                Integer.parseInt( digits[ j ] ) <= Integer.parseInt( digits[ smallest ] ) )
                smallest = j;
        
        // swap the two digits
        String tmp = digits[ i-1 ];
        digits[ i-1 ] = digits[ smallest ];
        digits[ smallest ] = tmp;
        
        // sort the arrary after i-1
        Arrays.sort( digits, i, in.length() );

        // the tricky part for this question is the final result could go beyond Integer.MAX_VALUE
        // ex. 1999999999
        long val = Long.parseLong( String.join( "", digits ) );
        return (val <= Integer.MAX_VALUE) ? (int) val : -1;
    }
}