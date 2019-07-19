package app;

class Q35_search_insert_pos_binary_search {
    public int searchInsert(int[] nums, int target) {
        int i = 0, j = nums.length - 1, l = 0;
        while( i <= j )
        {
            l = (i + j) / 2;
            if( nums[ l ] == target ) return l;
            else if( nums[ l ] < target ) i = l + 1;
            else j = l - 1;
        }
        return i;
    }
}