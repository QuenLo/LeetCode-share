package app;

import java.util.*;

class Q46_permutations
{
    public List<List<Integer>> permute(int[] nums)
    {
        List<List<Integer>> sol = new ArrayList<List<Integer>>();
        if( nums.length == 0 ) return sol;
        backtracking( sol, new ArrayList<Integer>(), nums );
        return sol;
    }
    
    public void backtracking( List<List<Integer>> sol, List<Integer> tmp, int[] nums )
    {
        if( tmp.size() == nums.length )
            sol.add( new ArrayList<Integer>( tmp ) );
        else
        {
            for( int i = 0; i < nums.length; i++ )
            {
                // the list already has the element
                if( tmp.contains( nums[ i ] ) ) continue;
                tmp.add( nums[ i ] );
                backtracking( sol, tmp, nums );
                // let the program try other possibilities
                tmp.remove( tmp.size() - 1 );
            }
        }
    }
}