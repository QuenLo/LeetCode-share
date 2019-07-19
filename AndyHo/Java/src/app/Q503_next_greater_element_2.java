package app;

import java.util.*;

// class Solution {
//     public int[] nextGreaterElements(int[] nums)
//     {
//         int len  = nums.length, i = 0;
//         if( len == 0 ) return new int[ 0 ];
        
//         Map<Integer, Integer> map = new HashMap<Integer, Integer>();
//         Stack<Integer> stack = new Stack<Integer>();

//         boolean atLeastOne = false;
//         while( true )
//         {
//             if( i == len )
//             {
//                 atLeastOne = true;
//                 i = 0;
//             }
//             while( !stack.isEmpty() && stack.peek() < nums[ i ] )
//             {
//                 int e = stack.pop();
//                 if( !map.containsKey( e ) ) map.put( e, nums[ i ] );
//             }
//             if( !stack.isEmpty() && stack.peek() == nums[ i ] && atLeastOne ) break;
//             stack.push( nums[ i ] );
//             i++;
//         }

//         // get the answer
//         int[] sol = new int[ len ];
//         for( i = 0; i < len; i++ )
//             sol[ i ] = map.getOrDefault( nums[ i ], -1 );
//         return sol;
//     }
// }

class Q503_next_greater_element_2
{
    // top of the stack refers to the index of the next greater element found so far
    // store the indices instead of the elements since there could be dups
    public int[] nextGreaterElements(int[] nums)
    {
        int len = nums.length;
        int[] sol = new int[ len ];
        Stack<Integer> stack = new Stack<Integer>();
        for( int i = 2 * len - 1; i >= 0; i-- )
        {
            while( !stack.isEmpty() && nums[ stack.peek() ] <= nums[ i % len ] )
                stack.pop();
            if( stack.isEmpty() )
                sol[ i % len ] = -1;
            else
                sol[ i % len ] = nums[ stack.peek() ];
            // push the index
            stack.push( i % len );
        }
        return sol;
    }
}