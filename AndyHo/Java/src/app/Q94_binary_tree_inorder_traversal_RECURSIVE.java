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

class Q94_binary_tree_inorder_traversal_RECURSIVE
{
    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int x) { val = x; }
    }

    List<Integer> sol = new ArrayList<Integer>();

    public List<Integer> inorderTraversal(TreeNode root)
    {
        inorder( root );
        return sol;
    }
    
    public void inorder( TreeNode root )
    {
        if( root == null ) return;
        inorder( root.left );
        sol.add( root.val );
        inorder( root.right );
    }
}