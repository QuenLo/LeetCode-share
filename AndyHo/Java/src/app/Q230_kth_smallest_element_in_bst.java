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

class Q230_kth_smallest_element_in_bst
{
    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int x) { val = x; }
    }

    int sol = 0, count = 0;
    public int kthSmallest(TreeNode root, int k)
    {
        inorder( root, k );
        return sol;
    }
    
    public void inorder( TreeNode root, int k )
    {
        if( root == null ) return;
        inorder( root.left, k );
        if( ++count == k )
        {
            sol = root.val;
            return;
        }
        inorder( root.right, k );
    }
}