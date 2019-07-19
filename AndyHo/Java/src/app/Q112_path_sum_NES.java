// ref. https://leetcode.com/problems/path-sum/discuss/322285/java-Runtime%3A-0-ms-faster-than-100.00-Memory-Usage%3A-37.3-MB-less-than-99.90

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

class Q112_path_sum_NES {

    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int x) { val = x; }
    }

    public boolean hasPathSum(TreeNode root, int sum)
    {
        // empty tree
        if( root == null ) return false;

        if( root.right == null && root.left == null )
        {
            if( root.val == sum ) return true;
            return false;
        }
        return hasPathSum( root.left, (sum - root.val) ) || hasPathSum( root.right, (sum - root.val) );
    }
}