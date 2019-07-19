package app;

import java.util.HashMap;

public class Q12_int_to_roman {
    HashMap<Integer, String> A = new HashMap<Integer, String>();
    HashMap<Integer, String> B = new HashMap<Integer, String>();
    HashMap<Integer, String> C = new HashMap<Integer, String>();
    HashMap<Integer, String> D = new HashMap<Integer, String>();
    
    public void build_maps()
    {
        A.put( 9, "IX" );
        A.put( 8, "VIII" );
        A.put( 7, "VII" );
        A.put( 6, "VI" );
        A.put( 5, "V" );
        A.put( 4, "IV" );
        A.put( 3, "III" );
        A.put( 2, "II" );
        A.put( 1, "I" );
        
        B.put( 9, "XC" );
        B.put( 8, "LXXX" );
        B.put( 7, "LXX" );
        B.put( 6, "LX" );
        B.put( 5, "L" );
        B.put( 4, "XL" );
        B.put( 3, "XXX" );
        B.put( 2, "XX" );
        B.put( 1, "X" );
        
        C.put( 9, "CM" );
        C.put( 8, "DCCC" );
        C.put( 7, "DCC" );
        C.put( 6, "DC" );
        C.put( 5, "D" );
        C.put( 4, "CD" );
        C.put( 3, "CCC" );
        C.put( 2, "CC" );
        C.put( 1, "C" );
        
        D.put( 3, "MMM" );
        D.put( 2, "MM" );
        D.put( 1, "M" );
    }
    
    public String intToRoman(int num)
    {
        build_maps();
        
        String input = Integer.toString( num );
        String sol = "";
        
        int level = -1;
        for( int i = input.length() - 1; i >= 0; i-- )
        {
            level++;
            int val = Character.getNumericValue( input.charAt( i ) );
            if( val == 0 ) continue;
            switch( level )
            {
                case 0: sol = A.get( val ) + sol; break;
                case 1: sol = B.get( val ) + sol; break;
                case 2: sol = C.get( val ) + sol; break;
                case 3: sol = D.get( val ) + sol; break;
            }
        }
        return sol;
    }
}