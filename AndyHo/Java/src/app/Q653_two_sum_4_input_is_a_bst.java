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
class Q653_two_sum_4_input_is_a_bst
{
    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int x) { val = x; }
    }

    public boolean findTarget(TreeNode root, int k)
    {
        return find( root, k, new HashSet<Integer>() );
    }
    
    public boolean find( TreeNode root, int k, Set<Integer> trace )
    {
        if( root == null ) return false;
        if( trace.contains( k - root.val ) ) return true;
        
        trace.add( root.val );
        boolean left = find( root.left, k, trace );
        boolean right = find( root.right, k, trace );
        return left || right;
    }
}