// ref. https://leetcode.com/problems/perfect-squares/discuss/71495/An-easy-understanding-DP-solution-in-Java

package app;

public class Q279_perfect_squares
{
    public int numSquares(int n)
    {
        int[] dp = new int[ n+1 ];
        dp[ 0 ] = 0;
        for( int i = 1; i <= n; i++ )
        {
            // findint the square number <= i
            // solution for i is the sum of (the solution for all the non-perfect square num + 1)
            for( int j = 1; j * j <= i; j++ )
                dp[ i ] = Math.min( dp[ i ], dp[ i - j*j ] + 1 );
        }
        return dp[ n ];
    }
}