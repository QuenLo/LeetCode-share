// ref. https://leetcode.com/problems/sum-of-two-integers/discuss/84290/Java-simple-easy-understand-solution-with-explanation

package app;

class Q371_sum_of_2_integers
{
    public int getSum(int a, int b)
    {
        while( b != 0 )
        {
            int carry = a & b;
            a = a ^ b;
            b = carry << 1;
        }
        return a;
    }
}