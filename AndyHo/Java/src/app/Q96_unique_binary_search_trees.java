// ref. https://leetcode.com/problems/unique-binary-search-trees/discuss/31666/DP-Solution-in-6-lines-with-explanation.-F(i-n)-G(i-1)-*-G(n-i)

package app;

class Q96_unique_binary_search_trees
{
    public int numTrees(int n)
    {
        // G( 2 ) = F( 1, 2 ) + F( 2, 2 ), G = dp
        // F( 1, 2 ) = G( 0 ) * G( 1 )

        int[] dp = new int[ n + 1 ];
        dp[ 0 ] = 1;
        dp[ 1 ] = 1;
        
        for( int i = 2; i <= n ; i++ )
            for( int j = 1; j <= i; j++ )
            {
                dp[ i ] += dp[ j - 1 ] * dp[ i - j ];
            }
            
        return dp[ n ];
    }
}