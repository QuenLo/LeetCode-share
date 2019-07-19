// ref. [Algorithm] https://www.wikiwand.com/zh-hant/%E7%B4%A0%E6%80%A7%E6%B5%8B%E8%AF%95

package app;

class Q204_count_primes_DP
{
    public int countPrimes(int n)
    {
        if( n <= 0 ) return 0;
        
        int[] dp = new int[ n + 1 ];
        dp[ 0 ] = 0;
        dp[ 1 ] = 0;
        
        for( int i = 2; i <= n; i++ )
        {
            if( isPrime( i ) )
                dp[ i ] = dp[ i - 1 ] + 1;
            else
                dp[ i ] = dp[ i - 1];
        }
        return dp[ n - 1  ];
    }
    
    public boolean isPrime( int n )
    {
        if( n <= 1 ) return false;
        for( int i = 2; i * i <= n; i++ )
            if( n % i == 0 ) return false;
        return true;
    }
}