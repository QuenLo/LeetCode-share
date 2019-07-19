package app;

class Q14_longest_common_prefix_BF
{
    public String longestCommonPrefix(String[] strs)
    {
        if( strs.length == 0 ) return "";
        // get the min length of the elements
        int min_len = Integer.MAX_VALUE;
        for( String s: strs ) min_len = Math.min( min_len, s.length() );
        if( min_len == 0 ) return "";
        
        String sol = "";
        for( int j = 0; j < min_len; j++ )
        {
            char c = strs[ 0 ].charAt( j );
            for( String s: strs )
                if( s.charAt( j ) != c ) return sol;
            sol += c;
        }
        return sol;
    }
}