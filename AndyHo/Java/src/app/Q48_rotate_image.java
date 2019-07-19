// ref. https://leetcode.com/problems/rotate-image/discuss/18872/A-common-method-to-rotate-the-image

package app;

class Q48_rotate_image
{
    public void rotate(int[][] matrix)
    {
        int p1 = 0, p2 = matrix.length - 1;
        // reverse row 0 with row n-1, then 1 with row n-2, and so on
        while( p1 < p2 )
        {
            int[] tmp = matrix[ p1 ];
            matrix[ p1 ] = matrix[ p2 ];
            matrix[ p2 ] = tmp;
            
            p1++; p2--;
        }

        // swap the matrix symmetrically
        for( int i = 0; i < matrix.length; i++ )
            for( int j = i + 1; j < matrix[ 0 ].length; j++ )
            {
                int tmp = matrix[ i ][ j ];
                matrix[ i ][ j ] = matrix[ j ][ i ];
                matrix[ j ][ i ] = tmp;
            }
    }
}