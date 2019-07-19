// ref. https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/discuss/33815/My-accepted-JAVA-solution

package app;

import java.util.*;

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Q103_binary_tree_zigzag_level_order_traversal
{
    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int x) { val = x; }
    }

    public List<List<Integer>> zigzagLevelOrder(TreeNode root)
    {
        List<List<Integer>> sol = new ArrayList<List<Integer>>();
        if( root == null ) return sol;
        
        traverse( root, sol, 0 );
        return sol;
    }
    
    public void traverse( TreeNode cur, List<List<Integer>> sol, int level )
    {
        if( cur == null ) return;
        // '=' for the first iteration
        if( sol.size() <= level )
        {
            List<Integer> tmp = new ArrayList<Integer>();
            sol.add( tmp );
        }
        
        List<Integer> cur_level = sol.get( level );
        if( level % 2 == 0 )
            cur_level.add( cur.val );
        else
            cur_level.add( 0, cur.val );
        
        traverse( cur.left, sol, level+1 );
        traverse( cur.right, sol, level+1 );
    }
}