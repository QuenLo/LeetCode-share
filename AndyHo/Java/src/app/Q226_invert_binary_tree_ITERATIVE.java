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

class Q226_invert_binary_tree_ITERATIVE {

    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int x) { val = x; }
    }

    public TreeNode invertTree(TreeNode root)
    {
        // prevent null input
        if( root == null ) return null;
        
        Queue<TreeNode> q = new LinkedList<TreeNode>();
        q.add( root );
        while( !q.isEmpty() )
        {
            TreeNode cur = q.poll();
            TreeNode tmp = cur.left;
            cur.left = cur.right;
            cur.right = tmp;
            if( cur.left != null ) q.add( cur.left );
            if( cur.right != null) q.add( cur.right );
        }
        return root;
    }
}