package app;

// improved brute-force
class Q70_climbing_stairs_MEM_BF {
    public int climbStairs(int n)
    {
        // brute-force
        // return brute_force( 0, n );
        
        // (n+1) since to exactly store the status for walking 3 steps at cell [3]!!
        int[] mem = new int[ (n + 1) ];
        return memo_bf( 0, n, mem );
    }
    
    public int brute_force( int steps, int remainings )
    {
        // not a solution
        if( steps > remainings )    return 0;
        // a solution
        if( steps == remainings )   return 1;
        // not yet
        return brute_force( steps + 1, remainings ) + brute_force( steps + 2, remainings );
    }
    
    public int memo_bf( int steps, int remainings, int[] mem )
    {
        // not a solution
        if( steps > remainings )    return 0;
        // a solution
        if( steps == remainings )   return 1;
        
        // if a solution already exists
        // should be placed here to prevent outOfBound exception!!
        if( mem[ steps ] != 0 )         return mem[ steps ];
        
        // store the solution
        mem[ steps ] = memo_bf( steps + 1, remainings, mem ) + memo_bf( steps + 2, remainings, mem );
        return mem[ steps ];
    }
}