// ref. https://leetcode.com/problems/powx-n/discuss/19544/5-different-choices-when-talk-with-interviewers

package app;

class Q50_pow
{
    public double myPow(double x, int n)
    {
        if(n >= 0) return helper( x, n );
        return 1 / helper( x, n );
    }
    
    private double helper( double x, int n )
    {
        if( n == 0 ) return 1;
        double half = helper( x, n/2 );
        
        if( n%2 == 0 )  return half*half;
        
        // for the iteration n == 1
        return half*half*x;
    }
}