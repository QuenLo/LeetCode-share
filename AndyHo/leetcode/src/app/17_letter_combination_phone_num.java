package app;
import java.util.HashMap;

class Solution
{
    HashMap<String, String> map = new HashMap<String, String>();
    List<String> output = new ArrayList<String>();

    public void backtrack( String comb, String remaining )
    {
        // if there is no more digits to check
        if ( remaining.length() == 0 ) output.add( comb ); // the comb is done
        else
        {
            // iterate over all letters which map the next available digit
            String digit = remaining.substring( 0, 1 );
            String letters = map.get( digit );
            for( int i = 0; i < letters.length(); i++ )
            {
                String l = map.get( digit ).substring( i, i + 1 );
                // append the current letter to the comb and proceed to the next digits
                backtrack( comb + l, remaining.substring( 1 ) );
            }
        }
    }

    public List<String> letterCombinations(String digits)
    {
        map.put( "2", "abc" );
        map.put( "3", "def" );
        map.put( "4", "ghi" );
        map.put( "5", "jkl" );
        map.put( "6", "mno" );
        map.put( "7", "pqrs" );
        map.put( "8", "tuv" );
        map.put( "9", "wxyz" );

        if( digits.length() != 0 ) backtrack( "", digits );
        return output;
    }
}