// ref. https://leetcode.com/problems/path-sum-iii/discuss/328137/10ms-simple-Java-DFS

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

class Q437_path_sum_III {

    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int x) { val = x; }
    }

    int target = 0, count = 0;
    public int pathSum(TreeNode root, int sum) {
        target = sum;
        helper( root );
        return count;
    }
    
    public void helper( TreeNode root )
    {
        if( root == null ) return;
        dfs( root, 0 );
        // make every node have chance to become the head of a path
        helper( root.left );
        helper( root.right );
    }
    
    // find solution from all the paths starting at the given root
    public void dfs( TreeNode root, int tmp )
    {
        if( root == null ) return;
        tmp += root.val;
        if( tmp == target ) count++;

        dfs( root.left, tmp );
        dfs( root.right, tmp );
    }
}