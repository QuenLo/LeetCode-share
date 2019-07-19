package app;

public class Q191_number_of_1_bits_BIT_MANI
{
    // you need to treat n as an unsigned value
    public int hammingWeight( int n )
    {
        int bits = 0;
        while( n != 0 )
        {
            bits++;
            n &= (n - 1);
        }
        return bits;
    }
}