package app;

// brute-force
// time-limit exceeded!!
class Q70_climbing_stairs_BF {
    public int climbStairs(int n)
    {
        return climb( 0, n );
    }
    
    public int climb( int steps, int remainings )
    {
        // not a solution
        if( steps > remainings )    return 0;
        // a solution
        if( steps == remainings )   return 1;
        // not yet
        return climb( steps + 1, remainings ) + climb( steps + 2, remainings );
    }
}