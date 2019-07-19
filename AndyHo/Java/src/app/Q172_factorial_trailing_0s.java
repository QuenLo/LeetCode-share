package app;

class Q172_factorial_trailing_0s
{
    // 10 is the product of 2 and 5. In n!, we need to know how many 2 and 5, and the number of zeros is the minimum of the number of 2 and the number of 5
    // Since multiple of 2 is more than multiple of 5, the number of zeros is dominant by the number of 5
    // Here is the basic solution: return n/5 + n/25 + n/125 + n/625 + n/3125+...;
    public int trailingZeroes( int n )
    {
        if( n == 0 ) return 0;
        else
            return n / 5 + trailingZeroes( n / 5 );
    }

    // brute force, overflow!!!!!!
    // public int trailingZeroes(int n)
    // {
    //     int mult = 1;
    //     for( int i = n; i >= 1; i-- ) mult *= i;
    //     String s = Integer.toString( mult );
    //     int count = 0;
    //     for( int i = s.length() - 1; i >= 0; i-- )
    //     {
    //         if( s.charAt( i ) != '0' ) break;
    //         if( s.charAt( i ) == '0' ) count++;
    //     }
    //     return count;
    // }
}