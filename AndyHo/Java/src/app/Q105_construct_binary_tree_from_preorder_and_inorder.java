// ref. https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/discuss/34538/My-Accepted-Java-Solution

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
class Q105_construct_binary_tree_from_preorder_and_inorder
{
    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int x) { val = x; }
    }

    public TreeNode buildTree(int[] preorder, int[] inorder) {
        return helper( 0, 0, inorder.length, preorder, inorder );
    }
    
    private TreeNode helper( int parent, int left, int right, int[] preorder, int[] inorder )
    {
        if( parent >= preorder.length || left > right ) return null;
        TreeNode root = new TreeNode( preorder[ parent ] );
    
        int i = left;
        for( ; i < right; i++ )
        {
            if( inorder[ i ] == root.val ) break;
        }
        root.left = helper( parent + 1, left, i-1, preorder, inorder );
        root.right = helper( parent - left + i + 1, i+1, right, preorder, inorder );
        return root;
    }
}