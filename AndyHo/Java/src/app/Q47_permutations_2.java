// ref. https://leetcode.com/problems/permutations/discuss/18239/A-general-approach-to-backtracking-questions-in-Java-(Subsets-Permutations-Combination-Sum-Palindrome-Partioning)

package app;

import java.util.*;

class Q47_permutations_2
{
    public List<List<Integer>> permuteUnique(int[] nums)
    {
        List<List<Integer>> sol = new ArrayList<List<Integer>>();
        if( nums.length == 0 ) return sol;
        // flag array
        boolean[] used = new boolean[ nums.length ];
        Arrays.fill( used, false );
        // sort the nums arr
        Arrays.sort( nums );
        backtracking( sol, new ArrayList<Integer>(), nums, used );
        return sol;
    }
    
    public void backtracking( List<List<Integer>> sol, List<Integer> tmp, int[] nums, boolean[] used )
    {
        if( tmp.size() == nums.length )
            sol.add( new ArrayList<Integer>( tmp ) );
        else
        {
            for( int i = 0; i < nums.length; i++ )
            {
                // the list already has the element and this is the one been used before;
                // the condition (i > 0 && nums[ i ] == nums[ i - 1 ] && !used[ i - 1 ]) means
                // if an element equals to the element before it,
                // and the element before this element is not used in the permutation yet,
                // we also skip it!
                // ex. case [ 1 (1a), 1 (1b), 1 (1c), 1 (1d) ]
                // make sure that 1a element is added to the result first, then 1b, then 1c, then 1d.
                // in this case, we can only get 1 result, instead of getting 4!.
                if( used[ i ] || i > 0 && nums[ i ] == nums[ i - 1 ] && !used[ i - 1 ] ) continue;
                tmp.add( nums[ i ] );
                used[ i ] = true;
                backtracking( sol, tmp, nums, used );
                // let the program try other possibilities
                tmp.remove( tmp.size() - 1 );
                used[ i ] = false;
            }
        }
    }
}