// ref. https://leetcode.com/problems/count-primes/discuss/57593/12-ms-Java-solution-modified-from-the-hint-method-beats-99.95

package app;

class Q204_count_primes_MATH
{
    public int countPrimes(int n)
    {
        if( n <= 0 ) return 0;
        
        boolean[] is_prime = new boolean[ n ];
        // initialize
        for( int i = 2; i < n; i++ ) is_prime[ i ] = true;

        for( int i = 2; i * i < n; i++ )
        {
            if( !is_prime[ i ] ) continue;
            // marking the non-primes
            // we can always mark off multiples of p starting at p*p
            for( int j = i * i; j < n; j += i )
                is_prime[ j ] = false;
        }

        int count = 0;
        for( int i = 2; i < n; i++ )
            if( is_prime[ i ] ) count++;
        return count;
    }
}