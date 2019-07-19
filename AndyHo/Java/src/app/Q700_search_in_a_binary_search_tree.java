// ref. https://leetcode.com/problems/search-in-a-binary-search-tree/discuss/149274/Java-beats-100-concise-method-using-recursion-and-iteration

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
class Q700_search_in_a_binary_search_tree
{
    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int x) { val = x; }
    }

    // public TreeNode searchBST(TreeNode root, int val)
    // {
    //     if( root == null ) return null;
        
    //     if( root.val == val ) return root;
    //     else if( root.val > val )
    //         return searchBST( root.left, val );
    //     else
    //         return searchBST( root.right, val );
    // }

    // logic improved
    public TreeNode searchBST(TreeNode root, int val)
    {
        if( root == null ) return null;
        
        if( root.val == val ) return root;
        else
            return root.val > val? searchBST( root.left, val ) : searchBST( root.right, val );
    }
}