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
class Q145_binary_tree_postorder_traversal_RECURSIVE
{
    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int x) { val = x; }
    }

    List<Integer> sol = new ArrayList<Integer>();

    public List<Integer> postorderTraversal(TreeNode root)
    {
        postorder( root );
        return sol;
    }
    
    public void postorder( TreeNode root )
    {
        if( root == null ) return;
        postorder( root.left );
        postorder( root.right );
        sol.add( root.val );
    }
}