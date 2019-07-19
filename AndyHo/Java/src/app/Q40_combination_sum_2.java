package app;

import java.util.*;

class Q40_combination_sum_2
{
    public List<List<Integer>> combinationSum2(int[] candidates, int target)
    {
        ArrayList<List<Integer>> sol = new ArrayList<List<Integer>>();
        // important step!
        Arrays.sort( candidates );
        if( candidates.length == 0 ) return sol;
        backtracking( sol, new ArrayList<Integer>(), candidates, target, 0 );
        return sol;
    }

    public void backtracking( ArrayList<List<Integer>> sol, List<Integer> tmp, int[] candi, int remain, int start )
    {
        if( remain < 0 ) return;
        else if( remain == 0 ) sol.add( new ArrayList<Integer>( tmp ) );
        else
        {
            for( int i = start; i < candi.length; i++ )
            {
                if( i > start && candi[ i ] == candi[ i - 1 ] ) continue;
                tmp.add( candi[ i ] );
                // start of next recursion = i + 1 since the same element should be passed
                backtracking( sol, tmp, candi, remain - candi[ i ], i + 1 );
                tmp.remove( tmp.size() - 1 );
            }
        }
    }
}