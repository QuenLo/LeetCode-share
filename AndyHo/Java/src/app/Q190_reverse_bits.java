// ref. https://leetcode.com/problems/reverse-bits/discuss/54738/Sharing-my-2ms-Java-Solution-with-Explanation

package app;

public class Q190_reverse_bits {
    // you need treat n as an unsigned value
    public int reverseBits(int n)
    {
        // do nothing if n == 0
        if( n == 0 ) return 0;
        
        int sol = 0;
        for( int i = 0; i < 32; i++ )
        {
            // shift left
            sol <<= 1;
            // get the last bit of n and add to sol
            if( (n & 1) == 1 ) sol++;
            // shift right
            n >>= 1;
        }
        return sol;
    }
}