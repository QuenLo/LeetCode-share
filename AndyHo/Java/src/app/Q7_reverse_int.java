package app;

public class Q7_reverse_int {
    public int reverse(int x) {
        if( x == 0 ) return 0;
        String input = Integer.toString( x );
        String sign = "";
        if( input.charAt( 0 ) == '-' || input.charAt( 0 ) == '+' )
        {
            sign = Character.toString( input.charAt( 0 ) );
            input = input.substring( 1 );
        }
        if( input.length() > 32 ) return 0;

        String tmp = "";
        for( int i = input.length() - 1; i >= 0; i-- ){
            if( input.charAt( i ) == '0' && tmp == "" ) continue;
            tmp += Character.toString( input.charAt( i ) );
        }
        tmp = sign + tmp;
        int sol;
        try                     { sol = Integer.parseInt( tmp ); }
        catch( Exception e )    { return 0; }
        if( sol > Integer.MAX_VALUE ) return 0;
        if( sol < Integer.MIN_VALUE ) return 0;
        return sol;
    }
}