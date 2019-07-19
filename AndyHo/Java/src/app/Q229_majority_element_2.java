package app;

import java.util.List;
import java.util.ArrayList;

class Q229_majority_element_2 {
    public List<Integer> majorityElement(int[] nums)
    {
        List<Integer> sol = new ArrayList<Integer>();
        
        // since the condition is count > n/3, only 2 or less numbers will be the majority
        int cand1 = 0, cand2 = 0;
        int cnt1 = 0, cnt2 = 0;
        
        for( int n : nums )
        {
            if( n == cand1 )        cnt1++;
            else if( n == cand2 )   cnt2++;
            // couldn't put at front, both candidate will be the same number
            else if( cnt1 == 0 )
            {
                cand1 = n;
                cnt1++;
            }
            else if( cnt2 == 0 )
            {
                cand2 = n;
                cnt2++;
            }
            else
            {
                cnt1--;
                cnt2--;
            }
        }

        // get the acutal count for all the candidates
        cnt1 = 0;
        cnt2 = 0;
        for( int n : nums )
        {
            if( n == cand1 ) cnt1++;
            // prevent the case [0, 0, 0] to return [0, 0]
            else if( n == cand2 ) cnt2++;
        }
        
        if( cnt1 > nums.length/3 ) sol.add( cand1 );
        if( cnt2 > nums.length/3 ) sol.add( cand2 );
        
        return sol;
    }
}