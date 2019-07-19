package app;

import java.util.*;

class Q216_combination_sum_3
{
    public List<List<Integer>> combinationSum3(int k, int n)
    {
        boolean[] flag = new boolean[ 10 ];
        Arrays.fill( flag, false );
        List<List<Integer>> sol = new ArrayList<List<Integer>>();
        backtracking( sol, new ArrayList<Integer>(), flag, k, n, 1);
        return sol;
    }
    
    public void backtracking( List<List<Integer>> sol, List<Integer> tmp, boolean[] flag, int k, int remain, int start )
    {
        if( tmp.size() > k || remain < 0 ) return;
        else if( tmp.size() == k && remain == 0 ) sol.add( new ArrayList<Integer>( tmp ) );
        else
        {
            for( int i = start; i < 10; i++ )
            {
                if( flag[ i ] ) continue;
                flag[ i ] = true;
                tmp.add( i );
                backtracking( sol, tmp, flag, k, remain - i, i+1 );
                flag[ i ] = false;
                tmp.remove( tmp.size() - 1 );
            }
        }
    }
}