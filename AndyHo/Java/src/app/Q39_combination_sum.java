package app;

import java.util.*;

class Q39_combination_sum
{
    public List<List<Integer>> combinationSum(int[] candidates, int target)
    {
        List<List<Integer>> sol = new ArrayList<List<Integer>>();
        if( candidates.length == 0 ) return sol;
        backtracking( sol, new ArrayList<Integer>(), candidates, target, 0 );
        return sol;
    }
    
    public void backtracking( List<List<Integer>> sol, List<Integer> tmp, int[] candi, int remain, int start )
    {
        if( remain < 0 )        return;
        else if( remain == 0 )  sol.add( new ArrayList<Integer>( tmp ) );
        else
        {
            for( int i = start; i < candi.length; i++ )
            {
                tmp.add( candi[ i ] );
                // start of next recursion = i since the element could be reused
                backtracking( sol, tmp, candi, remain - candi[ i ], i );
                tmp.remove( tmp.size() - 1 );
            }
        }
    }
}