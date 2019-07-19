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

class Q337_house_robber_III {

    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int x) { val = x; }
    }

    public int rob(TreeNode root)
    {
        if( root == null ) return 0;
        int[] res = helper( root );
        return Math.max( res[ 0 ], res[ 1 ] );
    }
    
    public int[] helper( TreeNode root )
    {
        int[] res = {0, 0};
        if( root == null ) return res;
        
        int[] left = helper( root.left );
        int[] right = helper( root.right );
        res[ 0 ] = root.val + left[ 1 ] + right[ 1 ];
        res[ 1 ] = Math.max( left[ 0 ], left[ 1 ] ) + Math.max( right[ 0 ], right[ 1 ] );
        return res;
    }
}