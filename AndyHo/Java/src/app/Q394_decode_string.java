// ref. https://leetcode.com/problems/decode-string/discuss/87534/Simple-Java-Solution-using-Stack

package app;

import java.util.*;

class Q394_decode_string
{
    public String decodeString(String s)
    {
        String res = "";
        Stack<String> res_stack = new Stack<String>();
        Stack<Integer> cnt_stack = new Stack<Integer>();
        
        int idx = 0;
        while( idx < s.length() )
        {
            if( Character.isDigit( s.charAt( idx) ) )
            {
                int count = 0;
                while( Character.isDigit( s.charAt( idx ) ) )
                {
                    count = 10 * count + s.charAt( idx ) - '0';
                    idx++;
                }
                cnt_stack.push( count );
            }
            else if( s.charAt( idx ) == '[' )
            {
                res_stack.push( res );
                res = "";
                idx++;
            }
            else if( s.charAt( idx ) == ']' )
            {
                // previous stored result, consider 'a' in the case "3[a2[c]]"
                String tmp = res_stack.pop();
                int times = cnt_stack.pop();
                
                for( int i = 0; i < times; i++ ) tmp += res;
                // store the current result
                res = tmp;
                idx++;
            }
            else
            {
                // stores the current string to be duplicated
                res += s.charAt( idx );
                idx++;
            }
        }
        return res;
    }
}