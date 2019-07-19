// ref. http://www.csie.ntnu.edu.tw/~u91029/Function.html#4

package app;

class Q287_find_duplicate_number
{
    // notes that the value in arr is within n!!
    // which means the arr could be traversed infinitely (cycle)
    public int findDuplicate(int[] nums)
    {
        // phase 1
        // hare is faster than tortoise
        int tortoise = nums[ 0 ];
        int hare = nums[ 0 ];
        do
        {
            tortoise = nums[ tortoise ];
            hare = nums[ nums[ hare ] ];
        } while( tortoise != hare );

        // phase 2
        // find the cycle start point
        // hare and tortoise have the same speed
        hare = tortoise;
        tortoise = nums[ 0 ];
        while( tortoise != hare )
        {
            tortoise = nums[ tortoise ];
            hare = nums[ hare ];
        }

        return tortoise;
    }
}