// ref. http://javatutorialhq.com/java/util/hashmap-class/getordefault-method-example/

package app;

import java.util.*;

class Q242_valid_anagram
{
    Map<String, Integer> map = new HashMap<String, Integer>();
    public boolean isAnagram(String s, String t)
    {
        if( s.length() != t.length() ) return false;

        for( int i = 0; i < s.length(); i++ )
        {
            String c = s.substring( i, i+1 );
            map.put( c, map.getOrDefault( c, 0 ) + 1 );
        }
        for( int i = 0; i < t.length(); i++ )
        {
            String c = t.substring( i, i+1 );
            if( !map.containsKey( c ) ) return false;
            map.put( c, map.get( c ) - 1 );
        }
        for( String c: map.keySet() )
            if( map.get( c ) != 0 ) return false;

        return true;
    }
}