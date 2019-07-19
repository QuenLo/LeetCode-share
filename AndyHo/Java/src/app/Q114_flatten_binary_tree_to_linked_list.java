// ref. https://leetcode.com/problems/flatten-binary-tree-to-linked-list/discuss/36977/My-short-post-order-traversal-Java-solution-for-share

package app;

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Q114_flatten_binary_tree_to_linked_list
{
    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int x) { val = x; }
    }

    public void flatten(TreeNode root)
    {
        // preorder( root );
        flatten( root, null );
        // preorder( root );
    }
    
    private TreeNode flatten( TreeNode root, TreeNode pre )
    {
        if( root == null ) return pre;
        pre = flatten( root.right, pre );    
        pre = flatten( root.left, pre );
        root.right = pre;
        root.left = null;
        pre = root;
        return pre;
    }
    
    // evaluation
    public void preorder( TreeNode root )
    {
        if( root == null ) return;
        System.out.print( Integer.toString( root.val ) + " " );
        preorder( root.left );
        preorder( root.right );
    }
}