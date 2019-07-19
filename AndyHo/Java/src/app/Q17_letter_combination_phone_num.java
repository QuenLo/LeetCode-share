package app;

import java.util.*;

class Q17_letter_combination_phone_num {
    Map<String, String> map = new HashMap<String, String>();
    List<String> sol = new ArrayList<String>();

    public List<String> letterCombinations(String digits)
    {
        // build the map
        map.put( "2", "abc" );
        map.put( "3", "def" );
        map.put( "4", "ghi" );
        map.put( "5", "jkl" );
        map.put( "6", "mno" );
        map.put( "7", "pqrs" );
        map.put( "8", "tuv" );
        map.put( "9", "wxyz" );
        
        // start
        if( digits.length() != 0 ) backtrack( "", digits );
        return sol;
    }
    
    public void backtrack( String comb, String remains )
    {
        if( remains.length() == 0 )
        {
            sol.add( comb );
            return;
        }
        
        String digit = remains.substring( 0, 1 );
        String letters = map.get( digit );

        for( int i = 0; i < letters.length(); i++ )
        {
            String l = letters.substring( i, i+1 );
            // add the letter to comb then recursive call
            backtrack( comb + l, remains.substring( 1 ) );
        }
    }
}