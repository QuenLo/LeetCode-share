// ref. https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/discuss/278544/This-should-not-be-hard

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
class Q1028_recover_a_tree_from_preorder
{
    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int x) { val = x; }
    }

    Stack<TreeNode> stack = new Stack<TreeNode>();
    
    public TreeNode recoverFromPreorder(String s)
    {
        // root
        TreeNode root = null;

        // don't increase the i here!
        for( int i = 0; i < s.length(); )
        {
            int level = 0, val = 0;
            // here to increment i
            for( ; i < s.length() && s.substring( i, i+1 ).equals("-"); i++ ) level += 1;
            for( ; i < s.length() && !s.substring( i, i+1 ).equals("-"); i++ ) val = val * 10 + Integer.parseInt( s.substring( i, i+1 ) );

            while( stack.size() > level ) stack.pop();
            
            TreeNode cur = new TreeNode( val );
            
            // to prevent case like 10--7-8
            if( root == null ) root = cur;
            else
            {
                TreeNode parent = stack.peek();
                if( parent.left == null ) parent.left = cur;
                else                      parent.right = cur;
            }
            
            stack.push( cur );
        }
        
        return root;
    }
}