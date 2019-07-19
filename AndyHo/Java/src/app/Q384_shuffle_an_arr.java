// ref. https://www.mkyong.com/java/java-generate-random-integers-in-a-range/

package app;

import java.util.*;

class Q384_shuffle_an_arr
{
    private int[] array = null;
    private int[] original = null;
    private Random rand = new Random();
    
    public Q384_shuffle_an_arr(int[] nums)
    {
        array = nums;
        // remeber Java is call by reference
        original = nums.clone();
    }
    
    /** Resets the array to its original configuration and return it. */
    public int[] reset()
    {
        array = original;
        original = original.clone();
        return original;
    }
    
    /** Returns a random shuffling of the array. */
    public int[] shuffle()
    {
        for( int i = 0; i < array.length; i++ )
        {
            int j = randIndex( i, array.length );
            swap( array, i, j );
        }
        return array;
    }
    
    private int randIndex( int min, int max )
    {
        if( min > max ) return min;
        // return number between max and min
        return rand.nextInt( max - min ) + min;
    }
    
    private void swap( int[] nums, int a, int b )
    {
        int tmp = nums[ a ];
        nums[ a ] = nums[ b ];
        nums[ b ] = tmp;
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(nums);
 * int[] param_1 = obj.reset();
 * int[] param_2 = obj.shuffle();
 */