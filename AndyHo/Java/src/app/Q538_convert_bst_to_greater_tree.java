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
class Q538_convert_bst_to_greater_tree
{
    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int x) { val = x; }
    }

    int sum = 0;

    public TreeNode convertBST(TreeNode root)
    {
        if( root != null )
        {
            convertBST( root.right );
            sum += root.val;
            root.val = sum;
            convertBST( root.left );
        }
        return root;
    }
}