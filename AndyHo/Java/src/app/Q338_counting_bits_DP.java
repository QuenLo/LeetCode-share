// ref. https://leetcode.com/problems/counting-bits/discuss/79812/Simple-Java-Dynamic-Programming-without-any-bitwise-operation

package app;

// dynamic programming
class Q338_counting_bits_DP
{
    public int[] countBits(int num)
    {
        int[] sol = new int[ num + 1 ];
        for( int i = 0; i <= num; i++ )
        {
            sol[ i ] = sol[ (int) Math.floor( i/2 ) ];
            if( (i % 2) == 1 ) sol[ i ] ++;
        }
        return sol;
    }
}