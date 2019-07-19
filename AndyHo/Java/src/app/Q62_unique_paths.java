// ref. https://leetcode.com/problems/unique-paths/discuss/22953/Java-DP-solution-with-complexity-O(n*m)

package app;

class Q62_unique_paths
{
    // public int uniquePaths(int m, int n)
    // {
    //     int[][] map = new int[ m+1 ][ n+1 ];
    //     // the robot could only go right or down
    //     for( int i = 0; i < m; i++ ) map[ i ][ 0 ] = 1;
    //     for( int i = 0; i < n; i++ ) map[ 0 ][ i ] = 1;
        
    //     // result = uniquePaths(m-1,n) + uniquePaths(m,n-1)
    //     for( int i = 1; i < m; i++ )
    //         for( int j = 1; j < n; j++ )
    //         {
    //             map[ i ][ j ] = map[ i -1 ][ j ] + map[ i ][ j - 1];
    //         }
    //     return map[ m-1 ][ n-1 ];
    // }

    // simplifed
    public int uniquePaths(int m, int n)
    {
        int[][] map = new int[ m+1 ][ n+1 ];

        // result = uniquePaths(m-1,n) + uniquePaths(m,n-1)
        // The top row of 1s is always filled first, but the question of the left-most column depends on the fact that the loops actually go left-to-right on each row before advancing.
        // As a result, you always get a 1 filled on the left-most cell before you start filling out the stuff on the right.
        for( int i = 0; i < m; i++ )
            for( int j = 0; j < n; j++ )
            {
                if( i == 0 || j == 0 ) map[ i ][ j ] = 1;
                else
                    map[ i ][ j ] = map[ i -1 ][ j ] + map[ i ][ j - 1];
            }
        return map[ m-1 ][ n-1 ];
    }
}