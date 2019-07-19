package app;

class Q219_contains_dup_2_BF
{
    public boolean containsNearbyDuplicate(int[] nums, int k)
    {
        for( int i = 0; i < nums.length; i++ )
            for( int j = i+1; j <= i+k; j++ )
            {
                if( j >= nums.length ) break;
                if( nums[ i ] == nums[ j ] ) return true;
            }
        return false;
    }
}