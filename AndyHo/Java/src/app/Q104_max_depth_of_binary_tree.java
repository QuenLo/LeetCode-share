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

class Solution {

    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int x) { val = x; }
    }

    public int maxDepth(TreeNode root)
    {
        if( root == null )
            return 0;
        return cal( root, 0 );
    }
    
    public static int cal( TreeNode node, int current )
    {
        current += 1;
        if( node.left == null && node.right == null )   return current;
        
        int left = 0, right = 0;
        if( node.left != null )     left = cal( node.left, current );
        if( node.right != null )    right = cal( node.right, current );
        
        return Math.max( right, left );
    }
}