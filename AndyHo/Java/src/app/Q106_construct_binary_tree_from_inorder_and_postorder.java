// ref. https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/discuss/34803/Sharing-my-straightforward-recursive-solution

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
class Q106_construct_binary_tree_from_inorder_and_postorder
{
    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int x) { val = x; }
    }

    public TreeNode buildTree(int[] inorder, int[] postorder) {
        return helper( 0, inorder.length - 1, 0, postorder.length - 1, postorder, inorder );
    }
    
    private TreeNode helper( int in_start, int in_end, int post_start, int post_end, int[] postorder, int[] inorder )
    {
        if( post_start > post_end ) return null;

        TreeNode root = new TreeNode( postorder[ post_end ] );

        int i = in_end;
        for( ; i >= 0; i-- )
            if( inorder[ i ] == root.val ) break;

        root.left = helper( in_start, i-1, post_start, (post_start + i - in_start - 1), postorder, inorder );
        root.right = helper( i+1, in_end, (post_end - in_end + i), (post_end - 1), postorder, inorder );
        return root;
    }
}