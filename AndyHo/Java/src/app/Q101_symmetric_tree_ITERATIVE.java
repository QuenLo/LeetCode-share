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
class Q101_symmetric_tree_ITERATIVE {

    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int x) { val = x; }
    }

    public boolean isSymmetric(TreeNode root)
    {
        Queue<TreeNode> q = new LinkedList<TreeNode>();
        q.add( root );  // t_left
        q.add( root );  // t_right
        while( !q.isEmpty() )
        {
            TreeNode t_left = q.poll();
            TreeNode t_right = q.poll();
            if( t_left == null && t_right == null ) continue;
            if( t_left == null || t_right == null ) return false;
            if( t_left.val != t_right.val )         return false;

            q.add( t_left.left );
            q.add( t_right.right );
            q.add( t_left.right );
            q.add( t_right.left );
        }
        return true;
    }
}