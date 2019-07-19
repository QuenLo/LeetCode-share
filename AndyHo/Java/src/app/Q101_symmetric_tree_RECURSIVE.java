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
class Q101_symmetric_tree_RECURSIVE {

    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int x) { val = x; }
    }

    public boolean isSymmetric(TreeNode root)
    {
        return isMirror( root, root );
    }
    
    public boolean isMirror( TreeNode t_left, TreeNode t_right )
    {
        if( t_left == null && t_right == null ) return true;
        if( t_left == null || t_right == null ) return false;
        return (t_left.val == t_right.val) && isMirror( t_left.left, t_right.right ) && isMirror( t_left.right, t_right.left );
    }
}