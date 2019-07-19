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

class Q226_invert_binary_tree_RECURSIVE {
    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int x) { val = x; }
    }

    public TreeNode invertTree(TreeNode root)
    {
        if( root == null ) return null;

        TreeNode right = invertTree( root.right );
        TreeNode left = invertTree( root.left );
        root.right = left;
        root.left = right;
        
        return root;
    }
}