package app;

public class Q191_number_of_1_bits_LOOP
{
    // you need to treat n as an unsigned value
    public int hammingWeight( int n )
    {
        if( n > Integer.MAX_VALUE ) return 1;
        int bits = 0, mask = 1;
        for( int i = 0; i < 32; i++ )
        {
            if( (n & mask) != 0 ) bits++;
            mask <<= 1; // mask *= 2;
        }
        return bits;
    }
}