package app;

import java.util.Map;
import java.util.HashMap;

class Q771_jewels_and_stones {
    public int numJewelsInStones(String J, String S)
    {
        HashMap<Character, Integer> dict = new HashMap<Character, Integer>();
        for( int i = 0; i < J.length(); i++ )
            dict.put( J.charAt( i ), 0 );
        for( int i = 0; i < S.length(); i++ )
        {
            if( dict.get( S.charAt( i ) ) != null )
            {
                dict.put( S.charAt( i ), dict.get( S.charAt( i ) ) + 1 );
            }
        }
        int sol = 0;
        for( Map.Entry<Character, Integer> entry : dict.entrySet() )
            sol += entry.getValue();
        return sol;
    }
}