package app;

class Q35_search_insert_pos {
    public int searchInsert(int[] nums, int target) {
        int i = 0;
        for( ; i < nums.length; i++ )
        {
            if( nums[ i ] < target )
                continue;
            else
                return i;
        }
        return i;
    }
}