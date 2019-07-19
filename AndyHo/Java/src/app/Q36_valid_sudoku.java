// ref. https://leetcode.com/problems/valid-sudoku/discuss/15450/Shared-my-concise-Java-code

package app;

import java.util.*;

class Q36_valid_sudoku
{
    // A Sudoku board (partially filled) could be valid but is not necessarily solvable
    public boolean isValidSudoku( char[][] board )
    {
        for( int i = 0; i < 9; i++ )
        {
            HashSet<Character> row = new HashSet<Character>();
            HashSet<Character> col = new HashSet<Character>();
            HashSet<Character> cube = new HashSet<Character>();
            for( int j = 0; j < 9; j++ )
            {
                // add() returns false if the element already exists
                if( board[i][j] != '.' && !row.add( board[i][j] ) ) return false;
                if( board[j][i] != '.' && !col.add( board[j][i] ) ) return false;

                // for cube traversal
                // '%' for horizontal traversal
                // '/' for vertical traversal
                int row_idx = 3 * (i/3);
                int col_idx = 3 * (i%3);
                if( board[row_idx + j/3][col_idx + j%3] != '.'
                    && !cube.add( board[row_idx + j/3][col_idx + j%3] ) 
                )
                    return false;
            }
        }
        return true;
    }
}