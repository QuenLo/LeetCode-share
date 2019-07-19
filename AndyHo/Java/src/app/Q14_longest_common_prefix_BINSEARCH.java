package app;

class Q14_longest_common_prefix_BINSEARCH
{
    String longestCommonPrefix( String[] strs )
    {
        if( strs.length == 0 ) return "";
        // get the min length of the elements
        int min_len = Integer.MAX_VALUE;
        for( String s: strs ) min_len = Math.min( min_len, s.length() );
        if( min_len == 0 ) return "";
        
        // choose one of an element to do the separation
        // the solution use the element arr[0]
        int low = 1;
        int high = min_len; // min_len will never cause any overflow
        while( low <= high )
        {
            int mid = (low + high) / 2;
            if( isCommonPrefix( strs, mid ) ) low = mid + 1;
            else                              high = mid - 1;
        }
        return strs[ 0 ].substring( 0, ((low + high) / 2) );
    }
    
    public boolean isCommonPrefix( String[] strs, int len )
    {
        // since it's "prefix", the left index will always be 0
        String to_try = strs[ 0 ].substring( 0 ).substring( 0, len );
        for( String s: strs )
            if( !s.startsWith( to_try ) ) return false;
        return true;
    }
}