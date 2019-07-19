package app;

import java.lang.Math;

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

class Q543_diameter_of_binary_tree {

    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int x) { val = x; }
    }

    // at first, there are "1" node on the path (path length = 0)
    int sol = 1;
    public int diameterOfBinaryTree(TreeNode root)
    {
        depth( root );
        // the ans should be "(num. of nodes on path) - 1"
        return sol - 1;
    }
    
    // count number of "nodes" on the path!
    public int depth( TreeNode root )
    {
        if( root == null ) return 0;
        int left = depth( root.left );
        int right = depth( root.right );
        // missing part
        sol = Math.max( sol, (left + right + 1) );
        return Math.max( left, right ) + 1;
    }
}