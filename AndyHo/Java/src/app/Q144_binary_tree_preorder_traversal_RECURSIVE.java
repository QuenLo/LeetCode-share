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

class Q144_binary_tree_preorder_traversal_RECURSIVE
{
    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int x) { val = x; }
    }

    List<Integer> sol = new ArrayList<Integer>();

    public List<Integer> preorderTraversal(TreeNode root)
    {
        preorder( root );
        return sol;
    }
    
    public void preorder( TreeNode root )
    {
        if( root == null ) return;
        sol.add( root.val );
        preorder( root.left );
        preorder( root.right );
    }
}