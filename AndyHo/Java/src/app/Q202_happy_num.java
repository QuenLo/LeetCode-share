// ref. [Explanation] https://leetcode.com/problems/happy-number/discuss/117136/c++-using-Floyd-Cycle-Detection-Algorithm
// ref. [Explanation] https://leetcode.com/problems/happy-number/discuss/56918/All-you-need-to-know-about-testing-happy-number!
// ref. [Solution] https://leetcode.com/problems/happy-number/discuss/56917/My-solution-in-C(-O(1)-space-and-no-magic-math-property-involved-)

package app;

class Q202_happy_num
{
    // loop detection
    // Tortoise and Hare Algorithm (Floyd Cycle Detection)
    // a loop must exist if not happy (the process will never end!)
    public boolean isHappy(int n)
    {
        int slow = n, fast = n;
        do
        {
            slow = digitSquareSum( slow );
            fast = digitSquareSum( digitSquareSum( fast ) );
        }
        while( slow != fast );
        if( slow == 1 ) return true;
        else            return false;
    }
    
    public int digitSquareSum( int n )
    {
        int sum = 0, digit = 0;
        while( n > 0 )
        {
            digit = n % 10;
            sum += digit * digit;
            n /= 10;
        }
        return sum;
    }
}