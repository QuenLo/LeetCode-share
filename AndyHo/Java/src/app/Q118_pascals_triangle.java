package app;

import java.util.*;

class Q118_pascals_triangle
{
    public List<List<Integer>> generate(int numRows)
    {
        // ArrayList has index
        List<List<Integer>> triangle = new ArrayList<List<Integer>>();
        if( numRows == 0 ) return triangle;
        // first row
        triangle.add( new ArrayList<Integer>() );
        triangle.get( 0 ).add( 1 );
        
        for( int i = 1; i < numRows; i++ )
        {
            List<Integer> row = new ArrayList<Integer>();
            
            for( int j = 0; j <= i; j++ )
            {
                if( j == 0 || j == i ) row.add( 1 );
                else
                    row.add( triangle.get( i - 1 ).get( j - 1 ) + triangle.get( i - 1 ).get( j ) );
            }
            triangle.add( row );
        }
        return triangle;
    }
}