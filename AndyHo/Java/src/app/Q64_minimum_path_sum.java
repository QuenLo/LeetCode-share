// ref. https://leetcode.com/problems/minimum-path-sum/discuss/23471/DP-with-O(N*N)-space-complexity

package app;

import java.lang.Math;

class Q64_minimum_path_sum
{
    public int minPathSum(int[][] grid)
    {
        int m = grid.length, n = grid[ 0 ].length;
        
        // initialization
        for( int i = 1; i < m; i++ )
            grid[ i ][ 0 ] += grid[ i - 1 ][ 0 ];
        for( int i = 1; i < n; i++ )
            grid[ 0 ][ i ] += grid[ 0 ][ i - 1 ];

        for( int i = 1; i < m; i++ )
            for( int j = 1; j < n; j++ )
                grid[ i ][ j ] += Math.min( grid[ i - 1 ][ j ], grid[ i ][ j - 1 ] );
        return grid[ m-1 ][ n-1 ];   
    }
}