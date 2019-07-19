package app;

import java.util.*;

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

class Q112_path_sum {

    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int x) { val = x; }
    }
    
    List<Integer> paths = new ArrayList<Integer>();
    
    public boolean hasPathSum(TreeNode root, int sum)
    {
        if( root == null ) return false;
        preorder( root, 0 );
        for( int i = 0; i < paths.size(); i++ )
            if( paths.get( i ) == sum ) return true;
        return false;
    }
    
    public void preorder( TreeNode root, int sum )
    {
        // leaf
        if( root.left == null && root.right == null )
        {
            paths.add( sum + root.val );
            return;
        }
        sum += root.val;
        if( root.left != null )     preorder( root.left, sum );
        if( root.right != null )    preorder( root.right, sum );
    }
}

// improved
// class Q112_path_sum {

//     public class TreeNode {
//         int val;
//         TreeNode left;
//         TreeNode right;
//         TreeNode(int x) { val = x; }
//     }

//     int target = 0;
    
//     public boolean hasPathSum(TreeNode root, int sum)
//     {
//         target = sum;
//         return preorder( root, 0 );
//     }
    
//     public boolean preorder( TreeNode root, int sum )
//     {
//         if( root == null ) return false;
//         // leaf
//         if( root.left == null && root.right == null )
//         {
//             // paths.add( sum + root.val );
//             if( sum + root.val == target ) return true;
//             return false;
//         }
//         return preorder( root.left, sum + root.val ) || preorder( root.right, sum + root.val );
//     }
// }