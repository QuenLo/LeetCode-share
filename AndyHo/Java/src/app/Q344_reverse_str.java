package app;

class Q344_reverse_str
{
    public void reverseString(char[] s)
    {
        int left = 0, right = s.length - 1;
        while( left < right && right >= 0 && left < s.length )
        {
            char tmp = s[ left ];
            s[ left ] = s[ right ];
            s[ right ] = tmp;

            left++;
            right--;
        }
    }
}