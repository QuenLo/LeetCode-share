// ref. https://stackoverflow.com/questions/2406432/converting-an-int-to-a-binary-string-representation-in-java

package app;

class Q338_counting_bits_BF
{
    public int[] countBits(int num)
    {
        int[] sol = new int[ (num + 1) ];
        for( int i = 0; i <= num; i++ )
        {
            String s = intToBinString( i );
            int count = 0;
            for( int j = 0; j < s.length(); j++ )
                if( s.substring( j, j+1 ).contains( "1" ) ) count++;
            sol[ i ] = count;
        }
        return sol;
    }
    
    public String intToBinString( int n )
    {
        String s = "";
        while( n > 0 )
        {
            s = ( (n % 2 == 0) ? "0" : "1" ) + s;
            n /= 2;
        }
        return s;
    }
}