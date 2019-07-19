// ref. https://www.cs.cmu.edu/~pattis/15-1XX/common/handouts/ascii.html
// ref. https://leetcode.com/problems/excel-sheet-column-number/discuss/52091/Here-is-my-java-solution

package app;

class Q171_excel_sheet_column_no
{
    public int titleToNumber(String s)
    {
        // '@' = 64, 'A' = 65 in ascii table
        int sol = 0;
        for( int i = 0; i < s.length(); i++ )
            sol = sol * 26 + (s.charAt(i) - '@');
        return sol;   
    }
}