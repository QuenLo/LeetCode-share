// ref. https://leetcode.com/problems/find-all-anagrams-in-a-string/discuss/92007/Sliding-Window-algorithm-template-to-solve-all-the-Leetcode-substring-search-problem.

package app;

import java.util.*;

class Q438_find_all_anagrams_in_string
{
    public List<Integer> findAnagrams( String s, String p )
    {
        List<Integer> result = new LinkedList<>();
        if( p.length() > s.length() ) return result;

        Map<Character, Integer> map = new HashMap<>();
        // initialize the map
        for( char c : p.toCharArray() )
            map.put( c, map.getOrDefault( c, 0 ) + 1 );

        // input p = "abc", map size = 3
        int counter = map.size();

        int begin = 0, end = 0;
        while( end < s.length() )
        {
            char c = s.charAt( end );
            if( map.containsKey( c ) )
            {
                map.put( c, map.get( c ) - 1 );
                if( map.get( c ) == 0 ) counter--;
            }
            end++;

            while( counter == 0 )
            {
                char tmpc = s.charAt( begin );
                if( map.containsKey( tmpc ) )
                {
                    map.put( tmpc, map.get( tmpc ) + 1 );
                    if( map.get( tmpc ) > 0 ) counter++;
                }
                // found the solution
                if( end-begin == p.length() ) result.add(begin);
                begin++;
            }
        }
        return result;
    }
}