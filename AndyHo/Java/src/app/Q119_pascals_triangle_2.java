// ref. https://leetcode.com/problems/pascals-triangle-ii/discuss/38420/Here-is-my-brief-O(k)-solution

package app;

import java.util.*;

class Q119_pascals_triangle_2
{
    public List<Integer> getRow(int rowIndex)
    {
        List<Integer> row = new ArrayList<Integer>();
        row.add( 1 );
        if( rowIndex == 0 ) return row;

        for( int i = 1; i <= rowIndex; i++ )
        {
            for( int j = i - 1; j >= 1; j-- )
                row.set( j, (row.get( j - 1 ) + row.get( j )) );
            // make up the space for the next row
            row.add( 1 );
        }
        return row;
    }
}