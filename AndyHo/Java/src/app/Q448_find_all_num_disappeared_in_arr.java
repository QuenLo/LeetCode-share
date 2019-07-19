package app;

import java.lang.Math;
import java.util.List; 
import java.util.ArrayList; 

class Q448_find_all_num_disappered_in_arr {
    public List<Integer> findDisappearedNumbers(int[] nums)
    {
        for( int i = 0; i < nums.length; i++ )
        {
            // make sure the index will not exceed
            int record = Math.abs( nums[ i ] ) - 1;
            // if the number exist, mark the corresponding location by converting to neg. val.
            // make sure to reserve the original value!!!
            nums[ record ] = -Math.abs( nums[ record ] );
        }
        // find all the cell with value larger than 0 (no record)
        List<Integer> arr = new ArrayList<Integer>();
        for( int i = 0; i < nums.length; i++ )
            if( nums[ i ] > 0 ) arr.add( i + 1 );
        return arr;
    }
}